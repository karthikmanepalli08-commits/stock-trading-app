import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def lstm_predict(data):
    prices = data['Close'].values.reshape(-1, 1)

    # Normalize
    prices = prices / prices.max()

    X, y = [], []

    for i in range(10, len(prices)):
        X.append(prices[i-10:i])
        y.append(prices[i])

    X, y = np.array(X), np.array(y)

    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))

    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=2, batch_size=32, verbose=0)

    pred = model.predict(X[-1].reshape(1,10,1))
    return float(pred[0][0] * data['Close'].max())
