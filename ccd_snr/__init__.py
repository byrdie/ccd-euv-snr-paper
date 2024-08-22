"""
Create the figures and compile the LaTeX files for this article.
"""

from ._wavelength import wavelength
from ._ccd import ccd
from ._acronyms import acronyms
from ._variables import variables
from ._authors import authors
from . import figures
from . import sections
from ._document import document, pdf

__all__ = [
    "wavelength",
    "ccd",
    "acronyms",
    "variables",
    "authors",
    "figures",
    "sections",
    "document",
    "pdf",
]
