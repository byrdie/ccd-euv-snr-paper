import functools
import optika

__all__ = [
    "ccd",
]


@functools.cache
def ccd() -> optika.sensors.E2VCCDAIAMaterial:
    return optika.sensors.E2VCCDAIAMaterial()
