import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from ingest_data.seedwork.infraestructura import utils
from ingest_data.modulos.aplicacion.comandos.iniciar_ingestacion import ComandoIniciarIngestacion, ejecutar_comando_iniciar_ingestacion
from ingest_data.modulos.aplicacion.comandos.ingestar_dato import ComandoIngestarDato, ejecutar_comando_ingestar_dato
from ingest_data.modulos.aplicacion.comandos.cancelar_ingestacion import ComandoCancelarIngestacion, ejecutar_comando_cancelar_ingestacion


async def suscribirse_a_topico(topico: str, suscripcion: str, schema: Record, tipo_consumidor:_pulsar.ConsumerType=_pulsar.ConsumerType.Shared):
    try:
        async with aiopulsar.connect(f'pulsar://{utils.broker_host()}:6650') as cliente:
            async with cliente.subscribe(
                topico, 
                consumer_type=tipo_consumidor,
                subscription_name=suscripcion, 
                schema=AvroSchema(schema)
            ) as consumidor:
                while True:
                    mensaje = await consumidor.receive()
                    print(mensaje)
                    datos = mensaje.value()
                    print(f'Evento recibido: {datos.data}')

                    match datos.type:
                        case "IniciarIngestacion":
                            ejecutar_comando_iniciar_ingestacion(
                                ComandoIniciarIngestacion(
                                    datos.data.id,
                                    datos.data.fuente,
                                    datos.data.fecha_inicio_ingestacion
                                )
                            )
                        case "IngestarDato":
                            ejecutar_comando_ingestar_dato(
                                ComandoIngestarDato(
                                    datos.data.id,
                                    datos.data.fuente,
                                    datos.data.contenido,
                                    datos.data.fecha_ingestacion
                                )
                            )
                        case "CancelarIngestacion":
                            ejecutar_comando_cancelar_ingestacion(
                                ComandoCancelarIngestacion(
                                    datos.data.id,
                                    datos.data.fecha_cancelacion
                                )
                            )

                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc() 