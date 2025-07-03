import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

df = pd.read_csv('data/training_data.csv')
X, y = df['text'], df['category']

vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
joblib.dump(model, 'models/job_fit_model.pkl')
print("Model saved.")
