import numpy as np
import optika
import aastex
import ccd_snr

__all__ = [
    "variables",
]


def variables() -> list[aastex.Command]:
    """
    A list of numeric variables used in this article.
    """

    ccd = ccd_snr.ccd()

    return [
        aastex.Variable(
            name="bandgapEnergy",
            value=optika.sensors.energy_bandgap,
        ),
        aastex.Variable(
            name="electronHoleEnergy",
            value=optika.sensors.energy_electron_hole,
        ),
        aastex.Variable(
            name="backsurfaceCCE",
            value=np.round(ccd.cce_backsurface, 3),
        ),
        aastex.Variable(
            name="oxideThickness",
            value=np.round(ccd.thickness_oxide),
        ),
        aastex.Variable(
            name="implantThickness",
            value=np.round(ccd.thickness_implant),
        ),
        aastex.Variable(
            name="substrateThickness",
            value=ccd.thickness_substrate,
        ),
    ]
