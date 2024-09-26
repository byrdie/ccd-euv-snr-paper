import aastex


def introduction() -> aastex.Section:
    result = aastex.Section("Introduction")
    result.append(
        r"""
Backilluminated, silicon-based image sensors such as \CCDs\ and \CMOS\ sensors 
are ubiquitous in \UV\ solar astronomy, 
and are currently used in many of NASA's most ambitious solar missions,
such as \AIA\ \citep{Lemen2012} and \IRIS\ \citep{DePontieu2014}.

Despite their popularity,
understanding the \QE\ and  noise statistics of these sensors in the \UV\
is challenging due to the phenomenon of \PCC,
where photoelectrons generated near the back surface of the sensor
(due to the shallow penetration depth of \UV\ photons)
recombine before they can be measured \citep{Janesick2001}.
\PCC\ can be difficult to quantify since it depends on how the back surface
of the sensor was prepared by the manufacturer,
and directly measuring it is complicated by other effects such as transmission
through the illuminated surface and charge diffusion \citep{Janesick2001}.
In this work, we will model \PCC\ using the simple, ad-hoc method described in
\citet{Stern1994} and investigate its effects on the noise measured by a typical
sensor.

Another source of noise which is even less understood than \PCC\ is
Fano noise \citep{Fano1947}, 
the unavoidable variation in the number of electrons measured per photon.
Fano noise is routinely measured in soft X-ray regime \citep{Rodrigues2023},
but has possibly never been measured in the \UV\ despite being predicted to
have significant width \citep{Santos1991} and skew \citep{Fraser1994}
variations as a function of wavelength.
Since the Fano noise in silicon is so small,
this work will use a very simple model of constant Fano noise,
which still exhibits the width variations observed in \citet{Santos1991}
since \UV\ photons produce very few photoelectrons.

We will use these two noise sources along with a simple absorbance calculation
to model a silicon imaging sensor and to develop an analytic
expression for the expected noise measured by this sensor as a function of
the mean signal.
This model will be applied to predict the noise measured by some typical solar
\UV\ instruments,
and we will also compare our results to some unexpected noise measurements in
\IRIS\ \citep{Wulser2018}.
"""
    )
    return result
