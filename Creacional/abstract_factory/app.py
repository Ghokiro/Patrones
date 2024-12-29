"""
    Codificar una app de tarjetas bancarias donde se fabriquen familias
    de Tarjetas (ej: Visa clásica, Visa Oro, Visa Platinum)
"""
""" LIBRERÍAS 
    - abc: para abstracción.
    - datetime: para obtener el año actual y generar fecha de vencimiento futuros.
    - random: Para generar fechas y códigos aleatorios.
"""
from abc import ABC, abstractmethod
from datetime import datetime
from random import randint

""" Atributos base de tarjetas"""
class Atributos:
    """
        La clase Atributos declara los atributos para las tarjetas

        Atributos:
            - marca: Almacena la marca de la tarjeta. Ejemplo: Visa, Mastercard, etc.
            - tipo: Almacena el tipo de la tarjeta. Ejemplo: Clásica, Gold, Platinum...
            - numeracion: Almacena el número de la tarjeta. Ejemplo: 4XXX XXXX XXXX XXXX
            - vencimiento: Almacena la fecha de vencimiento de la Tarjeta. Ejemplo: 06/29 (mes 6 del año 2029)
            - cvc: almacena el código de tres dígitos de la parte trasera de la tarjeta. Ejemplo: 099

            Metodo Get Obtener Atributos: retorna un diccionario con la información de la tarjeta.
    """
    def __init__(self, marca: str, tipo: str, numeracion: str, vencimiento: str, cvc: str, beneficios: set) -> None:
        self.marca = marca
        self.tipo = tipo
        self.numeracion = numeracion
        self.vencimiento = vencimiento
        self.cvc = cvc
        self.beneficios = beneficios

    @property
    def obtener_atributos(self) -> dict:
        return {
            "marca": self.marca,
            "tipo": self.tipo,
            "numeracion": self.numeracion,
            "vencimiento": self.vencimiento,
            "cvc": self.cvc,
            "beneficios": self.beneficios
        }


""" INTERFAZ ABSTRACTA PRINCIPAL """
class Tarjeta(ABC):
    """ La clase Tarjeta declara los atributos y la propiedad que requerirán las clases hereditarias

        Atributos de la clase:
            - información: atributo protegido que almacena la información de los atributos de la tarjeta.
                Más adelante se le asigna la clase Atributos.
            - beneficios: atributo protegido de tipo set, almacena el conjunto de beneficios de la tarjeta.
    """
    def __init__(self) -> None:
        self._informacion = None
    @abstractmethod
    def generar_atributos(self, emisor_bancario: str, codigo_titular: str, vencimiento: str, cvc) -> None:
        pass

    def __str__(self) -> str:
        return f"{self._informacion.obtener_atributos}\n\n"

""" INTERFAZ PRODUCTO CONCRETO PRINCIPAL """
class TarjetaVisa(Tarjeta):
    def __init__(self) -> None:
        super().__init__()
        self._marca = "VISA"
        self._numeracion = NumeracionTarjeta('4')

    @abstractmethod
    def generar_atributos(self, emisor_bancario: str, codigo_titular: str, vencimiento: str, cvc) -> None:
        pass

""" PRODUCTO CONCRETO VISA """
""" Visa Tipo Clásica """
class TarjetaVisaClasica(TarjetaVisa):
    """ La clase Tarjeta Visa Clásica hereda de Tarjeta Visa.
            - Genera los atributos como predeterminado para la tarjeta.

        Metodo generar atributo:
            Genera los atributos con los cuales debe contar la tarjeta visa clásica. No retorna valor

    """
    def generar_atributos(self, emisor_bancario: str, codigo_titular: str, vencimiento: str, cvc) -> None:
        numeracion_completa = self._numeracion.generar_codigo(emisor_bancario, codigo_titular)
        beneficios = {"Compra en Linea"}
        self._informacion = Atributos(self._marca, "Clasica", numeracion_completa, vencimiento, cvc, beneficios)


""" Visa Tipo Gold """
class TarjetaVisaGold(TarjetaVisa):
    def generar_atributos(self, emisor_bancario: str, codigo_titular: str, vencimiento: str, cvc) -> None:
        numeracion_completa = self._numeracion.generar_codigo(emisor_bancario, codigo_titular)
        beneficios = {"Compra en Linea", "Menos Limitado que la tarjeta clásica"}
        self._informacion = Atributos(self._marca, "Gold", numeracion_completa, vencimiento, cvc, beneficios)

