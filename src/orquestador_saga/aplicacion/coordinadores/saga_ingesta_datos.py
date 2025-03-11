#from orquestador_saga.aplicacion.comandos.ingesta_datos import ComandoCancelarCarga, ComandoIniciarCargarDatos
#from orquestador_saga.aplicacion.comandos.query_entrenamiento import ComandoCancelarQueryEntrenamiento, ComandoIniciarQueryEntrenamiendo

from orquestador_saga.dominio.eventos.ingesta_data import EventoCargaFinalizada, EventoCargaFallida 
from orquestador_saga.dominio.eventos.processed_data import EventoProcesamientoDatosFinalizado, EventoProcesamientoDatosFallido
from orquestador_saga.dominio.eventos.validacion import EventoValidacionFinalizada, EventoValidacionFallido
from orquestador_saga.dominio.eventos.query_entrenamiento import EventoQueryEntrenamiendoFinalizado, EventoQueryEntrenamiendoFallido

from orquestador_saga.infraestructura.v1.comandos import ComandoIniciarCargaDatos, ComandoCancelarCargaDatos, CargarDatos 
from orquestador_saga.infraestructura.v1.comandos import ComandoCancelarProcesamientoDatos, ComandoIniciarProcesamientoDatos, ProcesarDatos
from orquestador_saga.infraestructura.v1.comandos import ComandoIniciarValidacion, ComandoCancelarValidacion, IniciarValidacion 
from orquestador_saga.infraestructura.v1.comandos import ComandoIniciarQueryEntrenamiento, ComandoCancelarQueryEntrenamiento, QueryEntrenamiento 

"""from orquestador_saga.infraestructura.v1.eventos import EventoCargaFinalizada, EventoCargaFallida
from orquestador_saga.infraestructura.v1.eventos import EventoProcesamientoDatosFinalizado, EventoProcesamientoDatosFallido
from orquestador_saga.infraestructura.v1.eventos import EventoValidacionFinalizada, EventoValidacionFallido
from orquestador_saga.infraestructura.v1.eventos import EventoQueryEntrenamiendoFinalizado, EventoQueryEntrenamiendoFallido  
"""

from orquestador_saga.seedwork.aplicacion.sagas import CoordinadorOrquestacion, Transaccion, Inicio, Fin
from orquestador_saga.seedwork.dominio.eventos import EventoDominio
from orquestador_saga.seedwork.infraestructura import utils

import logging


class CoordinadorSaludTech(CoordinadorOrquestacion):

    def inicializar_pasos(self):
        self.pasos = [
            Inicio(index=0),
            Transaccion(index=1, comando=ComandoIniciarCargaDatos, evento=EventoCargaFinalizada, error=EventoCargaFallida, compensacion=ComandoCancelarCargaDatos),
            Transaccion(index=2, comando=ComandoIniciarProcesamientoDatos, evento=EventoProcesamientoDatosFinalizado, error=EventoProcesamientoDatosFallido, compensacion=ComandoCancelarProcesamientoDatos),
            Transaccion(index=3, comando=ComandoIniciarValidacion, evento=EventoValidacionFinalizada, error=EventoValidacionFallido, compensacion=ComandoCancelarValidacion),
            Transaccion(index=4, comando=ComandoIniciarQueryEntrenamiento, evento=EventoQueryEntrenamiendoFinalizado, error=EventoQueryEntrenamiendoFallido, compensacion=ComandoCancelarQueryEntrenamiento),
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
        from orquestador_saga.config.db import db

        if not db:
            logging.error('ERROR: DB del app no puede ser nula')
            return
        
        fabrica_repositorio = FabricaRepositorio()
        #repositorio = fabrica_repositorio.crear_objeto(RepositorioReservas)
        
        #repositorio.agregar(
         #   Reserva(
          #      id=str(self.id_reserva), 
           #     id_cliente=str(self.id_cliente), 
            #    estado=str(self.estado), 
             #   fecha_creacion=self.fecha_creacion, 
              #  fecha_actualizacion=self.fecha_actualizacion))

    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        print("+++++++++++++++ CONSTRUIR COMANDO " + str(tipo_comando.__name__) +" +++++++++++++++")
        print(str(evento)) 
        match tipo_comando.__name__:
            case "ComandoIniciarCargaDatos":
                raise NotImplementedError("Comando no implementado")
            case "ComandoCancelarCargaDatos":
                raise NotImplementedError("Comando no implementado")
            
            
            
            case "ComandoIniciarProcesamientoDatos": 
                payload = ProcesarDatos(
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_s3 = evento.url_s3,
                )

                return ComandoIniciarProcesamientoDatos(
                    time=utils.time_millis(),
                    ingestion=utils.time_millis(),
                    datacontenttype=ProcesarDatos.__name__,
                    data = payload
                )
            case "ComandoCancelarProcesamientoDatos":
                raise NotImplementedError("Comando no implementado")
            
            
            case "ComandoIniciarValidacion": #EventoProcesamientoDatosFinalizado - EventoProcesamientoDatosFinalizado
                payload = IniciarValidacion(
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_s3 = evento.url_s3,
                )

                return ComandoIniciarValidacion(
                    time=utils.time_millis(),
                    ingestion=utils.time_millis(),
                    datacontenttype=IniciarValidacion.__name__,
                    data = payload
                )
                
            case "ComandoCancelarValidacion":
                raise NotImplementedError("Comando no implementado")
            
            
            case "ComandoIniciarQueryEntrenamiento":
                payload = QueryEntrenamiento(
                    url_raw_data = "evento.url_raw_data",
                    partner_id = "evento.partner_id",
                    user_id = "evento.user_id",
                    url_s3 = "evento.url_s3",
                    es_valido = True#evento.es_valido
                )

                return ComandoIniciarQueryEntrenamiento(
                    time=utils.time_millis(),
                    ingestion=utils.time_millis(),
                    datacontenttype=QueryEntrenamiento.__name__,
                    data = payload
                )
            case "ComandoCancelarQueryEntrenamiento":
                raise NotImplementedError("Comando no implementado")

   
            case _:
                print(f"⚠️ Advertencia: No se encontró un comando para {tipo_comando.__name__}")
                return None

        



def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorSaludTech()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es evento de Dominio")
