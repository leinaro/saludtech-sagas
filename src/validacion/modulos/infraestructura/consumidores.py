import logging
import traceback
import pulsar, _pulsar
import aiopulsar
import asyncio
from pulsar.schema import *
from validacion.seedwork.infraestructura import utils
from validacion.modulos.aplicacion.comandos.iniciar_validacion import ComandoIniciarValidacion,  ejecutar_comando_iniciar_validacion


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
                        case "IniciarValidacion": #IniciarValidacion-IniciarValidacion
                            ejecutar_comando_iniciar_validacion(
                                ComandoIniciarValidacion(
                                    datos.data.id,
                                    datos.data.url,
                                    datos.data.fecha_inicio_validacion
                                )
                            )

                    await consumidor.acknowledge(mensaje)    

    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()