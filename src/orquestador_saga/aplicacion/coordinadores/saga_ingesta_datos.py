
from orquestador_saga.dominio.eventos.ingesta_data import EventoCargaFinalizada, EventoCargaFallida 
from orquestador_saga.dominio.eventos.processed_data import EventoProcesamientoDatosFinalizado, EventoProcesamientoDatosFallido
from orquestador_saga.dominio.eventos.validacion import EventoValidacionFinalizada, EventoValidacionFallido
from orquestador_saga.dominio.eventos.query_entrenamiento import EventoQueryEntrenamiendoFinalizado, EventoQueryEntrenamiendoFallido

from orquestador_saga.infraestructura.v1.comandos import ComandoIniciarCargaDatos, ComandoCancelarCargaDatos 
from orquestador_saga.infraestructura.v1.comandos import ComandoCancelarProcesamientoDatos, ComandoIniciarProcesamientoDatos
from orquestador_saga.infraestructura.v1.comandos import ComandoIniciarValidacion, ComandoCancelarValidacion 
from orquestador_saga.infraestructura.v1.comandos import ComandoIniciarQueryEntrenamiento, ComandoCancelarQueryEntrenamiento 

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
        print("+++++++++++++++ SAGA LOG "+str(mensaje)+" +++++++++++++++")
        
    def construir_comando(self, evento: EventoDominio, tipo_comando: type):
        print("-------------- CONSTRUIR COMANDO " + str(tipo_comando.__name__) +" --------------")
        print("-------------- CON EVENTO "+str(evento) +" --------------") 
        match tipo_comando.__name__:
            case "ComandoIniciarCargaDatos":
                return ComandoIniciarCargaDatos(
                    traceId = evento.traceId,
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                )
            case "ComandoCancelarCargaDatos":
                return ComandoCancelarCargaDatos(
                    traceId = evento.traceId,
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                )
            
            
            case "ComandoIniciarProcesamientoDatos": 
                return ComandoIniciarProcesamientoDatos(
                    traceId = evento.traceId,
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_s3 = evento.url_s3,
                )
            case "ComandoCancelarProcesamientoDatos":
                return ComandoCancelarProcesamientoDatos(
                    traceId = evento.traceId,
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_s3 = evento.url_s3,
                )
            
            case "ComandoIniciarValidacion": #EventoProcesamientoDatosFinalizado - EventoProcesamientoDatosFinalizado
                return ComandoIniciarValidacion(
                    traceId = evento.traceId,
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_s3 = evento.url_s3,
                    path = evento.path
                )
                
            case "ComandoCancelarValidacion":
                return ComandoCancelarValidacion(
                    traceId = evento.traceId,
                    url_raw_data = evento.url_raw_data,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_s3 = evento.url_s3,
                    path = evento.path
                )
            
            case "ComandoIniciarQueryEntrenamiento":
                return ComandoIniciarQueryEntrenamiento(
                    traceId = evento.traceId,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_raw_data = evento.url_raw_data,
                    url_s3 = evento.url_s3,
                    path = evento.path,
                    es_valido = evento.es_valido
                )
            case "ComandoCancelarQueryEntrenamiento":
                return ComandoCancelarQueryEntrenamiento(
                    traceId = evento.traceId,
                    partner_id = evento.partner_id,
                    user_id = evento.user_id,
                    url_raw_data = evento.url_raw_data,
                    url_s3 = evento.url_s3,
                    path = evento.path,
                    es_valido = evento.es_valido
                )
   
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
