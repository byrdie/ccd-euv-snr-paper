"""
Create the figures used in the article.
"""

from ._absorbance import absorbance
from ._qe_effective import qe_effective
from ._probability_measurement import probability_measurement
from ._fano_factor import fano_factor

__all__ = [
    "qe_effective",
    "probability_measurement",
    "noise_discretization",
]
