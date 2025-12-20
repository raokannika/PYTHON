# program15_polynomial_regression.py

# Polynomial Regression Explanation:

# Polynomial Regression is used when the relationship between
# input (X) and output (y) is non-linear (curved).

# In this example:
# X = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# This follows the equation:
# y = x^2

# A straight line (Linear Regression) cannot fit this data properly.
# So we convert the input features into polynomial features
# (1, x, x^2) using PolynomialFeatures.

# Then Linear Regression is applied on these transformed features.

# Polynomial Regression is commonly used in:
# - Salary vs Experience prediction
# - House price prediction
# - Population growth analysis
# - Any scenario where data shows curved growth


import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([[1], [2], [3], [4]])
y = np.array([1, 4, 9, 16])

# Polynomial transformation
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# Model
model = LinearRegression()
model.fit(X_poly, y)

# Prediction
print("Prediction for x=5:", model.predict(poly.transform([[5]])))
