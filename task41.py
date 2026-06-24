from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "Win a free lottery",
    "Meeting at 10 AM",
    "Claim your prize now",
    "Project discussion tomorrow"
]

labels = [1, 0, 1, 0]  # 1 = Spam, 0 = Not Spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)

model = MultinomialNB()
model.fit(X, labels)

test = vectorizer.transform(["Free prize"])
print("Prediction:", model.predict(test))