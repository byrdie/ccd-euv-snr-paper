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
\UV\ telescopes practical.
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
factor in the effective \QE. We will also characterize the noise statistics
implied by this form of the \CCE\ and develop a simple analytic model of the
\SNR\ that can be applied easily to any astronomical instrument.
\acresetall
"""
    )
    return result
