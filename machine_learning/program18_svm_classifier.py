# program18_svm_classifier.py

from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = SVC(kernel='linear')
model.fit(X_train, y_train)

print("Accuracy:", model.score(X_test, y_test))

# Support Vector Machine (SVM) Explanation:

# SVM is a supervised learning algorithm used for
# classification and regression.

# It works by finding the BEST possible boundary
# (hyperplane) that separates different classes
# with maximum margin.

# Key idea:
# Maximum separation between data points of different classes.

# Used in:
# - Face recognition
# - Spam detection
# - Text classification
# - Bioinformatics