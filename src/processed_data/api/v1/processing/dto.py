from pydantic import BaseModel

class ProcesarDatos(BaseModel):
    partner_id: str
    user_id: str
    url_raw_data: str
    #tipo_processed_data: str
