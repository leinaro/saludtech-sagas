import logging
import traceback
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
                    print(f'Evento recibido++++: {datos}')
                    print(f'Evento recibido++++ type: {datos.type}')
                    print(f'Evento recibido++++ datacontenttype: {datos.datacontenttype}')
                    #print(f'Evento recibido++++ data: {datos.data}')
                    #print(f'Evento recibido++++ tipo_processed_data: {datos.data.tipo_processed_data}')

                    """

                    ejecutar_comando_iniciar_procesamiento_datos(
                        ComandoIniciarProcesamientoDatos(
                            datos.data.partner_id,
                            datos.data.user_id,
                            datos.data.url_raw_data,
                            #datos.data.tipo_processed_data.name
                        )
                    )"""
            
                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()