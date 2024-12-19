import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from textwrap import wrap


# Function to create a professional, ATS-friendly PDF
def create_pdf(file_path, name, email, phone, summary, skills, experience, education):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 72  # 1 inch margin
    y_position = height - margin

    # Header
    c.setFont("Helvetica-Bold", 20)
    c.drawString(margin, y_position, name)
    c.setFont("Helvetica", 10)
    c.drawString(margin, y_position - 15, email)
    c.drawString(margin, y_position - 30, phone)
    y_position -= 50

    # Professional Summary
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y_position, "PROFESSIONAL SUMMARY")
    y_position -= 20
    c.setFont("Helvetica", 10)
    wrapped_summary = wrap(summary, width=90)  # Wrap summary for better layout
    for line in wrapped_summary:
        c.drawString(margin, y_position, line)
        y_position -= 15

    # Skills
    y_position -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y_position, "SKILLS")
    y_position -= 20
    c.setFont("Helvetica", 10)
    skills_list = skills.split(',')
    for i, skill in enumerate(skills_list):
        c.drawString(margin + (i % 2) * (width / 2), y_position, f"- {skill.strip()}")
        if (i + 1) % 2 == 0:
            y_position -= 15

    # Work Experience
    y_position -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y_position, "WORK EXPERIENCE")
    y_position -= 20
    c.setFont("Helvetica", 10)
    experience_lines = experience.split('\n')
    for line in experience_lines:
        if y_position < margin:  # Add new page if content exceeds page height
            c.showPage()
            y_position = height - margin
        c.drawString(margin, y_position, line.strip())
        y_position -= 15

    # Education
    y_position -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(margin, y_position, "EDUCATION")
    y_position -= 20
    c.setFont("Helvetica", 10)
    education_lines = education.split('\n')
    for line in education_lines:
        if y_position < margin:
            c.showPage()
            y_position = height - margin
        c.drawString(margin, y_position, line.strip())
        y_position -= 15

    c.save()


# Streamlit UI
st.title("Resume Builder")

# Input fields
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience (separate by new lines)")
education = st.text_area("Education (separate by new lines)")

# Generate Resume button
if st.button("Generate Resume"):
    pdf_path = "resume.pdf"
    create_pdf(pdf_path, name, email, phone, summary, skills, experience, education)
    with open(pdf_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")
