from flask import Flask, request, jsonify
from backend.utils import clean_text
from backend.predictor import predict_job_fit
from backend.ats_checker import check_ats_compliance

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    raw_text = data.get("text", "")
    clean = clean_text(raw_text)
    prediction = predict_job_fit(clean)
    score, tips = check_ats_compliance(clean)

    return jsonify({
        "prediction": prediction,
        "ats_score": score,
        "tips": tips
    })

if __name__ == '__main__':
    app.run(debug=True)
