import matplotlib.pyplot as plt
import named_arrays as na
import optika
import aastex
import ccd_snr

__all__ = [
    "qe_effective",
]


def qe_effective() -> aastex.Figure:
    """
    A figure reproducing Figure 12 of Stern (1994).
    """

    result = aastex.Figure("eqe", position="htb!")

    ccd = ccd_snr.ccd()

    eqe_measured = ccd.quantum_efficiency_measured

    wavelength = ccd_snr.wavelength()

    eqe = ccd.quantum_efficiency_effective(
        rays=optika.rays.RayVectorArray(
            wavelength=wavelength,
            direction=na.Cartesian3dVectorArray(0, 0, 1),
        ),
        normal=na.Cartesian3dVectorArray(0, 0, -1),
    )

    absorbance = ccd.absorbance(
        rays=optika.rays.RayVectorArray(
            wavelength=wavelength,
            direction=na.Cartesian3dVectorArray(0, 0, 1),
        ),
        normal=na.Cartesian3dVectorArray(0, 0, -1),
    )

    fig, ax = plt.subplots(
        figsize=(aastex.column_width_inches, 2.5),
        constrained_layout=True,
    )
    na.plt.scatter(
        eqe_measured.inputs,
        eqe_measured.outputs,
        ax=ax,
        label="EQE measurement",
        s=10,
    )
    na.plt.plot(
        wavelength,
        eqe,
        ax=ax,
        label=r"EQE fit",
        zorder=10,
    )
    na.plt.plot(
        wavelength,
        absorbance.average,
        ax=ax,
        label=r"absorbance model",
        color="red",
        alpha=0.5,
    )

    ax.set_xscale("log")
    ax.set_xlabel(f"wavelength ({wavelength.unit:latex_inline})")
    ax.set_ylabel("incident energy fraction")
    ax.legend()

    result.append(aastex.NoEscape(r"\vspace{5pt}"))
    result.add_fig(fig, width=None)

    result.add_caption(
        aastex.NoEscape(
            r"""
A reproduction of Figure 6 of \citet{Boerner2012} that plots the measured,
effective \QE\ of the \AIA\ \CCDs\ against the \citet{Stern1994} model with
$\eta_0 = \backsurfaceCCE$, 
$\delta = \oxideThickness$,
$W = \implantThickness$,
and $D = \substrateThickness$.
Also plotted is the modeled absorbance of the epitaxial layer associated with
the effective \QE\ fit.
"""
        )
    )

    return result
