import numpy as np
from models.base_model import BaseModel

class ReactionDiffusionModel(BaseModel):
    """Modelo Gray-Scott de Reação-Difusão (1D simplificado)"""
    
    @staticmethod
    def equations(t, y, Du, Dv, F, k, n_points):
        """Equações do modelo de reação-difusão"""
        n = n_points
        u = y[:n]
        v = y[n:]
        
        # Laplaciano (diferenças finitas com condições de contorno periódicas)
        laplacian_u = np.zeros_like(u)
        laplacian_v = np.zeros_like(v)
        
        dx = 1.0 / (n - 1)
        
        # Centro
        laplacian_u[1:-1] = (u[:-2] - 2*u[1:-1] + u[2:]) / (dx**2)
        laplacian_v[1:-1] = (v[:-2] - 2*v[1:-1] + v[2:]) / (dx**2)
        
        # Condições de contorno periódicas
        laplacian_u[0] = (u[-1] - 2*u[0] + u[1]) / (dx**2)
        laplacian_u[-1] = (u[-2] - 2*u[-1] + u[0]) / (dx**2)
        laplacian_v[0] = (v[-1] - 2*v[0] + v[1]) / (dx**2)
        laplacian_v[-1] = (v[-2] - 2*v[-1] + v[0]) / (dx**2)
        
        # Termos de reação
        uvv = u * v * v
        
        dudt = Du * laplacian_u - uvv + F * (1 - u)
        dvdt = Dv * laplacian_v + uvv - (F + k) * v
        
        return np.concatenate([dudt, dvdt])
    
    @classmethod
    def get_parameters(cls):
        """Parâmetros padrão do modelo"""
        return {
            'Du': 0.16,     # Coeficiente de difusão de u
            'Dv': 0.08,     # Coeficiente de difusão de v
            'F': 0.035,     # Taxa de alimentação
            'k': 0.065,     # Taxa de morte
            'n_points': 50  # Número de pontos espaciais
        }
    
    @classmethod
    def get_initial_conditions(cls, params):
        """Condições iniciais para o modelo"""
        n = params['n_points']
        u0 = np.ones(n)
        v0 = np.zeros(n)
        
        # Perturbação inicial no centro
        center = n // 2
        u0[center-2:center+3] = 0.5
        v0[center-2:center+3] = 0.25
        
        return np.concatenate([u0, v0])
    
    @classmethod
    def get_arguments(cls, params):
        """Extrai argumentos para as equações dos parâmetros"""
        return (params['Du'], params['Dv'], params['F'], params['k'], params['n_points'])
    
    @classmethod
    def get_info(cls):
        """Informações sobre o modelo"""
        return {
            'name': '🎨 Reação-Difusão (Gray-Scott)',
            'description': 'Modelo de formação de padrões em sistemas químicos',
            'equations': [
                '∂u/∂t = Du∇²u - uv² + F(1-u)',
                '∂v/∂t = Dv∇²v + uv² - (F+k)v'
            ],
            'parameters': {
                'Du': 'Coeficiente de difusão da espécie u',
                'Dv': 'Coeficiente de difusão da espécie v',
                'F': 'Taxa de alimentação',
                'k': 'Taxa de morte',
                'n_points': 'Resolução espacial do modelo'
            }
        }