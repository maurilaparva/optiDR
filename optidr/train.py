import torch
from tqdm.auto import tqdm

def train_model(model, loss_module, optimizer, train_loader, valid_loader, device, path='efficientnetb7', epochs=20):
    training_losses, validation_losses = [], []
    best_val_loss = float('inf')

    for epoch in range(epochs):
        model.train()
        train_loss = 0
        for inputs, labels in tqdm(train_loader, desc=f"Epoch {epoch+1} [Train]"):
            inputs, labels = inputs.to(device), labels.to(device)
            optimizer.zero_grad()
            loss = loss_module(model(inputs), labels)
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
        training_losses.append(train_loss / len(train_loader))

        model.eval()
        val_loss = 0
        with torch.no_grad():
            for inputs, labels in valid_loader:
                inputs, labels = inputs.to(device), labels.to(device)
                loss = loss_module(model(inputs), labels)
                val_loss += loss.item()
        val_loss /= len(valid_loader)
        validation_losses.append(val_loss)

        print(f"Epoch {epoch+1} - Train Loss: {training_losses[-1]:.4f}, Val Loss: {val_loss:.4f}")
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), f"{path}_best.pth")

    return training_losses, validation_losses
