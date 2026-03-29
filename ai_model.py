from sklearn.linear_model import LinearRegression
import numpy as np

def predict_price(data):
    data = data.dropna()
    data['Days'] = np.arange(len(data))

    X = data[['Days']]
    y = data['Close']

    model = LinearRegression()
    model.fit(X, y)

    future = np.array([[len(data) + 1]])
    return model.predict(future)[0]
