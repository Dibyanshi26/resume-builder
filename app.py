import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, Image
from textwrap import wrap

def create_pdf(file_path, name, email, phone, summary, skills, experience, education, image_path=None):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 50  # Define margins
    y_position = height - 60

    # Header with optional photo
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, y_position, name)
    if image_path:
        c.drawImage(image_path, width - 100, y_position - 50, width=50, height=50, mask='auto')
    c.line(margin, y_position - 5, width - margin, y_position - 5)
    y_position -= 40

    # Contact Information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Contact Information:")
    c.setFont("Helvetica", 10)
    y_position -= 20
    c.drawString(margin + 20, y_position, f"Email: {email}")
    y_position -= 15
    c.drawString(margin + 20, y_position, f"Phone: {phone}")

    # Professional Summary
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Professional Summary:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for line in wrap(summary, 90):
        c.drawString(margin + 20, y_position, line)
        y_position -= 15

    # Skills
    y_position -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Skills:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    skills_list = [skill.strip() for skill in skills.split(',')]
    skill_columns = [skills_list[i:i + 4] for i in range(0, len(skills_list), 4)]
    for skill_row in skill_columns:
        c.drawString(margin + 20, y_position, ", ".join(skill_row))
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
        c.drawString(margin + 20, y_position, line)
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

# Photo upload
image_file = st.file_uploader("Upload a photo (optional)", type=["png", "jpg", "jpeg"])
image_path = None
if image_file is not None:
    with open("uploaded_image.png", "wb") as f:
        f.write(image_file.getbuffer())
    image_path = "uploaded_image.png"

# Generate Resume button
if st.button("Generate Resume"):
    pdf_path = "resume.pdf"
    create_pdf(pdf_path, name, email, phone, summary, skills, experience, education, image_path)
    with open(pdf_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")
