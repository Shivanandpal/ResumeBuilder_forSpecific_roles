import streamlit as st
from model import predict_skills, predict_projects
from utils import generate_resume, create_pdf

st.title("🚀 AI Resume Builder")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
education = st.text_area("Education")
experience=st.text_area("Experience")
role = st.text_input("Job Role")
company = st.text_input("Company")
address=st.text_area("Address")


# 🔥 THIS BUTTON IS CRITICAL
if st.button("Generate Resume"):

    print("BUTTON CLICKED")  # DEBUG

    # Step 1
    skills = predict_skills(role, company)

    # Step 2
    projects = predict_projects(role, company)

    # Step 3
    data = {
        "name": name,
        "email": email,
        "phone": phone,
        "address":address,
        "education": education,
        "experience":experience,
        "role": role,
        "company": company
    }

    # Step 4
    resume = generate_resume(data, skills, projects)

    st.subheader("📄 Preview")
    st.text(resume)

    # 🔥 THIS MUST RUN
    print("CALLING PDF FUNCTION")

    file_path = create_pdf(data, skills, projects)

    print("PDF CREATED")

    with open(file_path, "rb") as f:
        st.download_button("⬇ Download Resume", f, file_name="resume.pdf")