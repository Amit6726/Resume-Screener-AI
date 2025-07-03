import joblib

model = joblib.load("models/job_fit_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

def predict_job_fit(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)
    return prediction[0]
