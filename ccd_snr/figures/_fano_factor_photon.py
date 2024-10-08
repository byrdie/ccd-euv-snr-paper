import matplotlib.pyplot as plt
import astropy.units as u
import named_arrays as na
import aastex
import ccd_snr

__all__ = [
    "fano_factor_photon",
]


def fano_factor_photon() -> aastex.Figure:

    ccd = ccd_snr.ccd()

    wavelength = ccd_snr.wavelength()
    energy = ccd_snr.energy()

    rays = ccd_snr.simulations.rays()
    normal = ccd_snr.simulations.normal

    absorbance = ccd.absorbance(rays, normal)
    cce = ccd.charge_collection_efficiency(rays, normal)
    qe = ccd.quantum_efficiency(rays, normal)

    photons_measured = ccd_snr.simulations.photons_measured()

    fano_shot = 1 * u.photon
    fano_absorbance = (1 / absorbance.average - 1) * u.photon
    fano_recombination = (1 - cce) * u.electron / qe
    fano_total = fano_shot + fano_absorbance + fano_recombination
    fano_mc = ccd_snr.fano_factor(
        a=photons_measured,
        axis=ccd_snr.simulations.axis_xy,
    )

    fig, ax = plt.subplots(
        figsize=(aastex.column_width_inches, 2.5),
        constrained_layout=True,
    )
    ax2 = ax.twiny()
    ax2.invert_xaxis()
    na.plt.plot(
        wavelength,
        fano_shot,
        ax=ax,
        label="Poisson",
    )
    na.plt.plot(
        wavelength,
        fano_absorbance,
        ax=ax,
        label="absorbance",
    )
    na.plt.plot(
        wavelength,
        fano_recombination,
        ax=ax,
        label="recombination",
    )
    na.plt.plot(
        wavelength,
        fano_total,
        ax=ax,
        label="total",
    )
    na.plt.plot(
        wavelength,
        fano_mc,
        ax=ax,
        label=r"Monte Carlo",
        zorder=0,
    )
    na.plt.plot(
        energy,
        fano_shot,
        ax=ax2,
        linestyle="None",
    )

    ax.set_xscale("log")
    ax2.set_xscale("log")
    ax.set_xlabel(f"wavelength ({wavelength.unit:latex_inline})")
    ax2.set_xlabel(f"energy ({energy.unit:latex_inline})", labelpad=8)
    ax.set_ylabel("variance-to-signal ratio")
    ax.legend(loc="upper left")

    result = aastex.Figure("photon-fano-factor")
    result.add_fig(fig, width=None)
    result.add_caption(
        aastex.NoEscape(
            r"""
The total and component-wise \VSR\ for photons incident on the sensor.
This plot is useful when designing an instrument since it demonstrates the
noise to expect from the sensor for a given spectral radiance.
"""
        )
    )

    return result
