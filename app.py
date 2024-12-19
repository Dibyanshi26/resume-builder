from flask import Flask, request, send_file, render_template_string, send_from_directory

app = Flask(__name__)

# Route to serve CSS file
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Process form submission here
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        summary = request.form['summary']
        skills = request.form['skills']
        experience = request.form['experience']
        education = request.form['education']
        # Implement the resume generation logic
        pass

    # HTML template with CSS included
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Resume Builder</title>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
    </head>
    <body>
        <div class="container">
            <h1>Resume Builder</h1>
            <form method="post">
                <label>Name:</label> <input type="text" name="name" required><br><br>
                <label>Email:</label> <input type="email" name="email" required><br><br>
                <label>Phone:</label> <input type="tel" name="phone" required><br><br>
                <label>Summary:</label><br>
                <textarea name="summary" rows="3" required></textarea><br><br>
                <label>Skills (comma-separated):</label><br>
                <textarea name="skills" rows="3" required></textarea><br><br>
                <label>Work Experience (separate by new lines):</label><br>
                <textarea name="experience" rows="5" required></textarea><br><br>
                <label>Education (separate by new lines):</label><br>
                <textarea name="education" rows="3" required></textarea><br><br>
                <input type="submit" value="Generate Resume">
            </form>
        </div>
    </body>
    </html>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
