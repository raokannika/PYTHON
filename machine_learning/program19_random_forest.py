from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Random Forest Explanation:

# Random Forest is an ensemble learning algorithm
# that combines multiple decision trees.

# Each tree gives a prediction, and the final output
# is decided by majority voting.

# Advantages:
# - Reduces overfitting
# - High accuracy
# - Works well with large datasets

# Used in:
# - Medical diagnosis
# - Fraud detection
# - Recommendation systems