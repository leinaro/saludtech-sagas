from enum import Enum

class TipoFuente(str, Enum):
    api_externa = "api_externa"
    archivo = "archivo"
    base_datos = "base_datos"
