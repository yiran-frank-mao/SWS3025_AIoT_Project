import torch
import numpy as np
from torch import Tensor
from torchvision import transforms
import torch.nn.functional as F
from pathlib import Path
import arrow
from PIL import Image
from tqdm import tqdm

default_transform = transforms.Compose([transforms.Resize(256),
                                        transforms.CenterCrop(224),
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                            mean=[0.485, 0.456, 0.406],
                                            std=[0.229, 0.224, 0.225])
                                        ])


class ModeDetector:
    def __init__(self, modeMap=None, modelPath: str = "ml/model.pth", data_path: str = "ml/images",
                 transform=default_transform):
        print("Initializing modeDetector...")
        if modeMap is None:
            modeMap = ["computer", "none", "reading"]
        self.modeMap = modeMap
        self.model = torch.load(modelPath)
        self.transform = transform
        self.data_path = data_path
        self.imageSet = {}
        print("Initializing the image set under ml/images...")
        for item in tqdm(Path(self.data_path).glob('*')):
            if item.is_file():
                self.imageSet[item.name] = self.detect(item, numerical_output=True)

    def detect(self, img_path, numerical_output=False, vector_output=False):
        img = Image.open(img_path)
        input_img = self.transform(img).unsqueeze(0)
        pred_softmax = F.softmax(self.model(input_img), dim=1)
        if vector_output:
            return pred_softmax
        elif numerical_output:
            return pred_softmax.argmax()
        else:
            return self.modeMap[pred_softmax.argmax()]

    def detect_all(self, numerical_output=False):
        pred = []
        for item in Path(self.data_path).glob('*'):
            if item.is_file():
                pred.append(self.detect(item, True).argmax())
        if numerical_output:
            return pred, self.modeMap[np.bincount(pred).argmax()]
        else:
            return self.modeMap[np.bincount(pred).argmax()]

    def detect_new(self):
        for item in Path(self.data_path).glob('*'):
            if item.is_file() and item.name not in self.imageSet:
                self.imageSet[item.name] = self.detect(item, numerical_output=True)

    def get_detection(self):
        return self.modeMap[np.bincount(self.imageSet.values()).argmax()]

    def clear(self):
        max_minutes = 10
        now = arrow.now()
        for item in Path(self.data_path).glob('*'):
            if item.is_file() and arrow.get(item.stat().st_mtime)<now.shift(minutes=-max_minutes):
                del self.imageSet[item.name]
                item.unlink()

    def reset(self):
        self.imageSet = {}
        for item in Path(self.data_path).glob('*'):
            if item.is_file():
                item.unlink()
