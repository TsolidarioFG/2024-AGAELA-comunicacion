from torch.utils.data import Dataset
import os
import numpy as np
from scipy.ndimage import gaussian_filter1d
from Conjuntos import Conjuntos
import torch
import matplotlib.pyplot as plt


class DatasetEntero(Dataset):
    """
    Clase que hereda de Dataset y que se encarga de cargar los datos de texto y las imagenes

    """

    def __init__(self, datos, sigma = 5, conjunto=1, img_dir=None):
        """
        Inicializa la clase con los datos de texto y las imagenes si corresponde

        Args:
            datos (str): Nombre de la carpeta de datos
            sigma (int): Sigma del filtro gaussiano para el suavizado
            conjunto (int): Conjunto de datos a utilizar (PREPROCESADO)
            img_dir (str): Directorio de las imagenes

        """

        # Establecer los directorios de los txts
        self.img_dir = img_dir
        txt_input_file = f'./entrenamiento/datos/txts/{datos}/input.txt'
        txt_output_file = f'./entrenamiento/datos/txts/{datos}/output.txt'

        # Cargar los datos de texto que no ocupan tanto espacio en el init
        self.txt_input_data = np.loadtxt(txt_input_file, delimiter=',')
        self.txt_output_data = np.loadtxt(txt_output_file, delimiter=',')
        self.sigma = sigma
        self.conjunto = conjunto
        self.personas = self.get_indices_persona()

        # Obtener las personas 
        unique_persons = np.unique(self.personas)

        # Para cada persona en los datos suaivzar los datos
        for person in unique_persons:
            indices = np.where(self.personas == person)[0]
            for i in range(self.txt_input_data.shape[1]-2):
                # Suavizar los datos para esta persona y esta columna
                self.txt_input_data[indices, i] = gaussian_filter1d(self.txt_input_data[indices, i], sigma)


        # Borrar los datos con el ojo cerrado
        indices = np.where(self.txt_input_data[-2]<self.txt_input_data[-1])[0]
        self.txt_input_data = np.delete(self.txt_input_data, indices, axis=0)
        self.txt_output_data = np.delete(self.txt_output_data, indices, axis=0)
        self.personas = np.delete(self.personas, indices)

        # Transformar los datos al conjunto de entrenamiento
        if conjunto is not None:
            normalizar_funcion = getattr(Conjuntos, f'conjunto_{self.conjunto}')
            self.txt_input_data = normalizar_funcion(self.txt_input_data)

        # Obtener el .pt de las imagenes y borrar las posiciones de los ojos cerrados
        if self.img_dir is not None:
          img_dir = os.path.join(self.img_dir, 'imagenes.pt')
          self.imgs = torch.load(img_dir)

          self.imgs = torch.stack(self.imgs)
          self.imgs = np.delete(self.imgs, indices, axis=0)

          self.imgs = torch.tensor(self.imgs, dtype=torch.float32).to('cuda')
        
        # Mover los datos a la GPU
        self.txt_input_data = torch.tensor(self.txt_input_data, dtype=torch.float32).to('cuda')
        self.txt_output_data = torch.tensor(self.txt_output_data, dtype=torch.float32).to('cuda')



    def __len__(self):
        """
        Devuelve la longitud del dataset

        Returns:
            int: Longitud del dataset
        
        """

        return len(self.txt_input_data)



    def __getitem__(self, idx):
        """
        Devuelve los datos de texto y las imagenes si corresponde

        Args:
            idx (int): Indice del dataset
        
        Returns:
            torch.tensor: Datos de texto de entrada
            torch.tensor: Imagenes (si img_dir no es None)
            torch.tensor: Datos de texto de salida
        
        """
        txt_input_data = self.txt_input_data[idx]
        txt_output_data = self.txt_output_data[idx]
        if self.img_dir is not None:
            return txt_input_data, self.imgs[idx], txt_output_data
        else:
            return txt_input_data, txt_output_data



    def get_indices_persona(self):
        """
        Devuelve los indices de las personas en los datos

        Returns:
            list: Lista con los indices de las personas

        """
        personas = []
        contador = 1
        for i in range(len(self.txt_output_data)):
            if i == 0 or self.txt_output_data[i][1] != 0.0 or self.txt_output_data[i-1][1] == 0.0:
                personas.append(contador)
            else:
                contador += 1
                personas.append(contador)
        return personas