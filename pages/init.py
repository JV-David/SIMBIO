# Exporta todas as páginas
from .simulation import show as show_simulation
from .sensitivity import show as show_sensitivity
from .comparison import show as show_comparison
from .calibration import show as show_calibration
from .library import show as show_library

__all__ = [
    'show_simulation',
    'show_sensitivity',
    'show_comparison',
    'show_calibration',
    'show_library'
]