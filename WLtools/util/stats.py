__author__ = 'william'

import numpy as np


def std_weighted(a, weights):
    """
    Caluclates the weighted standard deviation.

    Parameters
    ----------
    a : array_like
        Calculate the standard deviation of these values.

    weights : array_like
        An array of weights associated with the values in `a`. Each value in
        `a` contributes to the average according to its associated weight. The weights array must have the same shape
        as `a`.

    Returns
    -------
    standard_deviation : ndarray
         A new array containing the weighted standard deviation.

    References
    ----------

    .. [1] http://en.wikipedia.org/wiki/Standard_deviation#Weighted_calculation
    """
    n = np.sum(weights > 0)
    return np.sqrt(n * np.sum(weights * (a - np.average(a, weights=weights))) / ((n - 1) * np.sum(weights)))


