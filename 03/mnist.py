import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

def plot_imagen(image_data):
    image = image_data.reshape(28, 28)
    plt.figure()
    plt.imshow(image, cmap="binary")
    plt.axis("off")

def muestra_mnist():
    # Enable interactive mode
    plt.ion()
    
    num_images = len(mnist.data)
    for n in range(num_images):
        digito = mnist.data[n]
        plot_imagen(digito)
        plt.title(f"{n}/{num_images} label:{mnist.target[n]}")
        plt.show()
        plt.pause(0.1)  # Micro-pause to allow the figure to update and appear, otherwise it won't be visible
        plt.close()

print("Cargando MNIST desde openml.org")
mnist = fetch_openml('mnist_784', as_frame=False)
print("Dataset cargado")

print(mnist.target)
print("Número de imágenes (y etiquetas) en el dataset:", len(mnist.target))

muestra_mnist()






