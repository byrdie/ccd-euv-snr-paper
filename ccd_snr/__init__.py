"""
Create the figures and compile the LaTeX files for this article.
"""

from ._wavelength import wavelength, energy
from ._ccd import ccd, ccd_aia
from ._acronyms import acronyms
from ._variables import variables
from ._authors import authors
from . import figures
from . import tables
from . import sections
from ._document import document, pdf

__all__ = [
    "wavelength",
    "energy",
    "ccd",
    "ccd_aia",
    "acronyms",
    "variables",
    "authors",
    "figures",
    "tables",
    "sections",
    "document",
    "pdf",
]
