# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:24:32 2024

@author: AA000139
"""

from fast import read_fast_file
from sdypy_sep005.sep005 import assert_sep005

file_path = '5MW_OC4Semi_H2.5_T10_WS13.out' # Path to the FAST.out file of interest

signals = read_fast_file(file_path)
assert_sep005(signals)

