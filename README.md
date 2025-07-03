
# Resume Screener AI

Resume Screener AI is an intelligent tool designed to parse resumes, extract relevant information using OCR, check for ATS (Applicant Tracking System) friendliness, and predict job-fit using machine learning models.


**Developer Info**
Amit Kumar
AI Developer
📞 Contact – 7087376726
📧 Email – **amitrajput6726@gmail.com**
🔗 LinkedIn – [https://www.linkedin.com/in/amit-kumar-89b7b4218/](https://www.linkedin.com/in/amit-kumar-89b7b4218/ "HIRE ME")

---

## Features

- **OCR-based Resume Parsing** (PDFs, Images)
- **ATS-Friendliness Scoring** using keyword matching
- **Job-fit Prediction** using trained ML models
- **Configurable OCR Modes**: Tesseract, EasyOCR, CRAFT
- **Modular Backend** built with Flask or Streamlit
- **Pluggable ML Architecture**: Easy training and model switching

---

## Project Structure

resume_screener_ai/
├── backend/
│ ├── app.py # Streamlit or Flask app entry point
│ ├── resume_parser.py # OCR pipeline (Tesseract, EasyOCR, CRAFT)
│ ├── ats_checker.py # ATS-friendly scoring & keyword checks
│ ├── model_trainer.py # (Optional) ML model training script
│ ├── utils.py # Helpers for cleaning, formatting, etc.
│ ├── config.py # Config for switching OCR modes, paths
├── models/
│ ├── tfidf_vectorizer.pkl # Saved TF-IDF model
│ ├── job_fit_model.pkl # ML model for job-fit prediction
├── data/
│ ├── resumes/ # Input test resumes (PDF/images)
│ ├── training_data.csv # Sample data for job-fit classifier
├── requirements.txt # Dependencies
├── README.md # Project overview and setup

yaml
Copy
Edit

---

## Getting Started

1. Clone the repository:

```bash


git clone https://github.com/yourusername/resume_screener_ai.git
cd resume_screener_ai
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the backend app:

bash
Copy
Edit
python backend/app.py
 Dependencies
Python 3.7+

Flask / Streamlit

Tesseract OCR / EasyOCR / CRAFT

Scikit-learn

Pandas

OpenCV

PyMuPDF or pdfminer

NLTK / SpaCy

Future Enhancements
UI enhancements using React frontend

Integration with job portals or LinkedIn

More powerful LLM-based job-fit prediction


```
