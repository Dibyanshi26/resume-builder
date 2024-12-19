import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Function to create a professional, ATS-friendly PDF
def create_pdf(file_path, name, email, phone, summary, skills, experience, education):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 50  # Define a margin for better layout
    y_position = height - 60

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, y_position, "Resume")
    c.line(margin, y_position - 5, width - margin, y_position - 5)  # Add a horizontal line for style

    # Personal Info
    y_position -= 40
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Contact Information:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    c.drawString(margin + 20, y_position, f"Name: {name}")
    y_position -= 15
    c.drawString(margin + 20, y_position, f"Email: {email}")
    y_position -= 15
    c.drawString(margin + 20, y_position, f"Phone: {phone}")

    # Summary
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Professional Summary:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for line in summary.split("\n"):
        c.drawString(margin + 20, y_position, line)
        y_position -= 15

    # Skills
    y_position -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Skills:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    skills_list = skills.split(',')
    col_width = 200
    for i, skill in enumerate(skills_list):
        x_position = margin + (i % 3) * col_width
        c.drawString(x_position, y_position, f"- {skill.strip()}")
        if (i + 1) % 3 == 0:
            y_position -= 15

    # Work Experience
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Work Experience:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for line in experience.split("\n"):
        if y_position < 50:  # Add a new page if content exceeds current page
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
        if y_position < 50:  # Add a new page if content exceeds current page
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

# Generate Resume button
if st.button("Generate Resume"):
    pdf_path = "resume.pdf"
    create_pdf(pdf_path, name, email, phone, summary, skills, experience, education)
    with open(pdf_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")
