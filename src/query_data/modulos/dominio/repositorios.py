from abc import ABC
from cliente.seedwork.dominio.repositorios import Repositorio
from entidades import IngestedData

class DataRepository(Repositorio):
    
    def add(self, data: IngestedData) -> None:
        pass
    
    def update(self, data: IngestedData) -> None:
        pass
    
    def get_by_id(self, data_id: str) -> Optional[IngestedData]:
        pass
    
    def get_all(self) -> List[IngestedData]:
        pass
    
    def get_by_partner_id(self, partner_id: str) -> List[IngestedData]:
        pass
