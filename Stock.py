import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

stock = yf.download("TATASTEEL.NS", start="2026-01-01", end="2026-03-25")

stock = stock[['Close']]

stock['Prediction'] = stock['Close'].shift(-1)

X = np.array(stock[['Close']][:-1])
y = np.array(stock['Prediction'][:-1])

model = LinearRegression()
model.fit(X, y)

last_price = np.array(stock[['Close']].tail(1))
prediction = model.predict(last_price)

print("Next Day Predicted Price:", prediction)

plt.figure(figsize=(10,5))
plt.plot(stock['Close'], label="Actual Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Stock Price Trend")
plt.legend()
plt.show()