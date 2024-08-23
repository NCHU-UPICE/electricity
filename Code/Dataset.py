
import torch
from torch.utils.data import Dataset
from h5py import File

path = r'D:\Datasets\Electricity'

class Electricity(Dataset):
    def __init__(self):

        self.file_path = f'{path}/electric_data.hdf5'

        with File(self.file_path, 'r') as file:
            self.dataset_len = len(file[f'target'])

    def __len__(self):
        return self.dataset_len

    def __getitem__(self, idx):

        x = torch.from_numpy(File(self.file_path, 'r')[f'features'][idx]).float()
        y = torch.from_numpy(File(self.file_path, 'r')[f'target'][idx]).float()

        return x, y
    
