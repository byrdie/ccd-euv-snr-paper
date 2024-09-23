import pylatex
import astropy.units as u
import ccd_snr

__all__ = [
    "models",
]


def models() -> pylatex.Table:

    result = pylatex.Table()
    result._star_latex_name = True

    result.add_caption(pylatex.NoEscape(
        r"""
The sensor model parameters which best fit the measurements in \citet{Boerner2012}
and \citet{Heymes2020}."""
    ))
    result.append(pylatex.Label("table:models"))

    ccd = ccd_snr.ccd()
    ccd_aia = ccd_snr.ccd_aia()

    unit = u.nm
    unit_substrate = u.um

    # with result.create(pylatex.Center()) as centering:
    with result.create(pylatex.Tabular("l|rrrrrr")) as tabular:
        tabular.escape = False
        tabular.add_row([
            "Source",
            rf"$\eta_0$",
            rf"$W$ ({unit:latex_inline})",
            rf"$\delta$ ({unit:latex_inline})",
            rf"$D$ ({unit_substrate:latex_inline})",
            rf"oxide roughness ({unit:latex_inline})",
            rf"substrate roughness ({unit:latex_inline})",
        ])
        tabular.add_hline()
        tabular.add_row([
            "\citet{Boerner2012}",
            f"{ccd_aia.cce_backsurface:0.3f}",
            f"{ccd_aia.thickness_implant.to_value(unit):0.0f}",
            f"{ccd_aia.thickness_oxide.to_value(unit):0.1f}",
            f"{ccd_aia.thickness_substrate.to_value(unit_substrate):0.0f}",
            f"{ccd_aia.roughness_oxide.to_value(unit):0.1f}",
            f"{ccd_aia.roughness_substrate.to_value(unit):0.1f}",
        ])
        tabular.add_row([
            "\citet{Heymes2020}",
            f"{ccd.cce_backsurface:0.3f}",
            f"{ccd.thickness_implant.to_value(unit):0.0f}",
            f"{ccd.thickness_oxide.to_value(unit):0.1f}",
            f"{ccd.thickness_substrate.to_value(unit_substrate):0.0f}",
            f"{ccd.roughness_oxide.to_value(unit):0.1f}",
            f"{ccd.roughness_substrate.to_value(unit):0.1f}",
        ])

    return result
