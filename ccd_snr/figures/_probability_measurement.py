import matplotlib.pyplot as plt
import astropy.units as u
import named_arrays as na
import optika
import aastex
import ccd_snr

__all__ = [
    "probability_measurement",
]


def probability_measurement() -> aastex.Figure:

    wavelength = ccd_snr.wavelength()

    ccd = ccd_snr.ccd()

    iqy = ccd.quantum_yield_ideal(wavelength)
    iqy = iqy.to(u.electron / u.photon).value

    cce = ccd.charge_collection_efficiency(
        rays=optika.rays.RayVectorArray(
            wavelength=wavelength,
            direction=na.Cartesian3dVectorArray(0, 0, 1),
        ),
        normal=na.Cartesian3dVectorArray(0, 0, -1),
    )

    p_r = (1 - cce) ** iqy
    p_m = 1 - p_r

    fig, ax = plt.subplots(
        figsize=(aastex.column_width_inches, 2.5),
        constrained_layout=True,
    )
    na.plt.plot(
        wavelength,
        cce,
        ax=ax,
        label=r"$\mathrm{CCE}(\lambda)$",
    )
    na.plt.plot(
        wavelength,
        p_m,
        ax=ax,
        label=r"$P_\mathrm{m}(\lambda)$",
    )
    ax.set_xscale("log")
    ax.set_xlabel(f"wavelength ({wavelength.unit:latex_inline})")
    ax.set_ylabel("probability")
    ax.legend()

    result = aastex.Figure("probability")
    result.append(aastex.NoEscape(r"\vspace{5pt}"))
    result.add_fig(fig, width=None)

    result.add_caption(
        aastex.NoEscape(
            r"""
The probability of measuring a photon vs. wavelength for the \AIA\ \CCDs.
Plotted for comparison is the \CCE\ for the \AIA\ \CCDs.
"""
        )
    )

    return result
