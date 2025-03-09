

#from processed_data.modulos.dominio.eventos import ProcesamientoDatosIniciado, ProcesamientoDatosCancelado, DatoProcesadoGuardado
from processed_data.seedwork.aplicacion.handlers import Handler


from processed_data.modulos.infraestructura.v1.eventos import EventoDatoProcesado, DatoProcesadoGuardado, ProcesamientoDatosCancelado, ProcesamientoDatosIniciado, TipoDatos
from processed_data.modulos.infraestructura.v1.comandos import ComandoIniciarProcesamientoDatos, ComandoGuardarDatoProcesado, ComandoCancelarProcesamientoDatos, ProcesarDatos, GuardarDatoProcesado, CancelarProcesamientoDatos
from processed_data.modulos.infraestructura.v1 import TipoDatos
from processed_data.modulos.infraestructura.despachadores import Despachador
from processed_data.seedwork.infraestructura import utils


class HandlerProcesarDatosIntegracion(Handler):

    @staticmethod
    def handle_procesamiento_datos_iniciado(evento):
        despachador = Despachador()
        print("--------------------------")
        print(str(evento))
        print("--------------------------")
        payload = ProcesamientoDatosIniciado(
           # id = "1232321321", 
            partner_id = "1234567890",
            user_id = "0987654321",
            url_raw_data = "qwertyuio",
            #tipo_processed_data = TipoDatos.imagen_medica,
            fecha_inicio = utils.time_millis())

        evento = EventoDatoProcesado(
            time=utils.time_millis(),
            ingestion=utils.time_millis(),
            datacontenttype=ProcesamientoDatosIniciado.__name__,
            procesamiento_datos_iniciado = payload
        )
        despachador = Despachador()
        despachador.publicar_evento(evento, 'evento-procesar-datos')

#        despachador.publicar_mensaje(evento, "evento-procesar-datos")
        return {"status": "ok"}

    """@staticmethod
    def handle_reserva_cancelada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_reserva_aprobada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')

    @staticmethod
    def handle_reserva_pagada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-reserva')
        

    """