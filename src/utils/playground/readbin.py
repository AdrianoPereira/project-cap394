import numpy as np
from osgeo import gdal
import matplotlib.pylab as plt
import pandas as pd

PATH='./vegetacao.bin'

vegetation = np.fromfile('./vegetacao.bin', dtype='float32')
vegetation = np.reshape(vegetation, (241, 241))
lat = np.array(pd.read_csv('./lat.csv', dtype='float32', header=None))
lon = np.array(pd.read_csv('./lon.csv', dtype='float32', header=None))

print(len(lat))