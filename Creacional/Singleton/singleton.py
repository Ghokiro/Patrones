""" EJERCICIO DE SINGLETON """
""" En este módulo se desarrolla un ejercicio práctico sobre un generador de códigos de numeración 
        de tarjetas bancarias (al menos solo el titular en esta ocasión)
            utilizando el patrón de diseño Singleton con principios SOLID.
"""

""" LIBRERIAS """
from abc import ABCMeta, ABC, abstractmethod

""" Interfaz para metodos de Codigo Titular """
class ICodigo(ABC):
    """ Implementa los metodos para la obtencion del codigo generado en la instancia """
    @abstractmethod
    def obtener_codigo(self) -> int:
        """ Implementar en clases hijas """

    @abstractmethod
    def obtener_nuevo_codigo(self) -> int:
        """ Implementar en clases hijas """

""" Interfaz de Formatos para Códigos """
class IFormatoCodigo(metaclass=ABCMeta):
    """ Interface Principal para metodo de formato códigos de numeración de tarjetas bancarias """
    @staticmethod
    @abstractmethod
    def generar_formato(codigo: ICodigo) -> str:
        """ Implementar en clases hijas """

""" IMPLEMENTACIÓN DE SINGLETON """
class SingletonMeta(type):
    """ Establece que las clases hijas sean instanciadas una sola vez """
    _instancias: dict = {}

    """ Verificar si la clase heredera ha sido instanciada por primera vez """
    def __call__(cls, *args: any, **kwargs: any):
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]

""" COMBINACION DE METAS ABCMeta y SingletonMeta"""
class ABCSingletonMeta(ABCMeta, SingletonMeta):
    """ Combina las metaclases ABCMeta y Singleton para evitar error """
    pass

""" CLASE CODIGO TITULAR """
class CodigoTitular(ICodigo, metaclass=ABCSingletonMeta):
    """ Sirve como generador de codigo titular para la tarjeta bancaria """
    def __init__(self):
        self.__codigo = 0

    def obtener_codigo(self) -> int:
        return self.__codigo

    def obtener_nuevo_codigo(self) -> int:
        self.__codigo += 1
        return self.__codigo

""" CLASE FORMATO CODIGO TITULAR"""
class FormatoCodigoTitular(IFormatoCodigo):
    """ Genera el formato para el código titular de la tarjeta bancaria """
    @staticmethod
    def generar_formato(codigo: ICodigo) -> str:
        codigo_str = str(codigo.obtener_codigo())
        return "0" * (6 - len(codigo_str)) + codigo_str


""" ARRANQUE DE LA APLICACIÓN """
if __name__ == "__main__":
    """ Al iniciar el programa ejecuta las lineas de codigo descritas en esta condición"""
    c1 = CodigoTitular()
    c2 = CodigoTitular()

    n1 = c1.obtener_nuevo_codigo()
    n2 = c2.obtener_codigo()
    print(c1 == c2)
    print(n1 == n2, f"{n1}")

    print("Codigo Titular Formateado: ", FormatoCodigoTitular.generar_formato(c1))