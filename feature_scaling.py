import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

data = [[25,30000],
        [35,60000]]

scaled = scaler.fit_transform(data)

print(scaled)
