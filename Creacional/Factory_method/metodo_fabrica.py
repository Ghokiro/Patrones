""" Instrucciones:
    - Codificar un software que permita crear tarjetas de débitos
    MasterCard, Visa y American Express

"""
import datetime
from random import randint

""" Se importa la librería que permite la abstracción """
from abc import ABC, abstractmethod

""" DICCIONARIO DE BANCOS POR PAISES """
bancos = { # self.__bancos[pais][banco]
        "X": {
            "BANCO 1": "000001",
            "BANCO 2": "000002",
            "BANCO 3": "000003",
            "BANCO 4": "000005"
        },
        "Y": {
            "BANCO 1": "000011",
            "BANCO 2": "000022",
            "BANCO 3": "000033",
            "BANCO 4": "000045"
        }
    }


""" Creación de clase para atributos base """
class Atributos:
    def __init__(self, marca: str, numeracion: str, vencimiento: str, cvc: str):
        self.__atributos = {
            "marca": marca,
            "numeracion": numeracion,
            "vencimiento": vencimiento,
            "cvc": cvc
        }

    @property
    def mostrar(self) -> dict:
        return self.__atributos

""" INTERFAZ PRINCIPAL """
""" Se implementa la interfaz principal """
class Tarjeta(ABC):
    def __init__(self) -> None:
        self._atributos = None
        self._atributos_generados: bool = False

    @property
    def obtener_atributos(self) -> dict:
        return self._atributos.mostrar

    """ El metodo generar_atributos obliga a las subclases a generar sus propias tarjetas bancarias"""
    @abstractmethod
    def generar_atributos(self, banco_emisor: str, cuenta_titular: str) -> None:
        pass

""" PRODUCTOS CONCRETOS """
""" Se implementa la clase de producto concreto para la tarjeta visa """
class TarjetaVisa(Tarjeta):
    def generar_atributos(self, banco_emisor: str, cuenta_titular: str) -> None:
        """
            Variables:
                - anio: esta variable almacena el año actual para ser procesado en la fecha de vencimiento de la Tarjeta.
                - vencimiento: almacena la fecha de vencimiento completa, utiliza números aleatorios para el mes
                    y el año posterior al actual.
                - numeración: almacena la numeración de la tarjeta bancaria teniendo en cuenta el código de la marca,
                    el banco emisor y el número de la cuenta titular (ejemplo para visa: 4XXXX XXXX XXXX)
                - marca: almacena la marca proveedora de la tarjeta.
                - cvc: almacena el código de tres dígitos de la parte trasera de la tarjeta bancaria. Se crean
                    de manera aleatoria.

            Atributos:
                - atributos: almacena los valores de las variables declaradas. Registra los datos de la tarjeta.
        """

        """ Condicional que bloquea la cambiar los atributos de la tarjeta ya generados """
        if self._atributos_generados:
            raise TypeError("No puedes cambiar los datos de la tarjeta")

        anio = datetime.datetime.now().year
        vencimiento = f"{randint(1, 12)}/{randint(anio + 2, anio + 5)}"

        numeracion = separar_numeracion("4" + banco_emisor + cuenta_titular)
        marca = "VISA"
        cvc = f"{randint(0, 9)}{randint(0, 9)}{randint(1, 9)}"
        self._atributos = Atributos(marca, numeracion, vencimiento, cvc)


""" Se implementa la clase de producto concreto para la tarjeta mastercard """
class TarjetaMastercard(Tarjeta):
    def generar_atributos(self, banco_emisor: str, cuenta_titular: str) -> None:
        """ Condicional que bloquea la cambiar los atributos de la tarjeta ya generados """
        if self._atributos_generados:
            raise TypeError("No puedes cambiar los datos de la tarjeta")

        anio = datetime.datetime.now().year
        vencimiento = f"{randint(1, 12)}/{randint(anio + 3, anio + 7)}"

        numeracion = separar_numeracion("5" + banco_emisor + cuenta_titular)
        marca = "MASTERCARD"
        cvc = f"{randint(0, 9)}{randint(0, 9)}{randint(1, 9)}"
        self._atributos = Atributos(marca, numeracion, vencimiento, cvc)

