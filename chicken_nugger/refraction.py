import numpy as np


def snell(theta, n1, n2):
    """
    Computes the refraction angle using Snell's law

    Parameters
    ----------

    theta : float
        Incident angle in radians

    n1, n2 : float
        The reflective index of medium of origin and destination.

    Returns
    -------
    alpha : float
        refraction angle

    Examples
    --------
    A ray entering an air-water boundary at 45 degrees

    >>> snell(np.deg2rad(45), 1.00, 1.33)
    """
    return np.arcsin(n1 / n2 * np.sin(theta))


def refractionary():
    pass
