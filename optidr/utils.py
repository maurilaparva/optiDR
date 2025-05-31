import matplotlib.pyplot as plt

def plot_learning_curves(training_losses, validation_losses):
    plt.figure(figsize=(10,6))
    plt.plot(training_losses, label='Train', marker='o')
    plt.plot(validation_losses, label='Validation', marker='o')
    plt.xlabel('Epochs'); plt.ylabel('Loss'); plt.title('Loss over Epochs')
    plt.legend(); plt.grid(); plt.show()
