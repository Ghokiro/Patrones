""" PATRÓN PROTOTYPE"""

"""
    Codificar una app relacionada a una cuenta bancaria donde
    las clases se copien en profundidad (deep coopy) 
"""

""" LIBRERÍAS"""
from abc import abstractmethod, ABC
from copy import deepcopy

""" Atributos para las clases """
class Atributos:
    """ Define los atributos base que debe contar una cuenta bancaria"""
    """
        ATRIBUTOS DE LA CLASE:
        - numero cuenta: es el numero de la cuenta del cliente a la que se le transfiere dinero.
        - nombre completo: es el nombre completo del cliente.
        - balance crédito: es el valor adicional al balance el cual es prestado por el banco.
        - balance: es el dinero actual que el cliente posee.
    """
    def __init__(self):
        self.numero_cuenta = "No Asignado"
        self.nombre_completo = "No Asignado"
        self.balance_credito = 0.00
        self.balance = 0.00

""" Clase Principal para las cuentas bancarias """
class Cuenta(ABC):
    """ Esta clase sirve de interfaz y prototipo para las demás clases de cuentas bancarias """
    """
        CONSTRUCTOR:
            - Instancia los atributos de la clase
            
        MÉTODOS GET DE LA CLASE:
            - Numero Cuenta: retorna el numero de la cuenta del cliente.
            - Nombre Completo: Retorna el nombre completo del cliente.
            - Balance Crédito: Retorna el valor del crédito que puede tomar el cliente.
            - Balance: Retorna el saldo actual del cliente.
        
        MÉTODOS SETTER DE LA CLASE:
            - Balance: Recibe un monto de dinero el cual se le sumará al balance actual,
                si recibe un monto negativo, se le restará el saldo actual.
            - Numero: Recibe el número de la cuenta del cliente por única vez.
            - Nombre Completo: Recibe el nombre del cliente por única vez.
        
        MÉTODOS:
                        
            - copy: Permitirá realizar la clonación de las subclases.
            - str: Retornará la información de la cuenta del cliente.
    """

    def __init__(self) -> None:
        self._atributos = Atributos()

    @property
    def numero_cuenta(self) -> str:
        return self._atributos.numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, numero) -> None:
        if self._atributos.numero_cuenta == "No Asignado":
            self._atributos.numero_cuenta = numero

    @property
    def nombre_completo(self) -> str:
        return self._atributos.nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, nombre_completo) -> None:
        if self._atributos.nombre_completo == "No Asignado":
            self._atributos.nombre_completo = nombre_completo

    @property
    def balance_credito(self) -> float:
        return self._atributos.balance_credito

    @property
    def balance(self) -> float:
        return self._atributos.balance

    @balance.setter
    def balance(self, valor: float) -> None:
        self._atributos.balance += valor

    @abstractmethod
    def clonar(self):
        pass

    def __str__(self) -> str:
        info = {"Número de cuenta": self._atributos.numero_cuenta,
                "Cliente": self._atributos.nombre_completo,
                "Balance": "${:,.2f}".format(self._atributos.balance),}

        return f"{info}"

""" Prototipo 1 """
class CuentaDeAhorro(Cuenta):
    """ Permite la creación de cuenta de ahorros para los clientes """
    """ ATRIBUTOS: 
        - limites de transacciones: define el numero de transacciones que el cliente
                puede realizar, quizás por día.
                
        MÉTODO:
            - copy: Realiza una clonación profunda de esta clase.
    """

    def __init__(self) -> None:
        super().__init__()
        self.limites_transacciones = 5

    """ FUNCIÓN REDUCIR INTENTO DE TRANSACCIÓN """

    def reducir_intento_transaccion(self) -> None:
        """ Esta función Reduce el número de intento actual de la cuenta de ahorro cuando
            realiza una transacción """
        if self.limites_transacciones > 0:
            self.limites_transacciones -= 1
        else:
            raise ExcepcionLimiteTransaccion("Limite de intentos de transacciones alcanzados.")

    def clonar(self):
        return deepcopy(self)

class CuentaCorriente(Cuenta):
    """ Permite la creación de cuentas corrientes para los clientes """
    """ ATRIBUTOS: 
        - balance crédito: Se asigna el balance del crédito inicial del cliente.

        MÉTODO:
            - copy: Realiza una clonación profunda de esta clase.
    """
    def __init__(self) -> None:
        super().__init__()
        self._atributos.balance_credito = 25000.00

    def clonar(self):
        return deepcopy(self)

