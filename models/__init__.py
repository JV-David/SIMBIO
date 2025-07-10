from .sir import SIRModel
from .lotka_volterra import LotkaVolterraModel
from .van_der_pol import VanDerPolModel
from .reaction_diffusion import ReactionDiffusionModel

MODEL_CLASSES = {
    "SIR": SIRModel,
    "Lotka-Volterra": LotkaVolterraModel,
    "Van der Pol": VanDerPolModel,
    "Reação-Difusão": ReactionDiffusionModel
}

def get_model_class(model_name):
    """Obtém a classe do modelo pelo nome"""
    return MODEL_CLASSES.get(model_name)

def get_model_classes():
    """Retorna o dicionário com todas as classes de modelos"""
    return MODEL_CLASSES

def get_model_info(model_name):
    """Obtém as informações de um modelo específico"""
    model_class = get_model_class(model_name)
    return model_class.get_info() if model_class else None

__all__ = ['get_model_class', 'get_model_classes', 'get_model_info']