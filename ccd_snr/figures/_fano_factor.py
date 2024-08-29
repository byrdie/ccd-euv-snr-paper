import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import named_arrays as na
import optika
import aastex
import ccd_snr

__all__ = [
    "fano_factor",
]


def _fano_factor(
    a: na.AbstractArray,
    axis: None | str | tuple[str],
):
    return np.var(a, axis=axis) / np.mean(a, axis=axis)


def fano_factor() -> aastex.Figure:

    ccd = ccd_snr.ccd()

    wavelength = ccd_snr.wavelength()

    iqy = ccd.quantum_yield_ideal(wavelength)
    iqy = iqy.to(u.electron / u.photon).value

    rays = optika.rays.RayVectorArray(
        intensity=na.broadcast_to(100 * u.photon, dict(experiment=1000)),
        wavelength=wavelength,
        direction=na.Cartesian3dVectorArray(0, 0, 1),
    )
    normal = na.Cartesian3dVectorArray(0, 0, -1)

    a = np.floor(iqy)
    b = np.ceil(iqy)

    q = iqy - a
    p = 1 - q

    variance = np.square(a - iqy) * p + np.square(b - iqy) * q

    fano_discretization = variance / iqy

    qe = ccd.quantum_efficiency(rays, normal)

    electrons_measured = ccd.electrons_measured(rays, normal)

    photons_measured = electrons_measured / qe
    # photons_measured = electrons_measured / (iqy * cce)

    fano_total = _fano_factor(photons_measured, axis="experiment")

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
