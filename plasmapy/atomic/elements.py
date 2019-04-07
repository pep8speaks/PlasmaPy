"""
Create a dictionary containing basic atomic data
The periodic tabla data is from: http://periodic.lanl.gov/index.shtml

"""

import astropy.units as u
import json
import collections
import pkgutil
_Elements = json.loads(pkgutil.get_data('plasmapy', 'atomic/elements.json'))

for element in _Elements:
    _Elements[element]["mass"] *= u.u
    if "half-life" in _Elements[element] and not isinstance(
            _Elements[element]["half-life"], str):
        _Elements[element]["half-life"] *= u.s

_PeriodicTable = collections.namedtuple(
    "periodic_table", ['group', 'category', 'block', 'period']
)

_atomic_numbers_to_symbols = {
    elemdict['atomic number']: symb for (symb, elemdict) in _Elements.items()
}

_element_names_to_symbols = {
    elemdict['element name']: symb for (symb, elemdict) in _Elements.items()
}
