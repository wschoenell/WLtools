from __future__ import division

import numpy as np


def gamma_nfw(r, c, r_mpc, factor, dx, dy, r_theta):
    '''
    Calculate NFW profile. Put here the equations???

    Parameters
    ----------
    r : float
        Radius.

    c : float
        Concentration index.

    r_mpc : float
        Radius in Mpc.

    factor : float
        caca

    dx : float
        caca

    dy : float
        caca

    r_theta : float
        caca

    Returns
    -------
    g1: float
        What is g1? Is it a float?

    g2: float
        What is g2? Is it a float?

    References
    ----------
    .. [1] O. McNoleg, "The integration of GIS, remote sensing,
       expert systems and adaptive co-kriging for environmental habitat
       modelling of the Highland Haggis using object-oriented, fuzzy-logic
       and neural-network techniques," Computers & Geosciences, vol. 22,
       pp. 585-588, 1996.
    '''

    x = (r_mpc * c / r)
    x2 = np.power(x, 2)

    y = 200 * r * np.power(c, 2) / (3 * np.log(1 + c) - c / (1 + c))

    g = np.zeros_like(r_mpc)

    # x == 1
    fl = (x == 1)
    g[fl] = factor[fl] * y * ((10 / 3.) + 4 * np.log(1. / 2))

    # x < 1
    fl = (x < 1)
    aux_arctan = np.arctanh(np.sqrt((1 - x[fl]) / (1 + x[fl])))
    g[fl] = factor[fl] * y * (8 * aux_arctan / (x2[fl] * np.sqrt(1 - x2[fl])) + (4 / x2[fl]) * np.log(x[fl] / 2) - 2 / (
        x2[fl] - 1) + 4 * aux_arctan / ((x2[fl] - 1) * np.sqrt(1 - x2[fl])))

    # x > 1
    fl = (x > 1)
    aux_arctan = np.arctan(np.sqrt((x[fl] - 1) / (1 + x[fl])))
    g[fl] = factor[fl] * y * (8 * aux_arctan / (x2[fl] * np.sqrt(x2[fl] - 1)) + (4 / x2[fl]) * np.log(x[fl] / 2) - 2 / (
        x2[fl] - 1) + 4 * aux_arctan / (x2[fl] - 1) ** (3 / 2))

    theta2 = np.power(r_theta, 2)
    g1 = g * (np.power(dy, 2) - np.power(dx, 2)) / theta2
    g2 = g * (-2 * dx * dy) / theta2

    return g1, g2