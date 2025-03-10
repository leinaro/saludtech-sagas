from orquestador_saga.aplicacion.comandos.ingesta_datos import ComandoCancelarCarga, ComandoIniciarCargarDatos
from orquestador_saga.aplicacion.comandos.processed_data import ComandoIniciarProcesamientoDatos, ComandoCancelarProcesamientoDatos
from orquestador_saga.aplicacion.comandos.query_entrenamiento import ComandoCancelarQueryEntrenamiendo, ComandoIniciarQueryEntrenamiendo
#from orquestador_saga.aplicacion.comandos.validacion import ComandoCancelarValidacion, ComandoIniciarValidacion
#from orquestador_saga.dominio.eventos.ingesta_data import EventoCargaFallida

from orquestador_saga.dominio.eventos.processed_data import EventoDatosGuardados, EventoProcesamientoDatosFallido
#from orquestador_saga.infraestructura.v1.eventos import EventoDatosGuardados, EventoProcesamientoDatosFallido

from orquestador_saga.infraestructura.v1.comandos import ComandoIniciarValidacion, ComandoCancelarValidacion, IniciarValidacion, CancelarValidacion
from orquestador_saga.infraestructura.v1.eventos import EventoCargaFinalizada, EventoCargaFallida, EventoValidacionFinalizada, EventoValidacionFallido, EventoQueryEntrenamiendoFinalizado, EventoQueryEntrenamiendoFallido
#from orquestador_saga.dominio.eventos.query_entrenamiento import EventoQueryEntrenamiendoFallido, EventoQueryEntrenamiendoFinalizado
#from orquestador_saga.dominio.eventos.validacion import EventoValidacionFallido, EventoValidacionFinalizada
from orquestador_saga.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from orquestador_saga.seedwork.dominio.eventos import EventoDominio
from orquestador_saga.seedwork.infraestructura import utils
from aeroalpes.modulos.vuelos.infraestructura.dto import Reserva as ReservaDTO


class CoordinadorSaludTech(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=ComandoIniciarCargarDatos, evento=EventoCargaFinalizada, error=EventoCargaFallida, compensacion=ComandoCancelarCarga),
            Transaccion(index=2, comando=ComandoIniciarProcesamientoDatos, evento=EventoDatosGuardados, error=EventoProcesamientoDatosFallido, compensacion=ComandoCancelarProcesamientoDatos),
            Transaccion(index=3, comando=ComandoIniciarValidacion, evento=EventoValidacionFinalizada, error=EventoValidacionFallido, compensacion=ComandoCancelarValidacion),
            Transaccion(index=4, comando=ComandoIniciarQueryEntrenamiendo, evento=EventoQueryEntrenamiendoFinalizado, error=EventoQueryEntrenamiendoFallido, compensacion=ComandoCancelarQueryEntrenamiendo),
            Fin(index=5)
        ]

    def iniciar(self):
        self.persistir_en_saga_log(self.pasos[0])
    
    def terminar(self):
        self.persistir_en_saga_log(self.pasos[-1])

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        print("+++++++++++++++ SAGA LOG +++++++++++++++")
        print(str(mensaje))
        from aeroalpes.config.db import db

        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        repositorio = fabrica_repositorio.crear_objeto(RepositorioReservas)
        
        repositorio.agregar(
            Reserva(
                id=str(self.id_reserva), 
                id_cliente=str(self.id_cliente), 
                estado=str(self.estado), 
                fecha_creacion=self.fecha_creacion, 
                fecha_actualizacion=self.fecha_actualizacion))



    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        # TODO Transforma un evento en la entrada de un comando
        # Por ejemplo si el evento que llega es ReservaCreada y el tipo_comando es PagarReserva
        # Debemos usar los atributos de ReservaCreada para crear el comando PagarReserva
        print("+++++++++++++++ CONSTRUIR COMANDO +++++++++++++++")
        print(str(evento))
        print(str(tipo_comando))
        print(str(tipo_comando.__name__))
         
        match tipo_comando.__name__:
            case "ComandoIniciarValidacion": #EventoDatoProcesado - EventoDatosGuardados
                payload = IniciarValidacion(
                    id = "1232321321", 
                    url = "http://localhost:8000/validar-usuario",
                    fecha_inicio_validacion = utils.time_millis()
                )

                return ComandoIniciarValidacion(
                    time=utils.time_millis(),
                    ingestion=utils.time_millis(),
                    datacontenttype=IniciarValidacion.__name__,
                    data = payload
                )
            case _:
                print(f"⚠️ Advertencia: No se encontró un comando para {tipo_comando.__name__}")
                return None

        



# TODO Agregue un Listener/Handler para que se puedan redireccionar eventos de dominio
def oir_mensaje(mensaje):
    print("******++++ "+str(mensaje))
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorSaludTech()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
