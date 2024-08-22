import astropy.units as u
import named_arrays as na

__all__ = [
    "wavelength"
]


def wavelength() -> na.ScalarArray:
    """
    The wavelength grid used throughout this article.
    """
    return na.geomspace(10, 10000, axis="wavelength", num=10001) * u.AA
