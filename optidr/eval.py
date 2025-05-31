import torch
import numpy as np
from torch.nn import Softmax
from sklearn.metrics import roc_curve, auc

def test_model(model, test_loader, device):
    model.eval()
    true_labels, predicted_probs = [], []
    with torch.no_grad():
        for inputs, labels in test_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            probs = Softmax(dim=1)(outputs)[:, 1]  # Binary classification
            predicted_probs.extend(probs.cpu().numpy())
            true_labels.extend(labels.cpu().numpy())
    return np.array(true_labels), np.array(predicted_probs)
