from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

STUDENT = {
    "name": "Swarda Naik",
    "roll_number": "69",
    "department": "Computer Science and Engineering (AIML)",
    "academic_year": "2026-27"
}

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Information System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f4f8;
                text-align: center;
                padding: 50px;
            }
            .card {
                background: white;
                max-width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px #0002;
            }
            h1 { color: #173b68; }
            p { font-size: 17px; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Student Information System</h1>
            <p><b>Name:</b> {{ student.name }}</p>
            <p><b>Roll Number:</b> {{ student.roll_number }}</p>
            <p><b>Department:</b> {{ student.department }}</p>
            <p><b>Academic Year:</b> {{ student.academic_year }}</p>
            <p>Application deployed using Docker and Jenkins.</p>
        </div>
    </body>
    </html>
    """, student=STUDENT)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "Student Information System"
    }), 200

@app.route("/api/student")
def student_details():
    return jsonify(STUDENT), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)