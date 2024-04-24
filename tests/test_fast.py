# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:24:32 2024

@author: AA000139
"""

from pathlib import Path

import pytest
from sdypy_sep005.sep005 import assert_sep005

from sep005_io_fast import read_fast_file


@pytest.fixture(scope="module")
def file_path():
    filename = "5MW_OC4Semi_H2.5_T10_WS13.out"
    pathname = Path(__file__).resolve().parent
    return pathname / filename  # Path to the FAST.out file of interest


def test_read_fast(file_path):
    signals = read_fast_file(file_path)
    assert assert_sep005(signals) is None
