import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


# Function to create Resume
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


# Function to create Cover Letter
def create_cover_letter(file_path, name, address, phone, email, company_name, job_title, key_skills, achievements):
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    elements = []

    # Define Styles
    header_style = ParagraphStyle(
        name="Header",
        fontSize=12,
        leading=14,
        fontName="Helvetica",
    )
    normal_style = ParagraphStyle(
        name="Normal",
        fontSize=10,
        leading=14,
        fontName="Helvetica",
    )

    # Cover Letter Content
    header_content = f"""
    {name}<br/>
    {address}<br/>
    {email} | {phone}<br/>
    <br/>
    {company_name}<br/>
    <br/>
    Dear Hiring Team at {company_name},<br/><br/>
    """
    elements.append(Paragraph(header_content, header_style))

    introduction = f"""
    I am excited to apply for the {job_title} position at {company_name}. With a solid foundation in {', '.join(key_skills.split(','))}, 
    I have successfully applied my expertise to solve complex challenges and drive impactful results. I came across this opportunity through [source, e.g., company website], 
    and I am eager to contribute to the continued success of your organization.
    """
    elements.append(Paragraph(introduction, normal_style))
    elements.append(Spacer(1, 12))

    achievements_paragraph = f"""
    Here are some of my key achievements:
    {chr(10).join([f"- {achievement.strip()}" for achievement in achievements.split(',')])}
    """
    elements.append(Paragraph(achievements_paragraph, normal_style))
    elements.append(Spacer(1, 12))

    conclusion = f"""
    I look forward to discussing how my qualifications align with your needs and exploring how I can contribute to the success of {company_name}. 
    Please feel free to contact me at {phone} or {email}. Thank you for considering my application.<br/><br/>
    Best regards,<br/>
    {name}
    """
    elements.append(Paragraph(conclusion.strip(), normal_style))

    # Build PDF
    doc.build(elements)


# Streamlit UI
st.set_page_config(page_title="Professional Docs Generator", layout="centered")
st.title("✨ Tailored Resume & Cover Letter Builder ✨")

# Sidebar Instructions
st.sidebar.title("Steps to Create Your Documents")
st.sidebar.write("### Steps to Create a Resume:")
st.sidebar.write("1. Fill out your personal information.")
st.sidebar.write("2. Enter your professional summary, education, skills, and experience.")
st.sidebar.write("3. Add projects you’ve worked on.")
st.sidebar.write("4. Click the 'Generate Resume' button to download your resume.")
st.sidebar.write("### Steps to Create a Cover Letter:")
st.sidebar.write("1. Enter your address, company name, and job title.")
st.sidebar.write("2. Provide key skills and achievements relevant to the job.")
st.sidebar.write("3. Click the 'Generate Cover Letter' button to download your cover letter.")

# Input fields for resume
st.header("Create Your Resume 📄")
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
st.header("Create Your Cover Letter ✉️")
address = st.text_area("Your Address")
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
    create_cover_letter(cover_letter_path, name, address, phone, email, company_name, job_title, key_skills, achievements)
    with open(cover_letter_path, "rb") as pdf_file:
        st.download_button("Download Cover Letter", pdf_file, file_name="cover_letter.pdf")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>✨ Designed with ❤️ using Streamlit, by Dibyanshi Singh ✨</p>",
    unsafe_allow_html=True,
)
