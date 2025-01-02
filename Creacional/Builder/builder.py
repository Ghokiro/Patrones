""" Patrón Builder"""

""" Crear un algoritmo que permita crear distintos tipos de cuentas bancarias
    con sus respectivos elementos que lo identifican, utilizando Builder.
    
    Ejemplo:
        * Para una cuenta de ahorros, se deben seguir los siguientes pasos:
            - Habilitar Cuenta de Ahorro
            - Habilitar Seguridad y protección
            - Habilitar acceso a internet banking
            - Habilitar Tarjeta de débito / Libreta (Opcional).
            - Habilitar acceso a servicios de dispositivos automáticos.
            - Asociar tarjeta de crédito (opcional).
        
        * Para una cuenta corriente:
            - Habilitar Cuenta Corriente
            - Habilitar Seguridad y Protección.
            - Habilitar Tarjeta de debito / Libreta (opcional).
            - Habilitar Chequera.
            - Habilitar Internet Banking.
            - Habilitar acceso a servicios de dispositivos automáticos.
            - Habilitar Facilidad para retirar dinero.
            - Habilitar Límites para retirar dinero.
            - Asociar Tarjeta de Crédito (opcional).
                 
"""

""" CLASE PRINCIPAL"""
class Cuenta:
    """ Contiene las propiedades de la cuenta bancaria """
    def __init__(self) -> None:
        self.__tipo_cuenta: str = "Sin Asignar"
        self.__seguridad: str = "Sin Asignar"
        self.__banking: bool = False
        self.__libreta: bool = False
        self.__chequera: bool = False
        self.__dispositivos_automaticos: bool = False
        self.__tarjeta_credito: bool = False
        self.__tarjeta_debito: bool = False
        self.__limite_deuda: float = 0.00
        self.__facilidad_retiro: bool = False

        self.elementos_habilitados = dict()

# class Constructor(ABC):
#
#     @abstractmethod
#     def habilitar_cuenta(self, cuenta: str) -> None: pass
#
#     @abstractmethod
#     def habilitar_seguridad(self, seguridad: str) -> None: pass
#
#     @abstractmethod
#     def habilitar_banking(self, habilitado: bool) -> None: pass
#
#     @abstractmethod
#     def habilitar_dispositivos_automaticos(self, habilitado: bool) -> None: pass
#
#     @abstractmethod
#     def habilitar_limite_deuda(self, limite: float) -> None: pass
#
#     @abstractmethod
#     def habilitar_tarjeta_debito(self, habilitado: bool) -> None: pass
#
#     @abstractmethod
#     def habilitar_libreta(self, habilitado: bool) -> None: pass
#
#     @abstractmethod
#     def habilitar_chequera(self, habilitado: bool) -> None: pass
#
#     @abstractmethod
#     def habilitar_tarjeta_credito(self, habilitado: bool) -> None: pass
#
#     @abstractmethod
#     def habilitar_facilidad_retiro(self, habilitado: bool) -> None: pass

    # def construir_cuenta(self):
    #     return

