import logging
import traceback
from orquestador_saga.aplicacion.coordinadores.saga_ingesta_datos import oir_mensaje
from orquestador_saga.dominio.eventos.ingesta_data import EventoCargaFallida, EventoCargaFinalizada
from orquestador_saga.dominio.eventos.processed_data import EventoProcesamientoDatosFallido, EventoProcesamientoDatosFinalizado
from orquestador_saga.dominio.eventos.query_entrenamiento import EventoQueryEntrenamiendoFallido, EventoQueryEntrenamiendoFinalizado
from orquestador_saga.dominio.eventos.validacion import EventoValidacionFinalizada, EventoValidacionFallido
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from orquestador_saga.seedwork.infraestructura import utils

async def suscribirse_a_topico(topico: str, suscripcion: str, schema: Record, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared):
    try:
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as processed_data:
            async with processed_data.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
                schema=AvroSchema(schema)
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'*********** Evento recibido *********** ')
                    print(f'*** Tipo {datos.type} - {datos.datacontenttype}')
                    print(f'*** Payload: {str(datos)}')
                    print(f'*************************************** ')


                    match datos.datacontenttype:
                        case "ProcesamientoDatosFinalizado":
                            oir_mensaje(EventoProcesamientoDatosFinalizado(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data,
                                url_s3=datos.data.url_s3,
                                path=datos.data.path
                            ))

                        case "CargaFinalizada":
                            oir_mensaje(EventoCargaFinalizada(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data,
                                url_s3=datos.data.url_s3
                            ))

                        case "ValidacionFinalizada":
                            oir_mensaje(EventoValidacionFinalizada(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data,
                                url_s3=datos.data.url_s3,
                                path=datos.data.path,
                                es_valido=datos.data.es_valido
                            ))

                        case "QueryEntrenamiendoFinalizado":
                            oir_mensaje(EventoQueryEntrenamiendoFinalizado(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data,
                                url_s3=datos.data.url_s3,
                                path=datos.data.path,
                                es_valido=datos.data.es_valido,
                                entrenamiendo_completado=datos.data.entrenamiendo_completado
                            ))

                        case "CargaFallida":
                            oir_mensaje(EventoCargaFallida(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data
                            ))

                        case "ProcesamientoDatosFallido":
                            oir_mensaje(EventoProcesamientoDatosFallido(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data,
                                url_s3=datos.data.url_s3
                            ))

                        case "ValidacionFallida":
                            oir_mensaje(EventoValidacionFallido(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data,
                                url_s3=datos.data.url_s3,
                                path=datos.data.path
                            ))

                        case "QueryEntrenamiendoFallido":
                            oir_mensaje(EventoQueryEntrenamiendoFallido(
                                traceId=datos.data.traceId,
                                partner_id=datos.data.partner_id,
                                user_id=datos.data.user_id,
                                url_raw_data=datos.data.url_raw_data,
                                url_s3=datos.data.url_s3,
                                path=datos.data.path,
                                es_valido=datos.data.es_valido
                            ))

                        case _:
                            # Si no hay una coincidencia, podrías manejarlo aquí, como un caso no esperado
                            print(f"Tipo de evento no reconocido: {datos.datacontenttype}")
  
            
                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()