""" Se implementa la clase de producto concreto para la tarjeta american express """
class TarjetaAmericanExpress(Tarjeta):
    def generar_atributos(self, banco_emisor: str, cuenta_titular: str) -> None:
        """ Condicional que bloquea la cambiar los atributos de la tarjeta ya generados """
        if self._atributos_generados:
            raise  TypeError("No puedes cambiar los datos de la tarjeta")


        anio = datetime.datetime.now().year
        vencimiento = f"{randint(1, 12)}/{randint(anio + 4, anio + 8)}"

        numeracion = separar_numeracion("3" + banco_emisor + cuenta_titular)
        marca = "AMERICAN EXPRESS"
        cvc = f"{randint(0, 9)}{randint(0, 9)}{randint(1, 9)}"
        self._atributos = Atributos(marca, numeracion, vencimiento, cvc)


""" FÁBRICAS """
""" Implementación de la fabrica principal para la creación de los productos de tarjetas"""
class FabricaTarjeta(ABC):
    @abstractmethod
    def fabricar_tarjeta(self, pais: str, banco: str, cuenta_titular: str) -> Tarjeta: pass

""" FÁBRICAS CONCRETAS """
""" Implementación de la fabrica concreta para la creación de productos VISA"""
class FabricaTarjetaVisa(FabricaTarjeta):
    def fabricar_tarjeta(self, pais: str, banco: str, cuenta_titular: str) -> Tarjeta:
        tarjeta = TarjetaVisa()
        tarjeta.generar_atributos(obtener_banco(pais, banco), cuenta_titular)
        return tarjeta

""" Implementación de la fabrica concreta para la creación de productos MasterCard"""
class FabricaTarjetaMastercard(FabricaTarjeta):
    def fabricar_tarjeta(self, pais: str, banco: str, cuenta_titular: str) -> Tarjeta:
        tarjeta = TarjetaMastercard()
        tarjeta.generar_atributos(obtener_banco(pais, banco), cuenta_titular)
        return tarjeta

""" Implementación de la fabrica concreta para la creación de productos American Express"""
class FabricaTarjetaAmericanExpress(FabricaTarjeta):
    def fabricar_tarjeta(self, pais: str, banco: str, cuenta_titular: str) -> Tarjeta:
        tarjeta = TarjetaAmericanExpress()
        tarjeta.generar_atributos(obtener_banco(pais, banco), cuenta_titular)
        return tarjeta


def obtener_banco(pais: str, banco: str) -> str:

    """ Verificación de la existencia del pais y del banco a retornar"""
    pais = str.upper(pais)
    banco = str.upper(banco)
    if pais in bancos:
        if banco in bancos[pais]:
            return bancos[pais][banco]
        raise TypeError(f"El banco {banco} no se encuentra registrado.")
    raise TypeError(f"El país {pais} no existe.")


""" Función para separar la numeración de la tarjeta con espacio cada 4 dígitos"""
def separar_numeracion(numeracion: str) -> str:
    return ' '.join([numeracion[i: i + 4]  for i in range (0, len(numeracion), 4)])

""" función que facilita la creación de las tarjetas bancarias """
def generar_tarjeta(marca: str, pais: str, banco: str, cuenta: str) -> Tarjeta:

    tarjetas = {
        "VISA": FabricaTarjetaVisa(),
        "MASTERCARD": FabricaTarjetaMastercard(),
        "AMERICAN EXPRESS": FabricaTarjetaAmericanExpress()
    }
    marca = str.upper(marca)

    """Verificación de la existencia de la marca de tarjeta """
    if marca in tarjetas:
        tarjeta: FabricaTarjeta = tarjetas[marca]
        return tarjeta.fabricar_tarjeta(pais, banco, cuenta)
    raise TypeError(f"La tarjeta bancaria marca {marca} de tarjeta no existe.")

""" ARRANQUE DE LA APP """
if __name__ == "__main__":
    adolfo_visa = generar_tarjeta('visa', 'Y', "BANCO 1", "000000001")
    adolfo_mastercard = generar_tarjeta('mastercard', 'Y', "BANCO 1", "000000002")
    adolfo_american = generar_tarjeta('american express', 'Y', "BANCO 2", "000000003")

    [print(x) for x in  [   adolfo_visa.obtener_atributos,
                            adolfo_mastercard.obtener_atributos,
                            adolfo_american.obtener_atributos
                        ]
    ]
