import os

os.environ["KERAS_BACKEND"] = "torch"
import keras
from keras.api.models import Sequential
from keras.api.layers import Dense

model = Sequential()
model.add(Dense(2))
model.add(Dense(1))

# Print model info
print("\nModel Summary:")
model.summary()

print("\nBackend Info:")
print("Keras version:", keras.__version__)
print("Keras backend:", keras.backend.backend())
