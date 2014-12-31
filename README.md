dmsdec
======

Python module for converting longitudes/latitudes between Degrees, Minutes, Seconds format and decimal format.

Usage
-----

Import dmsdec module
```python
>>> import dmsdec
```

To convert from Degrees/Minutes/Seconds to Decimal
```python
>>> print(dmsdec.dms2dec(('50 3 58.76N', '5 42 53.1W')))
>>> (50.066322, -5.71475)
```

The conversion function `dms2dec` takes a tuple containing two strings (longitude, latitude) as the argument and returns 
a tuple containing two floats, the converted longitude and latitude.

To convert from Decimal to Degrees/Minutes/Seconds
```python
>>> print(dmsdec.dec2dms((50.06632, -5.71475)))
>>> ('50 3 58.76N', '5 42 53.1W')
```

The conversion function `dec2dms` takes a tuple containing two floats (longitude, latitude) as the argument and returns
a tuple containing two strings, the converted longitude and latitude.
