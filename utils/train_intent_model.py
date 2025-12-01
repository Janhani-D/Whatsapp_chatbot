import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Load dataset
data = json.load(open("intents.json", encoding="utf-8"))


texts = []
labels = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        texts.append(pattern)
        labels.append(intent["tag"])

# Convert text → features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
clf = LinearSVC()
clf.fit(X, labels)

# Save model
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))
pickle.dump(clf, open("model/classifier.pkl", "wb"))

print("Model training complete ✔")
