import numpy as np
import named_arrays as na

__all__ = [
    "fano_factor",
]


def fano_factor(
    a: na.AbstractArray,
    axis: None | str | tuple[str],
):
    """
    Compute the Fano factor of a given array along the specified axis.

    Parameters
    ----------
    a
        The array to compute the Fano factor of.
    axis
        The axis along which to compute the Fano factor.

    Returns
    -------

    """
    return np.var(a, axis=axis) / np.mean(a, axis=axis)
