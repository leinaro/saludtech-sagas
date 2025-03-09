from pydispatch import dispatcher

from .handlers import HandlerProcesarDatosIntegracion

#from saludtech.modulos.vuelos.dominio.eventos.reservas import ReservaCreada, ReservaCancelada, ReservaAprobada, ReservaPagada
from processed_data.modulos.dominio.eventos import ProcesamientoDatosIniciado

dispatcher.connect(HandlerProcesarDatosIntegracion.handle_procesamiento_datos_iniciado, signal=f'{ProcesamientoDatosIniciado.__name__}Integracion')
#dispatcher.connect(HandlerProcesarDatosIntegracion.handle_reserva_cancelada, signal=f'{ReservaCancelada.__name__}Integracion')
#dispatcher.connect(HandlerProcesarDatosIntegracion.handle_reserva_pagada, signal=f'{ReservaPagada.__name__}Integracion')
#dispatcher.connect(HandlerProcesarDatosIntegracion.handle_reserva_aprobada, signal=f'{ReservaAprobada.__name__}Integracion')