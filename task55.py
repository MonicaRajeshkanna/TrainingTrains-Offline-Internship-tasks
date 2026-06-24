from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

model = Sequential([
    SimpleRNN(16, input_shape=(5,1)),
    Dense(1)
])

model.summary()