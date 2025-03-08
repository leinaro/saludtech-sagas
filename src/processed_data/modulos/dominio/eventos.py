
class ProcesamientoDatosIniciado():
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    tipo_processed_data = TipoDatos
    fecha_creacion = Long()

class DatoProcesadoValidado():
    id = String()
    fecha_validacion = Long()

class ProcesamientoDatosCancelado():
    id = String()
    fecha_desactivacion = Long()