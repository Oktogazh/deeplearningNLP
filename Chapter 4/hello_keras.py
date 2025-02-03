import os

os.environ["KERAS_BACKEND"] = "torch"
import keras

print("Keras version:", keras.__version__)
print("Keras backend:", keras.backend.backend())
print("Demat keras")
