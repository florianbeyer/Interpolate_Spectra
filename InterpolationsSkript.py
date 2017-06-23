''' 
#### Florian Beyers script to interpolate (linear) between reflectance values
### with Python 2.7
## 2017-05-17
# mail@flobeyer.de

   Copyright 2015 Florian Beyer
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
   
       http://www.apache.org/licenses/LICENSE-2.0
       
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 '''
## package import
import os
import pandas as pd
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt

## working directories
load_path = 'C:/path/'
save_path = 'C:/path/'

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

