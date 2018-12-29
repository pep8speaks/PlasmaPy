"""
Create a dictionary containing basic information for isotopes and
neutrons.
"""

import astropy.units as u
import json
import os

with open(os.path.join(os.path.dirname(__file__), "isotopes.json")) as f:
    _Isotopes = json.load(f)

for isotope in _Isotopes:
    _Isotopes[isotope]["mass"] *= u.u
    if "half-life" in _Isotopes[isotope] and not isinstance(
            _Isotopes[isotope]["half-life"], str):
        _Isotopes[isotope]["half-life"] *= u.s