""" Visa Tipo Platinum """
class TarjetaVisaPlatinum(TarjetaVisa):
    def generar_atributos(self, emisor_bancario: str, codigo_titular: str, vencimiento: str, cvc) -> None:
        numeracion_completa = self._numeracion.generar_codigo(emisor_bancario, codigo_titular)
        beneficios = {"Compra en Linea", "Sin limite", "Genera intereses"}
        self._informacion = Atributos(self._marca, "Gold", numeracion_completa, vencimiento, cvc, beneficios)


""" FABRICA DE TARJETAS """
class FabricaTarjeta(ABC):
    @abstractmethod
    def fabricar_tarjeta(self, tipo: str, emisor_bancario: str, codigo_titular: str) -> Tarjeta: pass

""" FÁBRICA DE TARJETAS VISA """
class FabricaTarjetaVisa(FabricaTarjeta):
    """
        La fábrica de Tarjetas visa genera el tipo de tarjeta visa requerido por el cliente.

        Metodo Fabricar Tarjeta:
            Retorna la tarjeta requerida por el usuario/cliente con los atributos asignados.

            Parámetros:
                - tipo: Recibe el tipo de tarjeta que el cliente requiere (ej.: Clásica, Gold, Platinum, etc.)
                - emisor bancario: recibe el código del emisor que forma parte de la numeración de la tarjeta.
                - codigo titular: Recibe el código de identificación interna de la tarjeta que forma parte de
                    la numeración.

            Variables:
                - tipo: convierte el valor del parámetro tipo a mayúscula.
                - dict_tarjeta: diccionario de tarjetas disponibles de la marca, sustituye las condicionales
                    if-else
                - tarjeta: almacena la tarjeta extraída del diccionario y genera los valores para los atributos.

    """
    def fabricar_tarjeta(self, tipo: str, emisor_bancario: str, codigo_titular: str) -> Tarjeta:
        tipo = str.upper(tipo)
        dict_tarjeta: dict[str, TarjetaVisa] = {
            'CLASICA': TarjetaVisaClasica(),
            'GOLD': TarjetaVisaGold(),
            "PLATINUM": TarjetaVisaPlatinum(),
        }
        if tipo not in dict_tarjeta:
            raise TypeError(f"El tipo {tipo} no se está disponible")

        tarjeta = dict_tarjeta[tipo]
        tarjeta.generar_atributos(emisor_bancario, codigo_titular, Vencimiento.generar(), CVC.generar())

        return tarjeta

""" NUMERACIÓN DE TARJETA """
class NumeracionTarjeta:
    """
        La clase Numeración de tarjeta se utiliza para retornar la numeración de la tarjeta formateada

        Atributos:
         - codigo: atributo privado que recibe el código de la tarjeta, que es el número inicial de la numeración

        Método
        - generar código: convierte el código del tipo de tarjeta, el código del emisor bancario y
            el código de la cuenta titular en una cadena con espacio cada 4 dígitos y retorna
            el resultado
    """

    def __init__(self, codigo: str) -> None:
        self.__codigo = codigo

    def generar_codigo(self, emisor_bancario: str, codigo_titular: str) -> str:
        numeracion = ''.join([self.__codigo, emisor_bancario, codigo_titular])
        return ' '.join([numeracion[i: i + 4] for i in range (0, len(numeracion), 4)])


""" Clase Vencimiento: Proporciona un método para generar la fecha de vencimiento de la tarjeta """
class Vencimiento:
    @staticmethod
    def generar() -> str:
        anio = datetime.now().year
        return f"{randint(1, 12)}/{randint(anio + 4, anio + 8)}"

""" Clase CVC: Proporciona un método para generar el CVC de la tarjeta """
class CVC:
    @staticmethod
    def generar() -> str:
        return f"{randint(0, 9)}{randint(0, 9)}{randint(1, 9)}"

""" ARRANQUE DE LA APP """
if __name__ == "__main__":
    emisor = "123456"
    cuenta = "000000001"

    visa_gold = FabricaTarjetaVisa().fabricar_tarjeta('gold', emisor, cuenta)

    emisor = "123400"
    cuenta = "000050001"
    visa_clasica = FabricaTarjetaVisa().fabricar_tarjeta('clasica', emisor, cuenta)

    emisor = "000000"
    cuenta = "000050088"

    visa_platinum = FabricaTarjetaVisa().fabricar_tarjeta("platinum", emisor, cuenta)

    [print(x.__str__()) for x in [visa_clasica, visa_gold, visa_platinum]]





