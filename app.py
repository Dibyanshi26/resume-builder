import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from textwrap import wrap


# Function to create a professional, ATS-friendly PDF
def create_pdf(file_path, name, email, phone, linkedin, github, summary, skills, experience, education):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 50
    y_position = height - 60

    # Header with Name and Contact Information
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, y_position, name)
    y_position -= 25
    c.setFont("Helvetica", 10)
    c.drawString(margin, y_position, f"Email: {email}")
    y_position -= 15
    c.drawString(margin, y_position, f"Phone: {phone}")
    y_position -= 15
    c.drawString(margin, y_position, f"LinkedIn: {linkedin}")
    y_position -= 15
    c.drawString(margin, y_position, f"GitHub: {github}")
    y_position -= 30

    # Professional Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Professional Summary:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    wrapped_summary = wrap(summary, width=90)
    for line in wrapped_summary:
        c.drawString(margin, y_position, line)
        y_position -= 15

    # Skills Section
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Skills:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    skill_lines = [
        "Programming and Database: Python (Streamlit, Pandas, Matplotlib, Seaborn), R, SQL, MySQL, Neo4j, MongoDB",
        "Data Visualization and Analytics: Tableau, Power BI, MS Excel, Predictive Modeling, Power Query",
        "Cloud and Platforms: Microsoft Azure, Google Cloud Platform (GCP)",
        "Tools and Other Skills: Git/GitHub, APIs (RESTful), Image Processing, ETL Processes, HTML, CSS, JavaScript"
    ]
    for skill in skill_lines:
        c.drawString(margin, y_position, skill)
        y_position -= 15

    # Work Experience
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Work Experience:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for line in experience.split("\n"):
        if y_position < 50:
            c.showPage()
            y_position = height - 50
        c.drawString(margin, y_position, line)
        y_position -= 15

    # Education
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Education:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for line in education.split("\n"):
        if y_position < 50:
            c.showPage()
            y_position = height - 50
        c.drawString(margin, y_position, line)
        y_position -= 15

    c.save()


# Streamlit UI
st.title("Resume Builder")

# Input fields
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
linkedin = st.text_input("LinkedIn Profile URL")
github = st.text_input("GitHub Profile URL")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills")
experience = st.text_area("Work Experience (separate by new lines)")
education = st.text_area("Education (separate by new lines)")

# Generate Resume button
if st.button("Generate Resume"):
    pdf_path = "resume.pdf"
    create_pdf(pdf_path, name, email, phone, linkedin, github, summary, skills, experience, education)
    with open(pdf_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")
