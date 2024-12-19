import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Function to create a professional, ATS-friendly PDF
def create_pdf(file_path, name, email, phone, summary, skills, experience, education):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 50  # Define a margin for better layout
    y_position = height - 60  # Start position for content

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, y_position, "Resume")
    c.line(margin, y_position - 5, width - margin, y_position - 5)  # Add a horizontal line for style
    y_position -= 40

    # Contact Information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Contact Information:")
    c.setFont("Helvetica", 10)
    c.drawString(margin + 20, y_position - 20, f"Name: {name}")
    c.drawString(margin + 20, y_position - 40, f"Email: {email}")
    c.drawString(margin + 20, y_position - 60, f"Phone: {phone}")
    y_position -= 100

    # Professional Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Professional Summary:")
    c.setFont("Helvetica", 10)
    y_position -= 20
    for line in summary.splitlines():
        c.drawString(margin + 20, y_position, line)
        y_position -= 15
    y_position -= 20

    # Skills
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Skills:")
    c.setFont("Helvetica", 10)
    y_position -= 20
    skills_list = skills.split(',')
    for skill in skills_list:
        c.drawString(margin + 20, y_position, f"- {skill.strip()}")
        y_position -= 15
    y_position -= 20

    # Work Experience
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Work Experience:")
    c.setFont("Helvetica", 10)
    y_position -= 20
    experience_lines = experience.splitlines()
    for line in experience_lines:
        c.drawString(margin + 20, y_position, line)
        y_position -= 15
    y_position -= 20

    # Education
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Education:")
    c.setFont("Helvetica", 10)
    y_position -= 20
    education_lines = education.splitlines()
    for line in education_lines:
        c.drawString(margin + 20, y_position, line)
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
