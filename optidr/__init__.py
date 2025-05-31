import torch
from torch.utils.data import DataLoader
from torch import nn, optim
from optidr.dataset import CustomDataset
from optidr.transforms import get_transforms
from optidr.model import initialize_model
from optidr.train import train_model
from optidr.utils import plot_learning_curves

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    transform = get_transforms()

    train_dataset = CustomDataset("data/train_images", "data/train_1.csv", transform)
    val_dataset = CustomDataset("data/val_images", "data/valid.csv", transform)
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=64)

    model = initialize_model(num_classes=5, device=device)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-4)

    train_losses, val_losses = train_model(model, loss_fn, optimizer, train_loader, val_loader, device)
    plot_learning_curves(train_losses, val_losses)

if __name__ == "__main__":
    main()
