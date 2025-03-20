import streamlit as st
from resume_parser import extract_text_from_pdf, extract_text_from_docx, extract_skills

from ats_scoring import calculate_similarity

st.title("📄 Resume Scanner & ATS Score Predictor")

# Upload resume
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX)", type=["pdf", "docx"])

# Input job description
job_desc = st.text_area("Paste Job Description Here")

if uploaded_file and job_desc:
    file_type = uploaded_file.name.split(".")[-1]
    
    # Extract text based on file type
    resume_text = extract_text_from_pdf(uploaded_file) if file_type == "pdf" else extract_text_from_docx(uploaded_file)

    # Extract skills
    found_skills = extract_skills(resume_text)

    # Calculate similarity score
    ats_score = calculate_similarity(resume_text, job_desc)

    # Display results
    st.subheader("📊 Resume Analysis")
    st.write(f"✅ **ATS Score:** {ats_score:.2f}%")
    st.write(f"📌 **Skills Identified:** {', '.join(found_skills)}")

    # Improvement Suggestions
    if ats_score < 50:
        st.warning("⚠️ Your resume needs improvement. Try adding more keywords from the job description!")


