import functools
import astropy.units as u
import named_arrays as na
import optika
import ccd_snr

__all__ = [
    "axis_x",
    "axis_y",
    "axis_xy",
    "num_x",
    "num_y",
    "photons_expected",
    "normal",
    "rays",
    "electrons_measured",
    "photons_measured",
]

axis_x = "detector_x"
"""The logical axis representing the horizontal dimension of the sensor."""

axis_y = "detector_y"
"""The logical axis representing the vertical dimension of the sensor."""

axis_xy = (axis_x, axis_y)
"""The logical axes representing the horizontal and vertical dimensions of the sensor."""

num_x = 128
"""The number of pixels in the horizontal dimension."""

num_y = 128
"""The number of pixels in the vertical dimension."""

photons_expected = 100 * u.photon
"""The expected number of photons measured by each pixel in the sensor."""

normal = na.Cartesian3dVectorArray(0, 0, -1)
"""The vector perpendicular to the surface of the sensor."""


def rays() -> optika.rays.RayVectorArray:
    """
    The geometric light rays incident on the surface of the sensor.
    """
    intensity = na.broadcast_to(
        array=photons_expected,
        shape={axis_x: num_x, axis_y: num_y},
    )
    return optika.rays.RayVectorArray(
        intensity=intensity,
        wavelength=ccd_snr.wavelength(),
        direction=na.Cartesian3dVectorArray(0, 0, 1),
    )


@functools.cache
def electrons_measured() -> na.ScalarArray:
    """
    The number of electrons measured by each pixel in the simulation.
    """
    ccd = ccd_snr.ccd()
    return ccd.electrons_measured(rays(), normal).intensity


@functools.cache
def photons_measured() -> na.ScalarArray:
    """
    The number of photons measured by each pixel in the simulation.
    """
    ccd = ccd_snr.ccd()
    qe = ccd.quantum_efficiency(rays(), normal)
    return electrons_measured() / qe
