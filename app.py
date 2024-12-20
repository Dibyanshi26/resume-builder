import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


def create_resume(file_path, name, email, phone, linkedin, github, tableau, summary, education, skills, experience, projects):
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    elements = []

    # Define Styles
    header_style = ParagraphStyle(
        name="Header",
        fontSize=14,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
        spaceAfter=12,
    )
    section_header_style = ParagraphStyle(
        name="SectionHeader",
        fontSize=12,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#333333"),
        spaceAfter=10,
        spaceBefore=20,
    )
    normal_style = ParagraphStyle(
        name="Normal",
        fontSize=10,
        leading=12,
        fontName="Helvetica",
    )

    # Header Section
    header_content = f"""
    <b>{name.upper()}</b><br/>
    {email} | {phone} | <a href='{linkedin}'>LinkedIn</a> | <a href='{github}'>GitHub</a> | <a href='{tableau}'>Tableau Public</a>
    """
    elements.append(Paragraph(header_content, header_style))
    elements.append(Spacer(1, 12))

    # Professional Summary
    elements.append(Paragraph("Professional Summary", section_header_style))
    elements.append(Paragraph(summary, normal_style))
    elements.append(Spacer(1, 12))

    # Education Section
    elements.append(Paragraph("Education", section_header_style))
    for entry in education.split("\n\n"):
        if entry.strip():
            elements.append(Paragraph(entry.strip(), normal_style))
            elements.append(Spacer(1, 6))

    # Skills Section
    elements.append(Paragraph("Skills", section_header_style))
    skills_list = skills.split(',')
    for skill in skills_list:
        elements.append(Paragraph(f"- {skill.strip()}", normal_style))
    elements.append(Spacer(1, 12))

    # Work Experience Section
    elements.append(Paragraph("Work Experience", section_header_style))
    for entry in experience.split("\n\n"):
        if entry.strip():
            elements.append(Paragraph(entry.strip(), normal_style))
            elements.append(Spacer(1, 6))

    # Projects Section
    elements.append(Paragraph("Projects", section_header_style))
    for entry in projects.split("\n\n"):
        if entry.strip():
            elements.append(Paragraph(entry.strip(), normal_style))
            elements.append(Spacer(1, 6))

    # Build PDF
    doc.build(elements)


def create_cover_letter(file_path, name, company_name, job_title, key_skills, achievements):
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    elements = []

    # Define Styles
    normal_style = ParagraphStyle(
        name="Normal",
        fontSize=10,
        leading=12,
        fontName="Helvetica",
    )

    # Cover Letter Content
    cover_letter_content = f"""
    Dear Hiring Manager at {company_name},

    I am writing to express my enthusiasm for the {job_title} position at {company_name}. With a solid foundation in {', '.join(key_skills.split(','))}, 
    I have successfully applied my expertise to solve complex challenges and drive impactful results. My commitment to innovation and precision aligns seamlessly 
    with the values and goals of your organization.

    Over the course of my career, I have achieved several milestones, such as:
    {chr(10).join([f"- {achievement.strip()}" for achievement in achievements.split(',')])}

    These experiences have honed my ability to adapt to evolving business needs and leverage analytical tools to optimize processes and uncover opportunities for growth. 
    My skills in {', '.join(key_skills.split(',')[:5])} have allowed me to excel in cross-functional teams and deliver high-quality results, even under tight deadlines.

    At {company_name}, I am eager to bring my passion for data-driven insights and my proven track record of success to contribute meaningfully to your team. 
    The {job_title} role presents the perfect opportunity for me to combine my skills and experience with my desire to make a measurable impact.

    Thank you for considering my application. I would welcome the chance to discuss how my qualifications align with your needs and explore how I can contribute to the continued success of {company_name}. 
    Please feel free to contact me at {phone} or {email} to schedule a conversation.

    Best regards,
    {name}
    """
    elements.append(Paragraph(cover_letter_content.strip(), normal_style))

    # Build PDF
    doc.build(elements)


# Streamlit UI
st.title("Resume and Cover Letter Generator")

# Input fields for resume
st.header("Resume")
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
linkedin = st.text_input("LinkedIn URL")
github = st.text_input("GitHub URL")
tableau = st.text_input("Tableau Public URL")
summary = st.text_area("Professional Summary")
education = st.text_area("Education (separate entries with two newlines, format: Institution Location Degree Dates)")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience (separate entries with two newlines, format: Company - Details)")
projects = st.text_area("Projects (separate entries with two newlines, format: Project - Details)")

# Input fields for cover letter
st.header("Cover Letter")
company_name = st.text_input("Company Name")
job_title = st.text_input("Job Title")
key_skills = st.text_area("Key Skills (comma-separated)")
achievements = st.text_area("Achievements (comma-separated)")

# Generate Resume and Cover Letter buttons
if st.button("Generate Resume"):
    resume_path = "resume.pdf"
    create_resume(resume_path, name, email, phone, linkedin, github, tableau, summary, education, skills, experience, projects)
    with open(resume_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")

if st.button("Generate Cover Letter"):
    cover_letter_path = "cover_letter.pdf"
    create_cover_letter(cover_letter_path, name, company_name, job_title, key_skills, achievements)
    with open(cover_letter_path, "rb") as pdf_file:
        st.download_button("Download Cover Letter", pdf_file, file_name="cover_letter.pdf")
