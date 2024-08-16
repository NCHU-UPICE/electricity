
import pandas as pd
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
import h5py

path = r'D:\Datasets\Electricity'

raw_all_data = pd.read_csv(f'{path}/all_elec_data.csv')
raw_data = pd.read_csv(f'{path}/elec_data.csv')
raw_data_pred = pd.read_csv(f'{path}/elec_data_pred.csv')

all_data = raw_all_data.to_numpy()
all_data = sliding_window_view(all_data, 60, axis = 0)
all_data = np.average(all_data, axis = 2)

data = raw_data.to_numpy()
data = sliding_window_view(data, 60, axis = 0)
data = np.average(data, axis = 2)

data_pred = raw_data_pred.to_numpy()
data_pred = sliding_window_view(data_pred, 60, axis = 0)
data_pred = np.average(data_pred, axis = 2)

#------------------------------------------------------------
def data_maker(raw_data, window):

    datum = sliding_window_view(raw_data, window + 1, axis = 0)
    features = datum[:, :, :window]
    targets = datum[:, 0, -1]

    # features = np.transpose(features, (0, 2, 1))
    features = np.transpose(features[np.newaxis], (1, 0, 2, 3))
    # print(features.shape)
    targets = np.transpose(targets[np.newaxis], (1, 0))

    return features, targets
#------------------------------------------------------------

all_data_1, all_target_1 = data_maker(all_data, 32)
all_data_2, all_target_2 = data_maker(all_data, 64)

data_1, target_1 = data_maker(data, 32)
data_2, target_2 = data_maker(data, 64)

data_pred_1, target_pred_1 = data_maker(data_pred, 32)
data_pred_2, target_pred_2 = data_maker(data_pred, 64)

with h5py.File(f'{path}/electric_data.hdf5', 'w') as f: 

    f.create_dataset('all_data_32', data = all_data_1)
    f.create_dataset('all_target_32', data = all_target_1)

    f.create_dataset('all_data_64', data = all_data_2)
    f.create_dataset('all_target_64', data = all_target_2)

    f.create_dataset('data_32', data = data_1)
    f.create_dataset('target_32', data = target_1)

    f.create_dataset('data_64', data = data_2)
    f.create_dataset('target_64', data = target_2)

    f.create_dataset('data_pred_32', data = data_pred_1)
    f.create_dataset('target_pred_32', data = target_pred_1)

    f.create_dataset('data_pred_64', data = data_pred_2)
    f.create_dataset('target_pred_64', data = target_pred_2)
