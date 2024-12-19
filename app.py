from flask import Flask, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        summary = request.form['summary']
        skills = request.form['skills']
        experience = request.form['experience']
        education = request.form['education']

        # Create PDF
        pdf_path = "resume.pdf"
        create_pdf(pdf_path, name, email, phone, summary, skills, experience, education)
        return send_file(pdf_path, as_attachment=True)

    # Render the input form
    return '''
        <form method="post">
            <label>Name:</label> <input type="text" name="name" required><br><br>
            <label>Email:</label> <input type="email" name="email" required><br><br>
            <label>Phone:</label> <input type="tel" name="phone" required><br><br>
            <label>Summary:</label><br>
            <textarea name="summary" rows="3" cols="50" required></textarea><br><br>
            <label>Skills (comma-separated):</label><br>
            <textarea name="skills" rows="3" cols="50" required></textarea><br><br>
            <label>Work Experience (separate by new lines):</label><br>
            <textarea name="experience" rows="5" cols="50" required></textarea><br><br>
            <label>Education (separate by new lines):</label><br>
            <textarea name="education" rows="3" cols="50" required></textarea><br><br>
            <input type="submit" value="Generate Resume">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
