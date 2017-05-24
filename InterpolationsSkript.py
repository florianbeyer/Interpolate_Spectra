#### Florian Beyers script to interpolate (linear) between reflectance values
### with Python 2.7
## 2017-05-17
# mail@flobeyer.tk

## package import
import os
import pandas as pd
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt

## working directories
load_path = 'C:/Users/LenoFlo/Google Drive/A001_BERUFLICH/20170517_Daniel/'
save_path = 'C:/Users/LenoFlo/Google Drive/A001_BERUFLICH/20170517_Daniel/'

# read all files in a directory
onlyfiles = [f for f in listdir(load_path) if isfile(join(load_path, f))]
del(f)

## read one file as pandas dataframe
## ATTENTION!!! Hard Coding: onlyfiles[1]
temp = pd.read_csv(os.path.join(load_path, onlyfiles[1]), sep = ';', header=0)

## convert pandas dataframe to numpy arrays
npMatrix = temp.as_matrix()
wl = np.array(npMatrix[:,0]) # wl = wavelength
ref = np.array(npMatrix[:,1]) # ref = reflectance values

## define wavelength steps
xval = np.linspace(wl[0],wl[-1],(wl[-1]-wl[0]))

## interpolate y values
ref_interpol = np.interp(xval,wl,ref)

## plot the results
plt.plot(wl, ref, 'o')
plt.plot(xval, ref_interpol, '-x')
plt.show()

## convert results to pandas dataframe
temp = {
        'WL':xval,
        'R':ref_interpol}
spectrum_new = pd.DataFrame(data = temp)
spectrum_new.set_index('WL', inplace = True)

## save data as csv seperated with ";"
file_name = 'interpolated_spectrum.csv'
spectrum_new.to_csv(join(save_path + file_name), sep=';')

