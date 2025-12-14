# Program 14: Feature scaling
from sklearn.preprocessing import StandardScaler
import numpy as np

X = np.array([[1, 20], [2, 30], [3, 40]])
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
print("Before:\n", X)
print("After Scaling:\n", X_scaled)
