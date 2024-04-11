SEP005 <- FAST io
-----------------------

Basic package to import data generated by FAST.out files compliant with
SDyPy format for timeseries as proposed in SEP005.

Using the package
------------------

```
from sep005_io_fast import read_fast_file

file_path = # Path to the FAST.out file of interest
signals = read_fast_file(file_path)

Acknowledgements
----------------
This package was developed in the framework of the
[Belfloat project](https://www.owi-lab.be/bel-float)