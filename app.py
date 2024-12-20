from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit

def create_pdf(file_path, name, email, phone, linkedin, github, summary, skills, experience, education):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    margin = 72  # 1-inch margin
    y_position = height - margin

    # Helper Function to Wrap Text
    def wrap_text(text, max_width, x, y, font_size=10):
        c.setFont("Helvetica", font_size)
        lines = simpleSplit(text, "Helvetica", max_width)
        for line in lines:
            c.drawString(x, y, line)
            y -= 14
        return y

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(margin, y_position, name)
    c.drawImage("profile_picture.jpg", width - margin - 50, y_position - 25, width=50, height=50, preserveAspectRatio=True, anchor="n")
    y_position -= 40

    # Contact Information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Contact Information:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    c.drawString(margin, y_position, f"Email: {email}")
    y_position -= 15
    c.drawString(margin, y_position, f"Phone: {phone}")
    y_position -= 15
    c.drawString(margin, y_position, f"LinkedIn: {linkedin}")
    y_position -= 15
    c.drawString(margin, y_position, f"GitHub: {github}")
    y_position -= 30

    # Professional Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Professional Summary:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    y_position = wrap_text(summary, width - 2 * margin, margin, y_position)

    # Skills
    y_position -= 20
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Skills:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    skills_list = skills.split(",")
    col_width = (width - 2 * margin) / 3
    for i, skill in enumerate(skills_list):
        x_position = margin + (i % 3) * col_width
        c.drawString(x_position, y_position, skill.strip())
        if (i + 1) % 3 == 0:
            y_position -= 15

    # Work Experience
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Work Experience:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    experience_lines = experience.split("\n")
    for line in experience_lines:
        if y_position < margin:
            c.showPage()
            y_position = height - margin
        y_position = wrap_text(line, width - 2 * margin, margin, y_position)

    # Education
    y_position -= 30
    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, y_position, "Education:")
    y_position -= 20
    c.setFont("Helvetica", 10)
    education_lines = education.split("\n")
    for line in education_lines:
        if y_position < margin:
            c.showPage()
            y_position = height - margin
        y_position = wrap_text(line, width - 2 * margin, margin, y_position)

    c.save()
