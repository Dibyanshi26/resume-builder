import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors

def create_pdf(file_path, name, email, phone, summary, skills, experience, education, photo_path=None):
    # Create PDF document
    doc = SimpleDocTemplate(file_path, pagesize=letter, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=72)
    elements = []
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        name="Title",
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName="Helvetica-Bold"
    )
    section_header_style = ParagraphStyle(
        name="SectionHeader",
        fontSize=14,
        leading=18,
        fontName="Helvetica-Bold",
        textColor=colors.HexColor("#333333"),
        spaceAfter=10,
        spaceBefore=20,
    )
    normal_style = ParagraphStyle(
        name="Normal",
        fontSize=10,
        leading=14,
        fontName="Helvetica",
    )

    # Add title
    elements.append(Paragraph(name, title_style))
    elements.append(Spacer(1, 12))

    # Add photo if provided
    if photo_path:
        elements.append(Image(photo_path, width=1.5 * inch, height=1.5 * inch, hAlign="RIGHT"))
        elements.append(Spacer(1, 12))

    # Contact Information
    contact_info = f"Email: {email}<br/>Phone: {phone}"
    elements.append(Paragraph("Contact Information:", section_header_style))
    elements.append(Paragraph(contact_info, normal_style))
    elements.append(Spacer(1, 12))

    # Professional Summary
    elements.append(Paragraph("Professional Summary:", section_header_style))
    elements.append(Paragraph(summary, normal_style))
    elements.append(Spacer(1, 12))

    # Skills
    elements.append(Paragraph("Skills:", section_header_style))
    skills_list = skills.split(',')
    skills_table = [[skill.strip() for skill in skills_list[i:i+3]] for i in range(0, len(skills_list), 3)]
    skills_table_formatted = Table(skills_table, colWidths=[2.5 * inch] * 3)
    skills_table_formatted.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#333333")),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))
    elements.append(skills_table_formatted)
    elements.append(Spacer(1, 12))

    # Work Experience
    elements.append(Paragraph("Work Experience:", section_header_style))
    experience_lines = experience.split('\n')
    for line in experience_lines:
        elements.append(Paragraph(f"• {line}", normal_style))
    elements.append(Spacer(1, 12))

    # Education
    elements.append(Paragraph("Education:", section_header_style))
    education_lines = education.split('\n')
    for line in education_lines:
        elements.append(Paragraph(f"• {line}", normal_style))
    elements.append(Spacer(1, 12))

    # Build the PDF
    doc.build(elements)

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
photo_path = st.file_uploader("Upload a photo", type=["jpg", "png"])

# Generate Resume button
if st.button("Generate Resume"):
    pdf_path = "resume.pdf"
    photo_file = None
    if photo_path:
        photo_file = f"uploaded_{photo_path.name}"
        with open(photo_file, "wb") as f:
            f.write(photo_path.getvalue())

    create_pdf(pdf_path, name, email, phone, summary, skills, experience, education, photo_file)
    with open(pdf_path, "rb") as pdf_file:
        st.download_button("Download Resume", pdf_file, file_name="resume.pdf")
