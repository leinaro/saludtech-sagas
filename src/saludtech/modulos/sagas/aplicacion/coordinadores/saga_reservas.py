from saludtech.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from saludtech.seedwork.aplicacion.comandos import Comando
from saludtech.seedwork.dominio.eventos import EventoDominio

from saludtech.modulos.sagas.aplicacion.comandos.cliente import RegistrarUsuario, ValidarUsuario
from saludtech.modulos.sagas.aplicacion.comandos.pagos import PagarReserva, RevertirPago
from saludtech.modulos.sagas.aplicacion.comandos.gds import ConfirmarReserva, RevertirConfirmacion
from saludtech.modulos.vuelos.aplicacion.comandos.crear_reserva import CrearReserva
from saludtech.modulos.vuelos.aplicacion.comandos.aprobar_reserva import AprobarReserva
from saludtech.modulos.vuelos.aplicacion.comandos.cancelar_reserva import CancelarReserva
from saludtech.modulos.vuelos.dominio.eventos.reservas import ReservaCreada, ReservaCancelada, ReservaAprobada, CreacionReservaFallida, AprobacionReservaFallida
from saludtech.modulos.sagas.dominio.eventos.pagos import ReservaPagada, PagoRevertido
from saludtech.modulos.sagas.dominio.eventos.gds import ReservaGDSConfirmada, ConfirmacionGDSRevertida, ConfirmacionFallida

from processed_data.modulos.aplicacion.comandos.iniciar_procesamiento_datos import ComandoIniciarProcesamientoDatos
from processed_data.modulos.aplicacion.comandos.cancelar_procesamiento_datos import ComandoCancelarProcesamientoDatos
from processed_data.modulos.dominio.eventos import ProcesamientoDatosIniciado, ProcesamientoDatosFallido

class CoordinadorReservas(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=ComandoIniciarProcesamientoDatos, evento=ProcesamientoDatosIniciado, error=ProcesamientoDatosFallido, compensacion=ComandoCancelarProcesamientoDatos),
            Fin(index=2)
            
            #Transaccion(index=1, comando=CrearReserva, evento=ReservaCreada, error=CreacionReservaFallida, compensacion=CancelarReserva),
            #Transaccion(index=2, comando=PagarReserva, evento=ReservaPagada, error=PagoFallido, compensacion=RevertirPago),
            #Transaccion(index=3, comando=ConfirmarReserva, evento=ReservaGDSConfirmada, error=ConfirmacionFallida, compensacion=ConfirmacionGDSRevertida),
            #Transaccion(index=4, comando=AprobarReserva, evento=ReservaAprobada, error=AprobacionReservaFallida, compensacion=CancelarReserva),
            #Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar():
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        ...


# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorReservas()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
