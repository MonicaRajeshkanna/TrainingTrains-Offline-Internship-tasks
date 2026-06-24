from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(32, activation="relu", input_shape=(5,)))

model.add(Dense(16, activation="relu"))

model.add(Dense(1))

model.summary()