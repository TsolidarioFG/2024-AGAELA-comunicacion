from kivy.app import App
from ModelViewPresenter.Modelo import Modelo
from ModelViewPresenter.Vista import Vista
from ModelViewPresenter.Presenter import Presenter
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.config import Config
from ajustes.utils import get_recurso
Window.fullscreen = 'auto'
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class MyApp(App):
    """
    Clase principal de la aplicación, se encarga de inicializar el modelo, la vista y el presenter.
    Es la encargada de iniciar la aplicación y construirla.    
    """
    def build(self):
        self.title = 'ComunicELA'  
        self.icon = get_recurso("imagenes/logo.png")  
        LabelBase.register(name='Titulo', fn_regular=get_recurso('KivyCustom/fuentes/Orbitron-Regular.ttf'))
        LabelBase.register(name='Texto', fn_regular=get_recurso('KivyCustom/fuentes/FrancoisOne-Regular.ttf'))

        self.modelo = Modelo()
        vista = Vista()
        controlador = Presenter(self.modelo, vista)
        vista.set_controlador(controlador)
        vista.crear_pantallas()

        return vista.sm
    
    def on_stop(self):
        # Detiene la cámara antes de cerrar la aplicación
        self.modelo.detener_camara()

if __name__ == '__main__':        
    MyApp().run()
