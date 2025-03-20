import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from resume_parser import extract_text

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):
    doc = nlp(text)
    skills = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN"]]
    return skills

def calculate_ats_score(resume_text, job_description):
    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity_score[0][0] * 100  # Convert to percentage

# ✅ **Test the model**
if __name__ == "__main__":
    resume_text = extract_text("Saikumar_Mehtre_MisExecutive.pdf")
    job_description = open("job_descriptions.txt").read()

    extracted_skills = extract_skills(resume_text)
    ats_score = calculate_ats_score(resume_text, job_description)

    print("\nExtracted Skills:", extracted_skills)
    print(f"\n📊 ATS Score: {ats_score:.2f}%")

def load_skills():
    with open("datasets/skills_list.txt", "r") as file:
        return [skill.strip().lower() for skill in file.readlines()]

def extract_skills(text):
    skills_db = load_skills()
    doc = nlp(text.lower())
    extracted_skills = [token.text for token in doc if token.text in skills_db]
    return list(set(extracted_skills))  # Remove duplicates
