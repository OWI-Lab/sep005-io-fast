# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:36:37 2024

@author: AA000139
"""

from ashes import read_ashes_file
from sdypy_sep005.sep005 import assert_sep005

# Define file paths or path
filepaths = {
    'Sensor Floater': 'Sensor Floater.txt',
    'Sensor Generator': 'Sensor Generator.txt',
    'Sensor Sea': 'Sensor Sea.txt',
    'Sensor Total load [Hydro]': 'Sensor Total load [Hydro].txt', 
    'Sensor Demanded pitch controller': 'Sensor Demanded pitch controller.txt',
    'Sensor Blade': 'Sensor Blade [Time] [Blade 1].txt',
    'Sensor Mooring line': 'Sensor Mooring line.txt',
    'Sensor Rotor': 'Sensor Rotor.txt',
    'Sensor Node': 'Sensor Node [Node Hub Hub].txt',
    'Sensor Beam element': 'Sensor Beam element [Element 1 Tubular tower].txt'
    }

signals = read_ashes_file(filepaths)
assert_sep005(signals)
