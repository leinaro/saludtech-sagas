from cliente.seedwork.aplicacion.queries import Query, QueryHandler, ResultadoQuery
import uuid
from dominio.repositorios import DataRepository

class GetDataByIdQuery(Query):
    
    def __init__(self, data_id: str):
        self.data_id = data_id

class GetDataByPartnerIdQuery(Query):
    
    def __init__(self, partner_id: str):
        self.partner_id = partner_id

class GetAllDataQuery(Query):
    pass

class GetDataByPartnerIdQueryHandler(QueryHandler):
    
    def __init__(self, repository: DataRepository):
        self.repository = repository
    
    def handle(self, query: GetDataByPartnerIdQuery):
        return self.repository.get_by_partner_id(query.partner_id)

class GetAllDataQueryHandler(QueryHandler):
    
    def __init__(self, repository: DataRepository):
        self.repository = repository
    
    def handle(self, query: GetAllDataQuery):
        return self.repository.get_all() 