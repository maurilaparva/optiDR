import torch.nn as nn
from torchvision.models import efficientnet_b7, EfficientNet_B7_Weights

def initialize_model(num_classes, device):
    weights = EfficientNet_B7_Weights.DEFAULT
    model = efficientnet_b7(weights=weights)
    model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    return model.to(device)
