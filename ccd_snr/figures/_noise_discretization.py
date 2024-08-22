import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import named_arrays as na
import optika
import aastex
import ccd_snr

__all__ = [
    "noise_discretization",
]


def noise_discretization() -> aastex.Figure:

    ccd = ccd_snr.ccd()

    wavelength = ccd_snr.wavelength()

    iqy = optika.sensors.quantum_yield_ideal(wavelength)
    iqy = iqy.to(u.electron / u.photon).value

    a = np.floor(iqy)
    b = np.ceil(iqy)

    q = iqy - a
    p = 1 - q

    variance = np.square(a - iqy) * p + np.square(b - iqy) * q

    fano_discretization = variance / iqy

    electrons_measured = ccd.electrons_measured(
        rays=optika.rays.RayVectorArray(
            intensity=na.broadcast_to(1000 * u.photon, dict(experiment=10000)),
            wavelength=wavelength,
            direction=na.Cartesian3dVectorArray(0, 0, 1),
        ),
        normal=na.Cartesian3dVectorArray(0, 0, -1),
    )

    mean_total = electrons_measured.mean("experiment")
    variance_total = np.var(electrons_measured, axis="experiment")
    fano_total = mean_total / variance_total

    fig, ax = plt.subplots(
        figsize=(aastex.column_width_inches, 2.5),
        constrained_layout=True,
    )
    na.plt.plot(
        wavelength,
        fano_discretization,
        ax=ax,
        label=r"discretization",
    )
    na.plt.plot(
        wavelength,
        fano_total,
        ax=ax,
        label=r"total",
    )
    ax.set_xscale("log")
    ax.set_xlabel(f"wavelength ({wavelength.unit:latex_inline})")
    ax.set_ylabel("Fano factor")
    ax.legend()

    result = aastex.Figure("noise")
    result.add_fig(fig, width=None)
    result.add_caption(
        aastex.NoEscape(
            r"""
The Fano factor associated with electron discretization noise.
"""
        )
    )

    return result
