from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, Dense

model = Sequential([
    Conv2D(32, (3,3), activation="relu",
           input_shape=(28,28,1)),
    Flatten(),
    Dense(10, activation="softmax")
])

model.summary()