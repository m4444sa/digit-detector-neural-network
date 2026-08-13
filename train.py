from sklearn.datasets import fetch_openml

#load MNIST dataset of handwritten digits

X, y =fetch_openml(
    "mnist_784",
    version=1,
    return_X_y=True,
    as_frame=False

)
print("X shape:", X.shape)
print("y shape:", y.shape)