from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

age = np.array([12,14,16,17,21]).reshape(-1,1)
height = np.array([160,165,167,173,185])

model = LinearRegression()
model.fit(age,height)

predicted_height = model.predict([[24]])
print("predicted heeight is: ",predicted_height)

plt.scatter(age,height,color='blue')
plt.plot(age,model.predict(age),color='red')
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()

