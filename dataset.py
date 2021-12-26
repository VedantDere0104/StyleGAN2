from PIL import Image
import torch

from io import BytesIO
import lmdb


class Dataset(torch.utils.data.Dataset):
    def __init__(self , 
                path , 
                transform , 
                resolution = 256):
        super(Dataset , self).__init__()

        self.env = lmdb.open(
            path , 
            max_readers=32 , 
            readonly=True , 
            lock=False , 
            meminit=False
        )

        if not self.env:
            raise IOError("Cannot open dataset" , path)

        with self.env.begin(write=False) as t:
            self.length = int(t.get('length'.encode('utf-8')).decode('utf-8'))
        self.resolution = resolution
        self.transform = transform

    def __len__(self):
        return self.length
    
    def __getitem__(self , idx):
        with self.env.begin(write=False) as txn:
            key = f'{self.resolution}-{str(idx).zfill(5)}'.encode('utf-8')
            img_bytes = txn.get(key)

        buffer = BytesIO(img_bytes)
        img = Image.open(buffer)
        if self.transform:
            img = self.transform(img)
        return img