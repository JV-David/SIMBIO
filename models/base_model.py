from abc import ABC, abstractmethod

class BaseModel(ABC):
    @classmethod
    @abstractmethod
    def get_info(cls):
        """Retorna um dicionário com informações sobre o modelo"""
        return {
            'name': 'Nome do Modelo',
            'description': 'Descrição do modelo',
            'equations': [],
            'parameters': {}
        }
    
    @classmethod
    @abstractmethod
    def get_parameters(cls):
        """Retorna os parâmetros padrão do modelo"""
        pass
    
    @staticmethod
    @abstractmethod
    def equations(t, y, *args):
        """Define as equações diferenciais do modelo"""
        pass