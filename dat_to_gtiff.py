#!/usr/bin/env python3

'''
Convert the RGI grid to GeoTIFF
'''

import numpy as np
import rasterio
from rasterio.transform import from_origin

infile = '00_rgi60_30-30grid.dat'
outfile = '00_rgi60_30-30grid.tif'
numrows = 360
numcols = 720

# Read file into NumPy array
data = np.int32(np.loadtxt(infile))

print('max = ', np.max(data))
print('min = ', np.min(data))

# Write out as GeoTIFF

# Compute transform
res = 0.5
x = np.linspace(-180.0, 180.0, numcols)
y = np.linspace(-90.0, 90.0, numrows)
res = (x[-1] - x[0]) / numcols
print('res =', res)
transform = from_origin(x[0] - res / 2, y[-1] + res / 2, res, res)

with rasterio.open(outfile, 'w', driver='GTiff',
                   height=data.shape[0], width=data.shape[1], count=1,
                   dtype=rasterio.int32, crs='+proj=latlong',
                   transform=transform) as dst:


    dst.write(data, 1)
    dst.close()
