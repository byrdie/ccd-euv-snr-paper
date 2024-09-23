import aastex

__all__ = [
    "model",
]

import ccd_snr.figures


def model() -> aastex.Section:
    result = aastex.Section("CCD Model")
    result.append(ccd_snr.figures.qe_effective())
    result.append(ccd_snr.tables.models())
    result.append(
        r"""
In this work, we will model the light-sensitive region of the backilluminated 
sensor as a epitaxial silicon layer with a thickness $D$, which is coated
with a thin oxide layer of thickness $\delta$ to provide a realistic transmission 
coefficient.
The illuminated side of the epitaxial layer is considered to have a \PCC\ region
of width $W$, where some of the generated photoelectrons recombine before being
measured by the sensor.
In Section \ref{subsec:ShotNoise} we will see how partial-charge collection
affects the shot noise measured by an imaging sensor.
"""
    )
    subsection_qe = aastex.Subsection("Quantum Efficiency")
    subsection_qe.append(
        r"""
\QE\ is the average number of photoelectrons measured per photon and is a common 
performance metric for measuring sensor sensitivity.
It is given in \citet{Janesick2001} as
\begin{equation} \label{quantum-efficiency}
    \text{QE}(\lambda) = \frac{N_{e}}{N_\gamma}
                       = A(\lambda) \times \text{IQY}(\lambda) \times \text{CCE}(\lambda),
\end{equation}
where $N_e$ is the number of electrons measured by the sensor for a 
given wavelength $\lambda$,
$N_\gamma$ is the total number of photons incident on the sensor,
$A(\lambda)$ is the fraction of incident energy absorbed by the epitaxial layer, 
$\text{IQY}(\lambda)$ is the ideal \QY, the number of photoelectrons generated 
per absorbed photon,
and $\text{CCE}(\lambda)$ is the charge-collection efficiency, the fraction of 
photoelectrons measured by the sensor.

The absorbance $A(\lambda)$ can be determined from the optical constants, using, 
for example, the popular IMD code \citep{Windt1998}.
For this work, we used our software, \texttt{optika} \citep{optika}, 
which has a convenient Python interface and uses
the transfer matrix method described in \citet{Yeh1988} with the optical constants
from \citet{Palik1997} and \cite{Henke1993} to compute the electric field for
every interface in a multilayer stack.
In \citet{Stern1994}, the authors assume no reflections from the unilluminated
side of the sensor for simplicity.
In this work, we compute the total change in Poynting flux into and out of the 
light-sensitive region of the sensor to determine $A(\lambda)$.
This treatment introduces interference effects for infrared wavelengths, 
which can be seen on the right side of Figure \ref{fig:eqe}.

The ideal \QY\ is given by \citet{Janesick2001} as
\begin{equation}
    \text{IQY}(\lambda) = \begin{cases}
        0, & 0 < \epsilon < E_\text{g} \\
        1, & E_\text{g} < \epsilon < E_\text{eh} \\
        \epsilon / E_\text{eh}, & E_\text{eh} < \epsilon < \infty,
    \end{cases}
\end{equation}
where $\epsilon$ is the energy of an incident photon, 
$E_\text{g} = \bandgapEnergy$ is the bandgap energy of silicon,
and $E_\text{eh} = \electronHoleEnergy$ is the energy required to generate one
electron-hole pair at room temperature.
Surprisingly, despite initial results to the contrary \citep{Fraser1994},
this simple relation is a good approximation across the entire wavelength range
considered \citep{Geist1996,Scholze1998,Fang2019}.

In \citet{Stern1994}, the \CCE\ is expressed in terms of a differential \CCE,
$\eta(z)$, which is the fraction of photoelectrons collected for a photon 
absorbed at a depth $z$ into the epitaxial layer.
The total \CCE\ is then the average differential \CCE\ weighted by 
the probability of absorbing a photon at a depth $z$,
\begin{equation} \label{cce}
    \text{CCE}(\lambda) = \frac{\int_0^\infty \eta(z) \exp(-\alpha z) \, dz}
                               {\int_0^\infty \exp(-\alpha z) \, dz},
\end{equation}
where $\alpha$ is the absorption coefficient of silicon for the given wavelength.

In principle, $\eta(z)$ is a function of the exact implant profile which is
usually impractical to measure, but see \cite{Stern2004} for a case where the
authors did have a measurement of the exact implant profile provided by the
manufacturer.
In \citet{Stern1994}, the authors instead adopt a piecewise-linear approximation of
the differential \CCE,
\begin{equation} \label{differential-cce}
    \eta(z) = \begin{cases}
        \eta_0 + (1 - \eta_0) z / W, & 0 < z < W \\
        1, & W < z < \infty
    \end{cases}
\end{equation}
where $\eta_0$ is the differential \CCE\ at the back surface of the sensor.
Plugging Equation \ref{differential-cce} into Equation \ref{cce} yields an
arithmetic expression for the \CCE,
\begin{equation}
    \text{CCE}(\lambda) = \eta_0 + \left( \frac{1 - \eta_0}{\alpha W} \right)(1 - e^{-\alpha W}),
\end{equation}
which can be used in Equation \ref{quantum-efficiency} to determine the \QE.

In \citet{Stern1994}, the authors define an effective \QE\ as
\begin{equation} \label{eqe}
    \text{EQE}(\lambda) = A(\lambda) \times \text{CCE}(\lambda),
\end{equation}
which is the quantity that is typically measured when calibrating a image sensor
\citep{Stern1994,Stern2004,Boerner2012}.
In Figure \ref{fig:eqe}, we've plotted the measured, effective \QE\ of the
\AIA\ \CCDs, and a fit of Equation \ref{eqe} to the data, which varied $\eta_0$,
$\delta$, and $W$, while holding $D$ constant.
We will use these fit parameters in the remainder of this article as a representative
example.
"""
    )
    result.append(subsection_qe)

    subsection_noise = aastex.Subsection("Noise")
    subsubsection_noise_shot = aastex.Subsubsection("Shot Noise")
    subsubsection_noise_shot.append(ccd_snr.figures.probability_measurement())
    subsubsection_noise_shot.append(
        r"""
\UV\ solar astronomy is often shot-noise limited \citep{Lemen2012, DePontieu2014}.
The shot noise is described by a Poisson distribution with variance, 
$\left< N_{\gamma,\text{m}} \right>$, 
the expectation value of the number of photons measured by the sensor.
A critical point of this study is that $\left< N_{\gamma,\text{m}} \right>$ 
includes every photon for which at least one photoelectron is measured.
        
$\left< N_{\gamma,\text{m}} \right>$ can be expressed as a product of
the fraction of incident energy absorbed by the light-sensitive layer,
the probability that an absorbed photon will result in at least one electron
being measured by the sensor, $P_\text{m}(\lambda)$,
and the total number of incident photons, $N_\gamma$:
\begin{equation}
    \left< N_{\gamma,\text{m}} \right> = N_\gamma A(\lambda) P_\text{m}(\lambda).
\end{equation}
Partial charge collection raises the prospect that a photon absorbed in the 
epitaxial layer might not be detected at all.
The fraction of photons for which all photoelectrons are recombined before being 
measured, $P_\text{r}(\lambda) = 1 - P_\text{m}(\lambda)$, is given by
\begin{equation}
    P_\text{r}(\lambda) = \left[ 1 - \text{CCE}(\lambda) \right]^{\text{IQY}(\lambda)}.
\end{equation}

An example calculation of $P_\text{m}(\lambda)$ for the \AIA\ sensors is plotted 
in Figure~\ref{fig:probability}.
For long wavelengths,
$P_\text{m}(\lambda) \approx \text{CCE}(\lambda)$
since the ideal \QY\ is unity, and for short wavelengths, 
$P_\text{m}(\lambda) \approx 1$ since the ideal \QY\ is large.
However, in \UV\ wavelengths, $P_\text{m}(\lambda)$ is more complicated
and smoothly connects these two extremes. 
"""
    )
    subsection_noise.append(subsubsection_noise_shot)
    subsubsection_noise_fano = aastex.Subsubsection("Fano Noise")
    subsubsection_noise_fano.append(ccd_snr.figures.fano_factor())
    subsubsection_noise_fano.append(
        r"""
The Fano noise for silicon is commonly accepted to have a Fano factor of about 0.1.
This is usually measured with X-rays from $^{55}$Fe sources which have a high \QY.
For \UV\ wavelengths, where the \QY\ is much lower, it becomes impossible
to construct a distribution narrow enough to be consistent with a Fano factor 
that small.
"""
    )

    subsection_noise.append(subsubsection_noise_fano)
    subsubsection_noise_recombination = aastex.Subsubsection("Recombination Noise")
    subsection_noise.append(subsubsection_noise_recombination)
    result.append(subsection_noise)
    return result
