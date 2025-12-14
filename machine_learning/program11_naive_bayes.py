# Program 11: Naive Bayes for text classification
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

docs = ["I love Python", "Python is great", "I dislike bugs"]
labels = [1, 1, 0]

cv = CountVectorizer()
X = cv.fit_transform(docs)

model = MultinomialNB()
model.fit(X, labels)

print("Prediction:", model.predict(cv.transform(["I love coding"])))
