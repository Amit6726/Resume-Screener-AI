import streamlit as st
import os
from backend.utils import clean_text
from backend.ats_checker import check_ats_compliance
from backend.predictor import predict_job_fit
from backend.resume_parser import extract_text_from_image
from pdf2image import convert_from_path
from PIL import Image

st.set_page_config("Resume Screener AI", layout="centered")
st.title("Resume Screener AI with OCR")

ocr_mode = st.selectbox("Choose OCR Engine", ["tesseract", "easyocr"])

uploaded_file = st.file_uploader("Upload Resume (Image or PDF)", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    upload_dir = "data/resumes"
    os.makedirs(upload_dir, exist_ok=True)
    save_path = os.path.join(upload_dir, uploaded_file.name)

    # with open(save_path, "wb") as f:
    #     f.write(uploaded_file.read())
    # st.info("Processing file...")

    if uploaded_file.name.lower().endswith(".pdf"):
        images = convert_from_path(save_path)
        if images:
            image_path = save_path.replace(".pdf", "_page1.jpg")
            images[0].save(image_path, "JPEG")
            st.image(image_path, caption="Page 1 of PDF",use_container_width=True)
            extracted_text = extract_text_from_image(image_path, mode=ocr_mode)
        else:
            st.error("No pages found in PDF.")
            extracted_text = ""
    else:
        st.image(save_path, caption="Uploaded Resume",use_container_width=True)
        extracted_text = extract_text_from_image(save_path, mode=ocr_mode)
    clean = clean_text(extracted_text)

    st.text_area("Extracted Text", clean, height=300)

    if st.button("Analyze Resume"):
        score, tips = check_ats_compliance(clean)
        role = predict_job_fit(clean)

        st.metric("ATS Match", f"{score:.2f}%")
        st.success(f"Predicted Job Role: {role}")

        if tips:
            st.subheader("Suggestions to Improve")
            for tip in tips:
                st.warning(tip)

        
# ========== Developer Info Footer ==========
st.markdown("---")  # separator line
st.title("👨‍💻 Developer Info")
st.write("**Amit Kumar** — AI Developer")
st.write("📞 Contact: 7087376726")
st.write("📧 Email: [amitrajput6726@gmail.com](mailto:amitrajput6726@gmail.com)")
st.write("🔗 [LinkedIn Profile](https://www.linkedin.com/in/amit-kumar-89b7b4218/)")