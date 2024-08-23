
import pandas as pd
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import h5py

path = r'D:\Datasets\Electricity'

raw_data = pd.read_csv(f'{path}/solar_gen.csv', dtype = float)

avg_window_length = 30 # minutes

data = raw_data.to_numpy()
data = sliding_window_view(data, avg_window_length, axis = 0)
data = np.average(data, axis = 2)

#------------------------------------------------------------
def data_maker(raw_data, lookback, lookfwrd):

    datum = sliding_window_view(raw_data, lookback + lookfwrd, axis = 0)
    features = datum[:, :, :lookback]
    target = datum[:, 0, lookback:]

    return features, target
#------------------------------------------------------------

lookback_length = 96
lookfwrd_length = 96

features, target = data_maker(data, lookback_length, lookfwrd_length)

print(np.isnan(features).any())
print(np.isnan(target).any())

with h5py.File(f'{path}/electric_data.hdf5', 'w') as f: 

    f.create_dataset('features', data = features)
    f.create_dataset('target', data = target)
