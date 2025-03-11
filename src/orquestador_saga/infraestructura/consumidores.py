import logging
import traceback
from orquestador_saga.aplicacion.coordinadores.saga_ingesta_datos import oir_mensaje
from orquestador_saga.dominio.eventos.processed_data import EventoProcesamientoDatosFinalizado
from orquestador_saga.dominio.eventos.validacion import EventoValidacionFinalizada, EventoValidacionFallido
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from orquestador_saga.seedwork.infraestructura import utils
#from orquestador_saga.dominio.eventos.ingesta_data import EventoCargaFinalizada
#from orquestador_saga.aplicacion.comandos.ingesta_datos import ComandoIniciarProcesamientoDatos, ejecutar_comando_iniciar_procesamiento_datos

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
                    print(f'*************************************** ')
                    print(f'*** Payload: {str(datos)}')


                    match datos.datacontenttype:
                        case "EventoProcesamientoDatosFinalizado": #EventoProcesamientoDatosFinalizado - EventoProcesamientoDatosFinalizado
                            oir_mensaje(EventoProcesamientoDatosFinalizado(
                                datos.procesamiento_datos_finalizado.url_raw_data,
                                datos.procesamiento_datos_finalizado.partner_id,
                                datos.procesamiento_datos_finalizado.user_id
                            ))
                        case "DataValidada":
                            oir_mensaje(EventoValidacionFinalizada(
                                "datos.query_entrenamiento.url_raw_data",
                                "datos.query_entrenamiento.partner_id",
                                "datos.query_entrenamiento.user_id",
                                "datos.query_entrenamiento.path",
                                True#datos.query_entrenamiento.es_valido
                            ))    
            
                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()