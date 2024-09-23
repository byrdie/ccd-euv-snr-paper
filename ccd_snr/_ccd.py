import functools
import optika
__all__ = [
    "ccd",
    "ccd_aia",
]


@functools.cache
def ccd() -> optika.sensors.E2VCCD97Material:
    return optika.sensors.E2VCCD97Material()


@functools.cache
def ccd_aia() -> optika.sensors.E2VCCDAIAMaterial:
    return optika.sensors.E2VCCDAIAMaterial()
