import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import inch
from reportlab.lib import colors


def create_pdf(file_path, name, email, phone, linkedin, github, tableau, summary, education, skills, experience, projects):
    # PDF Document with 1-inch margins
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    elements = []
    styles = getSampleStyleSheet()

    # Custom styles
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
    education_lines = education.split('\n')
    for line in education_lines:
        if line.strip():  # Skip empty lines
            if line.startswith("•"):
                # Details in regular style
                elements.append(Paragraph(line.strip("•").strip(), normal_style))
            else:
                # Institution name in bold
                elements.append(Paragraph(f"<b>{line}</b>", normal_style))
    elements.append(Spacer(1, 12))

    # Skills
    elements.append(Paragraph("Skills", section_header_style))
    skills_list = skills.split(',')
    skills_table = [[skill.strip() for skill in skills_list[i:i+3]] for i in range(0, len(skills_list), 3)]
    skills_table_formatted = Table(skills_table, colWidths=[2 * inch] * 3)
    skills_table_formatted.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#333333")),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ]))
    elements.append(skills_table_formatted)
    elements.append(Spacer(1, 12))

    # Work Experience
    elements.append(Paragraph("Work Experience", section_header_style))
    experience_lines = experience.split('\n')
    for line in experience_lines:
        if line.strip():  # Skip empty lines
            if line.startswith("•"):
                # Regular details in bullet points
                elements.append(Paragraph(line.strip("•").strip(), normal_style))
            else:
                # Job title or organization in bold
                elements.append(Paragraph(f"<b>{line}</b>", normal_style))
    elements.append(Spacer(1, 12))

    # Projects
    elements.append(Paragraph("Projects", section_header_style))
    project_lines = projects.split('\n')
    for line in project_lines:
        if line.strip():  # Skip empty lines
            if line.startswith("•"):
                # Regular details in bullet points
                elements.append(Paragraph(line.strip("•").strip(), normal_style))
            else:
                # Project name in bold
                elements.append(Paragraph(f"<b>{line}</b>", normal_style))
    elements.append(Spacer(1, 12))

    # Build the PDF
    doc.build(elements)


# Streamlit UI
st.title("Resume Builder")

# Input fields
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
linkedin = st.text_input("LinkedIn URL")
github = st.text_input("GitHub URL")
tableau = st.text_input("Tableau Public URL")
summary = st.text_area("Professional Summary")
education = st.text_area("Education (separate by new lines)")
skills = st.text_area("Skills (comma-separated)")
experience = st.text_area("Work Experience (separate by new lines)")
projects = st.text_area("Projects (separate by new lines)")

# Generate Resume button
if st.button("Generate Resume"):
    pdf_path = "resume.pdf"
    create_pdf(pdf_path, name, email, phone, linkedin, github, tableau, summary, education, skills, experience, projects)
    with open(pdf_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")
