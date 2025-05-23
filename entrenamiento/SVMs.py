import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import ParameterGrid
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from DatasetEntero import DatasetEntero

"""
Fichero donde se evalúa mediante una busqueda de hiperparámetros el modelo de SVMs que mejor se ajusta a los datos

"""

class SVMs:
    """
    Clase que contiene los modelos de SVMs que se van a entrenar
    
    """
    def __init__(self):
        pass

    def crear_svm(self, kernel='rbf', C=1.0, epsilon=1):
        """
        Crea un modelo de SVM con los hiperparámetros dados

        Args:
            kernel (str): Tipo de kernel a utilizar.
            C (float): Parámetro de regularización.
            epsilon (float): Parámetro de la función de pérdida.

        Returns:
            Pipeline: Modelo de SVM.
        """
        # Se crean dos modelos, uno para cada salida
        model = make_pipeline(StandardScaler(), MultiOutputRegressor(SVR(kernel=kernel, C=C, epsilon=epsilon)))
        return model



def euclidean_loss(y_true, y_pred):
    """
    Calcula la pérdida euclidiana entre dos vectores
    
    Args:
        y_true (np.array): Vector verdadero
        y_pred (np.array): Vector predicho

    Returns:
        float: Pérdida euclidiana
    """
    return np.sqrt(np.sum((y_pred - y_true) ** 2, axis=-1)).mean()



def filtrar_parametros(param_grid):
    """
    Evita que haya combinaciones redundantes de parámetros ya que algunos parámetros no pueden estar juntos

    Args:
        param_grid (dict): Parámetros a combinar
    
    Returns:
        list: Lista de combinaciones de parámetros sin redundancias

    """
    combinaciones = list(ParameterGrid(param_grid))
    combinaciones_filtradas = []

    for params in combinaciones:
        kernel = params['multioutputregressor__estimator__kernel']
        if kernel == 'linear':
            if 'multioutputregressor__estimator__degree' in params or 'multioutputregressor__estimator__gamma' in params:
                continue
        elif kernel == 'rbf':
            if 'multioutputregressor__estimator__degree' in params:
                continue
        combinaciones_filtradas.append(params)

    for params in combinaciones_filtradas:
        for key in params:
            if not isinstance(params[key], list):
                params[key] = [params[key]]

    return combinaciones_filtradas



def entrenar_con_kfold_grid_search(modelo, dataset, param_grid):
    """
    Entrena un modelo con validación cruzada y búsqueda de hiperparámetros

    Args:
        modelo (function): Función que crea un modelo de SVM.
        dataset (DatasetEntero): Dataset con los datos.
        param_grid (dict): Parámetros a combinar.

    Returns:
        list: Lista con los resultados de cada combinación de parámetros.

    """
    cambios_de_persona = dataset.get_indices_persona()
    numero_de_persona = len(np.unique(cambios_de_persona))
    resultados = []

    # Rebaja la cantidad de datos para que sea más rápida la búsqueda
    reductor = 5
    X, y = dataset[:]
    X = X.cpu().numpy()[::reductor]
    y = y.cpu().numpy()[::reductor]
    cambios_de_persona = cambios_de_persona[::reductor]

    for params in ParameterGrid(param_grid):
        fold_mse_losses = []
        fold_euclidean_losses = []
        print("\n\n Busqueda numero ", len(resultados), " de ", len(list(ParameterGrid(param_grid))), " Parametros: ", params)
        for i in range(numero_de_persona):
            # Obtener los índices de entrenamiento y prueba para esta persona
            train_indices = [idx for idx, persona in enumerate(cambios_de_persona) if persona != i+1]
            val_indices = [idx for idx, persona in enumerate(cambios_de_persona) if persona == i+1]

            # Modelo nuevo para cada fold
            model = modelo()

            X_train, y_train = X[train_indices], y[train_indices]
            X_val, y_val = X[val_indices], y[val_indices]

            # Entrenar y evaluar
            model.set_params(**params)
            model.fit(X_train, y_train)
            y_val_pred = model.predict(X_val)
            fold_mse_losses.append(mean_squared_error(y_val, y_val_pred))
            fold_euclidean_losses.append(euclidean_loss(y_val, y_val_pred))

        mean_mse_loss = np.mean(fold_mse_losses)
        std_mse_loss = np.std(fold_mse_losses)
        mean_euclidean_loss = np.mean(fold_euclidean_losses)
        std_euclidean_loss = np.std(fold_euclidean_losses)

        resultados.append((params, mean_mse_loss, std_mse_loss, mean_euclidean_loss, std_euclidean_loss))
        print(f"Pérdida media MSE: {mean_mse_loss}, Desviación estándar MSE: {std_mse_loss}, Pérdida media Euclidiana: {mean_euclidean_loss}, Desviación estándar Euclidiana: {std_euclidean_loss}")
        print(f"Mejor resultado hasta ahora: {min(resultados, key=lambda x: x[1])}")

    best_params = min(resultados, key=lambda x: x[1])[0]
    best_result = min(resultados, key=lambda x: x[1])
    print(f"Mejores parámetros: {best_params}")
    print(f"Resultados del mejor modelo - Pérdida media MSE: {best_result[1]}, Desviación estándar MSE: {best_result[2]}, Pérdida media Euclidiana: {best_result[3]}, Desviación estándar Euclidiana: {best_result[4]}")


if __name__ == '__main__':
    # cargar el dataset
    dataset = DatasetEntero("texto_solo")

    # Parametros de la busqueda
    param_grid = {
        'multioutputregressor__estimator__C': [0.01, 0.1, 1, 10, 100],
        'multioutputregressor__estimator__epsilon': [0.0001, 0.001, 0.01, 0.1],
        'multioutputregressor__estimator__kernel': ['linear', 'rbf', 'poly'],
        'multioutputregressor__estimator__degree': [1, 2],  # Para kernel polinómico
        'multioutputregressor__estimator__gamma': ['scale', 'auto', 0.1, 1] 
    }

    # Filtrar los parámetros para que no haya combinaciones redundantes
    param_grid_filtrado = filtrar_parametros(param_grid)

    # Buscar los mejores parámetros 
    entrenar_con_kfold_grid_search(SVMs().crear_svm, dataset, param_grid_filtrado)
