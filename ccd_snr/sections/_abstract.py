import aastex

__all__ = [
    "abstract",
]


def abstract() -> aastex.Abstract:
    result = aastex.Abstract()
    result.append(
        r"""
Silicon-based imaging sensors are a critical component for solar \UV\ astronomy.
Their high sensitivity and low noise are important for making solar
\UV\ telescopes practical to build.
However, \UV\ light is unique compared to other components of the
electromagnetic spectrum since it has both a shallow penetration depth
into the silicon substrate, and liberates more than one electron per
photon.
This means that the electrons have both a moderate chance of recombination
and are numerous enough to cause a measurable deviation from Poisson 
statistics.
In this article, we will use a simple, piecewise-linear expression for the 
differential \CCE\ introduced by \citet{Stern1994} to show that recombination of
\textit{all} of the photoelectrons associated with one photon is a significant
factor in the noise measured by the sensor.
We will both derive an analytic expression for the measured electron distribution
as a function of wavelength and introduce an easy-to-implement algorithm which
can draw samples from this distribution, valid from about 1-1000 nm.
Finally, we will apply this model to the \IRIS\ instrument and estimate the
\SNR\ of the \FUV\ spectrograph channel.
\acresetall
"""
    )
    return result
