# Program 10: Decision Tree Classifier
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target

tree = DecisionTreeClassifier()
tree.fit(X, y)

print("Prediction:", tree.predict([X[0]]))