"""Tests for functions that calculate plasma parameters using cython."""

import numpy as np
import pytest
from astropy import units as u

from plasmapy.physics.exceptions import PhysicsError

from plasmapy.physics.parameters_cython import (thermal_speed,
                                 )
def test_thermal_speed():
    r"""Test for cythonized version of thermal_speed()."""
    trueVal = 593083.619464999
    T = 11604
    methodVal = thermal_speed(T, particle="e", method="most_probable")
    testTrue = np.isclose(methodVal,
                          trueVal,
                          rtol=0.0,
                          atol=1e-16)
    exceptStr = f'Thermal speed value is {methodVal}, should be {trueVal}.'
    assert testTrue, exceptStr