class Constructor:
    """ Define los pasos necesarios para la construcción de la cuenta bancaria """
    def __init__(self):
        self.__cuenta = Cuenta()

    def habilitar_cuenta(self, cuenta: str = "Ahorros") -> None:
        self.__cuenta.tipo_cuenta = cuenta
        self.__cuenta.elementos_habilitados["Cuenta"] = self.__cuenta.tipo_cuenta
        print("Nueva cuenta de ahorro Asignado.")

    def habilitar_seguridad(self, seguridad: str = "V1") -> None:
        self.__cuenta.seguridad = seguridad
        self.__cuenta.elementos_habilitados["Seguridad"] = self.__cuenta.seguridad
        print("Nueva Version de Seguridad Asignada.")

    def habilitar_banking(self, habilitado: bool = True) -> None:
        self.__cuenta.banking = habilitado
        self.__cuenta.elementos_habilitados["Banking"] = self.__cuenta.banking
        mensaje("Internet Banking", habilitado, 'o')

    def habilitar_dispositivos_automaticos(self, habilitado: bool = True) -> None:
        self.__cuenta.dispositivos_automaticos = habilitado
        self.__cuenta.elementos_habilitados["Dispositivos Automáticos"] = self.__cuenta.dispositivos_automaticos
        mensaje("Dispositivos de Transacciones Automáticos", habilitado, 'os')

    def habilitar_limite_deuda(self, limite: float = 0) -> None:
        self.__cuenta.limite_deuda = limite
        self.__cuenta.elementos_habilitados["Límite de deuda"] = self.__cuenta.limite_deuda
        if limite != 0:
            print(f"Limite de posibilidad de deuda habilitado hasta RD${limite}")

    def habilitar_tarjeta_debito(self, habilitado: bool = True) -> None:
        self.__cuenta.tarjeta_debito = habilitado
        self.__cuenta.elementos_habilitados["Tarjeta Débito"] = self.__cuenta.tarjeta_debito
        mensaje("Tarjeta de Débito", habilitado, 'a')

    def habilitar_libreta(self, habilitado: bool = True) -> None:
        self.__cuenta.libreta = habilitado
        self.__cuenta.elementos_habilitados["Libreta"] = self.__cuenta.libreta
        mensaje("Libreta", habilitado, 'a')

    def habilitar_chequera(self, habilitado: bool = True) -> None:
        self.__cuenta.chequera = habilitado
        self.__cuenta.elementos_habilitados["Chequera"] = self.__cuenta.chequera
        mensaje("Chequera", habilitado, 'a')

    def habilitar_tarjeta_credito(self, habilitado: bool = True) -> None:
        self.__cuenta.tarjeta_credito = habilitado
        self.__cuenta.elementos_habilitados["Tarjeta Crédito"] = self.__cuenta.tarjeta_credito
        mensaje("Tarjeta de Crédito", habilitado, 'a')

    def habilitar_facilidad_retiro(self, habilitado: bool = True) -> None:
        self.__cuenta.facilidad_retiro = habilitado
        self.__cuenta.elementos_habilitados["Facilidades Retiro"] = self.__cuenta.facilidad_retiro
        mensaje("Facilidades de Retiro de dinero", habilitado, 'o')

    """ Retorna la cuenta creada y limpia los campos """
    def obtener_cuenta(self):
        cuenta = self.__cuenta
        self.__cuenta = Cuenta()
        return cuenta


""" Función reutilizable para mostrar cuando una app se ha creado o modificado """
def mensaje(elemento: str, estado: bool, caracteres_finales: str):
    return  f"{elemento} {"des" if not estado else ""}habilitad{caracteres_finales}."

class Director:
    """ Clase directora que ayuda a dirigir la construcción de la cuenta bancaria"""

    """ La función construir cuenta permite al cliente construir una cuenta personalizada, además permite ser 
        reutilizada en cuentas comunes como en cuentas de ahorros y corrientes.
    """
    def construir_cuenta(self, constructor: Constructor,
                                cuenta: str = "No Asignado",
                                seguridad: str = "No Asignado",
                                limite_deuda: float = 0.0,
                                debito: bool = False,
                                libreta: bool = False,
                                credito: bool = False,
                                chequera: bool = False,
                                facilidad_retiro: bool = False) -> Cuenta:

        constructor.habilitar_cuenta(cuenta=cuenta)
        constructor.habilitar_seguridad(seguridad=seguridad)
        constructor.habilitar_limite_deuda(limite=limite_deuda)
        constructor.habilitar_banking()
        constructor.habilitar_dispositivos_automaticos()

        if debito:
            constructor.habilitar_tarjeta_debito()
        if credito:
            constructor.habilitar_tarjeta_credito()
        if libreta:
            constructor.habilitar_libreta()
        if chequera:
            constructor.habilitar_chequera()
        if facilidad_retiro:
            constructor.habilitar_facilidad_retiro()
        return constructor.obtener_cuenta()

    """ crear cuenta de ahorro reutiliza los campos del metodo construir cuenta y personaliza los campos
        para la cuenta de ahorro """
    def crear_cuenta_ahorro(self, constructor: Constructor):
        return self.construir_cuenta(constructor=constructor,
                                     cuenta="Ahorro", debito=True,
                                     seguridad="V1")

    """ crear cuenta corriente reutiliza los campos del metodo construir cuenta y personaliza los campos
            para la cuenta corriente """
    def crear_cuenta_corriente(self, constructor: Constructor,
                                    limite: float = 25000.00,
                                    tarjeta_credito: bool = False,
                                    tarjeta_debito: bool = True,
                                    libreta: bool = True,
                                    chequera: bool = True,
    ) -> Cuenta:
        return self.construir_cuenta(constructor= constructor,
                                     cuenta= "Corriente",
                                     limite_deuda= limite,
                                     seguridad= "V2",
                                     credito= tarjeta_credito,
                                     debito= tarjeta_debito,
                                     chequera= chequera,
                                     libreta= libreta)

""" Condición que permite la ejecución de la aplicación """
if __name__ == "__main__":
    director = Director()

    cuenta_a = director.crear_cuenta_ahorro(Constructor())
    print(cuenta_a.elementos_habilitados, end='\n\n')
    cuenta_b = director.crear_cuenta_corriente(Constructor())
    print(cuenta_b.elementos_habilitados)
