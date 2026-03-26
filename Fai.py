import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

area = np.array([500, 800, 1000, 1200, 1500]).reshape(-1,1)
price = np.array([100, 150, 200, 250, 300])

model = LinearRegression()
model.fit(area, price)

predicted_price = model.predict([[1100]])
print("Predicted Price:", predicted_price)

plt.scatter(area, price, color='blue')
plt.plot(area, model.predict(area), color='red')
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Linear Regression Model")
plt.show()