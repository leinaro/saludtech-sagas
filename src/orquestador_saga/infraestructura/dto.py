"""DTOs para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de vuelos

"""
"""
from orquestador_saga.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid


#from sqlalchemy import Column, String, Integer, BigInteger, JSON
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import validates
#from datetime import datetime

#Base = db.declarative_base()

# Tabla intermedia para tener la relación de muchos a muchos entre la tabla reservas e itinerarios
#reservas_logs = db.Table(
#    "reservas_logs",
 #   db.Model.metadata,
 #   db.Column("reserva_id", db.String(40), db.ForeignKey("reservas.id")),
 #   db.Column("odo_orden", db.Integer),
 #   db.Column("segmento_orden", db.Integer),
 #   db.Column("leg_orden", db.Integer),
 #   db.Column("fecha_salida", db.DateTime),
 #   db.Column("fecha_llegada", db.DateTime),
 #   db.Column("origen_codigo", db.String(10)),
 #   db.Column("destino_codigo", db.String(10)),
 #   db.ForeignKeyConstraint(
 #       ["odo_orden", "segmento_orden", "leg_orden", "fecha_salida", "fecha_llegada", "origen_codigo", "destino_codigo"],
 #       ["itinerarios.odo_orden", "itinerarios.segmento_orden", "itinerarios.leg_orden", "itinerarios.fecha_salida", "itinerarios.fecha_llegada", "itinerarios.origen_codigo", "itinerarios.destino_codigo"]
 #   )
#)


Base = declarative_base()

def time_millis():
    return int(datetime.utcnow().timestamp() * 1000)

class Sagalogs(Base):
    __tablename__ = 'sagalogs'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    time = Column(BigInteger, nullable=False)
    ingestion = Column(BigInteger, default=time_millis)
    specversion = Column(String(10), default="v1")
    type = Column(String(50), default="EventoValidacionFinalizada")
    datacontenttype = Column(String(50), nullable=False)
    service_name = Column(String(100), default="validacion.saludtech")
    payload = Column(String(), nullable=True)
"""