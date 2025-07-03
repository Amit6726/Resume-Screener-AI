import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

df = pd.read_csv('data/training_data.csv')
X = df['text']
y = df['category']

os.makedirs('models', exist_ok=True)

vectorizer = TfidfVectorizer(stop_words='english', max_features=3000)
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=300)
model.fit(X_vec, y)

joblib.dump(vectorizer, 'models/tfidf_vectorizer.pkl')
joblib.dump(model, 'models/job_fit_model.pkl')

print("✅ Model training complete.")