""" CLASE DEPÓSITO """
class Deposito:
    """ Esta clase permite agregar saldo al balance del cliente """
    """
        METODO:
            - DEPOSITAR EFECTIVO: 
                Parametros:
                    * cuenta: Recibe la cuenta del cliente a quien se le depositará.
                    * monto: Es el dinero a depositar.
    """
    @staticmethod
    def depositar(cuenta, monto: float) -> None:
        cuenta.balance = monto

""" CLASE PARA LA TRANSACCIÓN ENTRE CUENTAS """
class Transaccion:
    """ Esta clase permite la transacción de una cuenta a otra """
    """
        MÉTODOS:
            Transferir: Realiza la transferencia de cuenta a cuenta.
                PARAMETROS DE TRANSFERIR:
                    - Emisor: Es la cuenta que envía el dinero.
                    - Receptor: Es la cuenta que recibe el dinero.
                    - Monto: Es el saldo monetario a transferir.
                
            Validador: Método privado que verifica la posibilidad de la transacción
                observando el balance actual del de la cuenta emisora.                
    """
    def transferir(self, emisor, receptor, monto: float) -> None:
        if self.__validador(emisor, monto):
            emisor.balance = -monto
            receptor.balance = monto
            print("Transferencia exitosa!")

    @staticmethod
    def __validador(emisor, monto_a_transferir: float) -> bool:
        if type(emisor) == CuentaDeAhorro:
            emisor.reducir_intento_transaccion()
        credito = emisor.balance_credito
        balance = emisor.balance
        return balance + credito >= monto_a_transferir

""" GESTOR DE PROTOTIPOS DE CUENTAS """
class GestorCuentas:
    """ Esta clase administra el registro de los prototipos de cuentas creados """

    """ ATRIBUTO:
            - cuentas: almacena un diccionario de cuentas registradas.
        
        MÉTODOS:
            - Registrar Cuenta: Registra el prototipo de la cuenta.
                PARAMETROS:
                    - id: identificador clave para el diccionario de prototipos de cuentas.
                    - cuenta: Es el prototipo de la cuenta que se registrará.
                    
            - Obtener Cuenta: Valida la existencia del registro de una cuenta y, si existe,
                    la retorna.
    """
    def __init__(self):
        self.__cuentas: dict = {}

    def registrar_cuenta(self, identificador: str, cuenta):
        self.__cuentas[identificador] = cuenta

    def obtener_cuenta(self, identificador: str):
        if identificador in self.__cuentas:
            return self.__cuentas[identificador]
        else:
            raise TypeError(f"El prototipo de cuenta {identificador} no está registrada.")


""" Excepción de limite de intentos de transacciones ya alcanzados. """
class ExcepcionLimiteTransaccion(Exception):
    pass

""" CONDICIÓN PARA LA EJECUCIÓN DE LA APLICACIÓN """
if __name__ == "__main__":
    gestor = GestorCuentas()

    deposito = Deposito()
    transaccion = Transaccion()

    ahorro = CuentaDeAhorro()
    corriente = CuentaCorriente()

    gestor.registrar_cuenta("A1", ahorro)
    gestor.registrar_cuenta("C1", corriente)


    manuel_corriente: CuentaCorriente = gestor.obtener_cuenta('C1').clonar()

    manuel_corriente.numero_cuenta = "1001"
    manuel_corriente.nombre_completo = "Manuel Antonio Rodriguez"

    deposito.depositar(manuel_corriente, 15000)


    pedro_ahorro: CuentaDeAhorro = gestor.obtener_cuenta('A1').clonar()

    pedro_ahorro.numero_cuenta = "2001"
    pedro_ahorro.nombre_completo = "Pedro Ahorro"

    deposito.depositar(pedro_ahorro, 25000)

    print(manuel_corriente.__str__())
    print()

    print(pedro_ahorro.__str__())
    print()

    transaccion.transferir(pedro_ahorro, manuel_corriente, 100)

    print(manuel_corriente.__str__())
    print()

    print(pedro_ahorro.__str__())
    print()

