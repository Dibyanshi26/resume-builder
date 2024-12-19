import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Function to create a professional, ATS-friendly PDF
def create_pdf(file_path, name, email, phone, summary, skills, experience, education):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 50  # Define a margin for better layout

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, height - 60, "Resume")
    c.line(margin, height - 65, width - margin, height - 65)  # Add a horizontal line for style

    # Personal Info
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, height - 100, "Contact Information:")
    c.setFont("Helvetica", 10)
    c.drawString(margin + 20, height - 120, f"Name: {name}")
    c.drawString(margin + 20, height - 140, f"Email: {email}")
    c.drawString(margin + 20, height - 160, f"Phone: {phone}")

    # Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, height - 200, "Professional Summary:")
    c.setFont("Helvetica", 10)
    c.drawString(margin + 20, height - 220, summary)

    # Skills
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, height - 260, "Skills:")
    c.setFont("Helvetica", 10)
    skills_list = skills.split(',')
    for i, skill in enumerate(skills_list):
        c.drawString(margin + 20, height - 280 - (i * 15), f"- {skill.strip()}")

    # Experience
    y_position = height - 300 - (len(skills_list) * 15)  # Adjust position dynamically
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Work Experience:")
    c.setFont("Helvetica", 10)
    experience_lines = experience.split('\n')
    for i, line in enumerate(experience_lines):
        c.drawString(margin + 20, y_position - 20 - (i * 15), line.strip())

    # Education
    y_position -= 40 + (len(experience_lines) * 15)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Education:")
    c.setFont("Helvetica", 10)
    education_lines = education.split('\n')
    for i, line in enumerate(education_lines):
        c.drawString(margin + 20, y_position - 20 - (i * 15), line.strip())

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
