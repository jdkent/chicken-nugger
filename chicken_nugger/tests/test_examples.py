import numpy as np
from ..refraction import snell


def test_one_plus_one_is_two():
    "Check that one and one are indeed two."
    assert 1 + 1 == 2


def test_perpendicular(): 
    actual = snell(0, 2.0, 3.0)
    expected = 0
    assert actual == expected


def test_air_water():
    n_air = 1
    n_water = 1.33
    actual = snell(np.deg2rad(45), n_air, n_water)
    expected = 0.5605584137424605
    assert actual == expected
