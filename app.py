import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from textwrap import wrap

# Function to create a professional PDF
def create_pdf(file_path, name, email, phone, linkedin, github, summary, skills, experience, education, projects):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 72  # 1-inch margin
    y_position = height - margin

    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y_position, name)
    y_position -= 20

    # Contact Information
    c.setFont("Helvetica", 10)
    c.drawString(margin, y_position, f"{email} | {phone} | LinkedIn: {linkedin} | GitHub: {github}")
    y_position -= 40

    # Professional Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "PROFESSIONAL SUMMARY")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for line in wrap(summary, width=80):
        c.drawString(margin, y_position, line)
        y_position -= 15
    y_position -= 20

    # Skills
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "SKILLS")
    y_position -= 20
    c.setFont("Helvetica", 10)
    skills_list = skills.split(",")
    for i, skill in enumerate(skills_list):
        c.drawString(margin + 20, y_position, f"• {skill.strip()}")
        y_position -= 15
    y_position -= 20

    # Work Experience
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "WORK EXPERIENCE")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for entry in experience.split("\n\n"):  # Separate each role by double newline
        lines = entry.split("\n")
        if len(lines) > 0:
            c.setFont("Helvetica-Bold", 10)
            c.drawString(margin + 20, y_position, lines[0])  # Position/Company
            y_position -= 15
            c.setFont("Helvetica", 10)
            for line in lines[1:]:
                c.drawString(margin + 40, y_position, f"• {line.strip()}")
                y_position -= 15
        y_position -= 10

    # Education
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "EDUCATION")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for entry in education.split("\n\n"):
        lines = entry.split("\n")
        if len(lines) > 0:
            c.setFont("Helvetica-Bold", 10)
            c.drawString(margin + 20, y_position, lines[0])  # Degree/University
            y_position -= 15
            c.setFont("Helvetica", 10)
            for line in lines[1:]:
                c.drawString(margin + 40, y_position, f"• {line.strip()}")
                y_position -= 15
        y_position -= 10

    # Projects
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "PROJECTS")
    y_position -= 20
    c.setFont("Helvetica", 10)
    for entry in projects.split("\n\n"):
        lines = entry.split("\n")
        if len(lines) > 0:
            c.setFont("Helvetica-Bold", 10)
            c.drawString(margin + 20, y_position, lines[0])  # Project Title
            y_position -= 15
            c.setFont("Helvetica", 10)
            for line in lines[1:]:
                c.drawString(margin + 40, y_position, f"• {line.strip()}")
                y_position -= 15
        y_position -= 10

    c.save()

# Streamlit UI
st.title("Resume Builder")

# Input fields
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
linkedin = st.text_input("LinkedIn URL")
github = st.text_input("GitHub URL")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience (separate roles by double newlines, use single newlines for details)")
education = st.text_area("Education (separate degrees by double newlines, use single newlines for details)")
projects = st.text_area("Projects (separate projects by double newlines, use single newlines for details)")

# Generate Resume button
if st.button("Generate Resume"):
    pdf_path = "resume.pdf"
    create_pdf(pdf_path, name, email, phone, linkedin, github, summary, skills, experience, education, projects)
    with open(pdf_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")
