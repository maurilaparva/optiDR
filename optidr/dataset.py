import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self, image_dir, labels_csv, transform=None):
        self.image_dir = image_dir
        self.labels_df = pd.read_csv(labels_csv)
        self.labels_df['id_code'] = self.labels_df['id_code'].str.lower().str.strip()
        self.transform = transform

    def __len__(self):
        return len(self.labels_df)

    def __getitem__(self, idx):
        image_id = self.labels_df.iloc[idx]['id_code']
        label = self.labels_df.iloc[idx]['diagnosis']
        image_path = os.path.join(self.image_dir, f"{image_id}.png")
        image = Image.open(image_path)
        if self.transform:
            image = self.transform(image)
        return image, label
