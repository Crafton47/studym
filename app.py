from flask import Flask, render_template, request, jsonify, send_from_directory, session, redirect, url_for
import sqlite3
import smtplib
import os
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev_secret_key_change_in_production')

# Gmail SMTP Configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'ilovestudy6869@gmail.com'
EMAIL_PASSWORD = 'xkapyivuqkpywkzh'
FROM_NAME = 'Smart Study Platform'

# PDF Materials mapping
PDF_MATERIALS = {
    'Mathematics - Calculus Notes': 'materials/calculus_basics.pdf',
    'Physics - Quantum Mechanics Video': 'materials/physics_mechanics.pdf',
    'Chemistry - Organic Chemistry Assignment': 'materials/calculus_basics.pdf',
    'Computer Science - Data Structures Practice': 'materials/physics_mechanics.pdf'
}

def send_email(to_email, subject, message, pdf_path=None):
    # Real Gmail sending is now configured
    print(f"Sending email to: {to_email}")
    
    # Production email sending
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = f"{FROM_NAME} <{EMAIL_ADDRESS}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Create HTML version
        clean_subject = subject.replace('📚 Study Material: ', '')
        html_content = message.replace('\n', '<br>')
        username = session.get('username', 'Student') if 'session' in globals() else 'Student'
        
        html_message = f"""
        <html>
          <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="max-width: 600px; margin: 0 auto; padding: 20px;">
              <h2 style="color: #007bff;">📚 {clean_subject}</h2>
              <p>Hello <strong>{username}</strong>,</p>
              <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin: 20px 0;">
                {html_content}
              </div>
              <p style="color: #666; font-size: 14px;">Best regards,<br>Smart Study Platform Team</p>
            </div>
          </body>
        </html>
        """
        
        msg.attach(MIMEText(message, 'plain'))
        msg.attach(MIMEText(html_message, 'html'))
        
        # Add PDF attachment if provided
        if pdf_path and os.path.exists(pdf_path):
            with open(pdf_path, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
            
            encoders.encode_base64(part)
            filename = os.path.basename(pdf_path)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename= {filename}',
            )
            msg.attach(part)
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

# Helper functions for user management
def create_user(username, password, email=None, role='student'):
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    try:
        # Try with all columns first
        cursor.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)", (username, password, email, role))
        conn.commit()
        conn.close()
        return True
    except sqlite3.OperationalError:
        # Fallback to basic columns only
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            conn.close()
            return False
    except sqlite3.IntegrityError:
        conn.close()
        return False

def get_user_role(username):
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT role FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else 'student'
    except sqlite3.OperationalError:
        # Role column doesn't exist, return default
        conn.close()
        return 'student'

def get_user_email(username):
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT email FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        conn.close()
        return result[0] if result else None
    except sqlite3.OperationalError:
        # Email column doesn't exist
        conn.close()
        return None

def verify_user(username, password):
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result and result[0] == password

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT DEFAULT 'student'
        )
    """)
    
    # Create materials table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            type TEXT NOT NULL,
            filename TEXT NOT NULL,
            uploaded_by TEXT NOT NULL,
            upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create simple leaderboard table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conn.commit()
    conn.close()
    print("Fresh database created successfully")

init_db()

# Create default accounts and sample data for testing
try:
    create_user('teacher', 'teacher123', 'teacher@example.com', 'teacher')
    print("Default teacher account created: teacher/teacher123")
except:
    print("Teacher account already exists or creation failed")

# Add sample leaderboard data
try:
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    
    # Check if leaderboard is empty
    cursor.execute("SELECT COUNT(*) FROM leaderboard")
    count = cursor.fetchone()[0]
    
    if count == 0:
        sample_scores = [
            ('Alex Johnson', 95),
            ('Sarah Chen', 92),
            ('Mike Davis', 88),
            ('Emma Wilson', 85),
            ('John Smith', 82)
        ]
        
        cursor.executemany("INSERT INTO leaderboard (name, score) VALUES (?, ?)", sample_scores)
        conn.commit()
        print("Sample leaderboard data added")
    
    conn.close()
except Exception as e:
    print(f"Error adding sample data: {e}")



@app.route("/")
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('platform'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if verify_user(username, password):
            session['username'] = username
            return redirect(url_for('platform'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route("/register", methods=['GET', 'POST'])
def register():
    error = None
    success = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form.get('email', '').strip()
        role = request.form.get('role', 'student')
        if len(username) < 3:
            error = 'Username must be at least 3 characters long.'
        elif len(password) < 6:
            error = 'Password must be at least 6 characters long.'
        elif create_user(username, password, email, role):
            success = 'Account created successfully! You can now login.'
        else:
            error = 'Username already exists. Please choose another.'
    return render_template('register.html', error=error, success=success)

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/leaderboard")
def leaderboard_page():
    if 'username' not in session:
        return redirect(url_for('login'))
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10")
    leaderboard = cursor.fetchall()
    conn.close()
    return render_template("leaderboard.html", leaderboard=leaderboard)

@app.route("/submit", methods=["POST"])
def submit():
    if 'username' not in session:
        return redirect(url_for('login'))
    name = request.form["username"]
    score = int(request.form["score"])

    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    
    # Insert into database (no rank column in new structure)
    cursor.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

    return f"Thanks {name}, your score of {score} has been saved!"

@app.route("/platform")
def platform():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("platform.html", username=session['username'])

@app.route("/search-materials")
def search_materials():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("search-materials.html")

@app.route("/exam-mode")
def exam_mode():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("exam-mode.html")

@app.route("/api/leaderboard")
def api_leaderboard():
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    
    # Get top 10 scores from leaderboard
    cursor.execute("SELECT name, score FROM leaderboard ORDER BY score DESC LIMIT 10")
    leaderboard = cursor.fetchall()
    conn.close()
    
    result = [{"name": row[0], "score": row[1], "average": row[1]} for row in leaderboard]
    print(f"Leaderboard API returning: {result}")
    return jsonify(result)

@app.route("/submit-exam", methods=["POST"])
def submit_exam():
    if 'username' not in session:
        return jsonify({"error": "Not logged in"}), 401
    data = request.get_json()
    name = data.get('name', 'Anonymous')
    score = data.get('score', 0)
    
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": f"Score {score} saved for {name}"})

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/view-pdf/<material_title>')
def view_pdf(material_title):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Check for uploaded materials first
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM materials WHERE title = ?", (material_title,))
    result = cursor.fetchone()
    conn.close()
    
    filename = None
    if result:
        filename = result[0]
    else:
        # Fallback to default materials
        pdf_path = PDF_MATERIALS.get(material_title)
        if pdf_path:
            filename = os.path.basename(pdf_path)
    
    if filename and os.path.exists(os.path.join('materials', filename)):
        pdf_url = f'/materials/{filename}'
        return render_template('pdf_viewer.html', 
                             material_title=material_title, 
                             pdf_url=pdf_url)
    else:
        return f"<h2>PDF not found for: {material_title}</h2><a href='/search-materials'>← Back to Materials</a>", 404

@app.route('/materials/<filename>')
def serve_material(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    return send_from_directory('materials', filename)

@app.route("/teacher-upload")
def teacher_upload():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    user_role = get_user_role(session['username'])
    if user_role != 'teacher':
        return render_template('access_denied.html', message="Only teachers can upload materials. Please register as a teacher.")
    
    return render_template("teacher_upload.html")

@app.route("/upload-material", methods=["POST"])
def upload_material():
    if 'username' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    user_role = get_user_role(session['username'])
    if user_role != 'teacher':
        return jsonify({"error": "Access denied. Only teachers can upload materials."}), 403
    
    try:
        title = request.form.get('title', '').strip()
        subject = request.form.get('subject', '').strip()
        material_type = request.form.get('type', '').strip()
        file = request.files.get('file')
        
        if not all([title, subject, material_type]):
            return jsonify({"error": "All fields are required"}), 400
        
        if not file or not file.filename:
            return jsonify({"error": "Please select a PDF file"}), 400
        
        # Create safe filename
        safe_title = ''.join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
        filename = f"{subject}_{safe_title.replace(' ', '_')}.pdf"
        filepath = os.path.join('materials', filename)
        
        # Save file
        file.save(filepath)
        
        # Save to database with error handling
        conn = sqlite3.connect('leaderboard.db')
        cursor = conn.cursor()
        
        # Check if materials table exists and create if not
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS materials (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                type TEXT NOT NULL,
                filename TEXT NOT NULL,
                uploaded_by TEXT NOT NULL,
                upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute(
            "INSERT INTO materials (title, subject, type, filename, uploaded_by) VALUES (?, ?, ?, ?, ?)",
            (title, subject, material_type, filename, session.get('username', 'unknown'))
        )
        conn.commit()
        conn.close()
        
        return jsonify({"success": True, "message": f"Material '{title}' uploaded successfully!"})
        
    except Exception as e:
        print(f"Upload error: {e}")
        return jsonify({"error": f"Upload failed: {str(e)}"}), 500

@app.route("/api/materials")
def api_materials():
    try:
        conn = sqlite3.connect('leaderboard.db')
        cursor = conn.cursor()
        
        # Check if table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='materials'")
        if not cursor.fetchone():
            conn.close()
            return jsonify([])
        
        cursor.execute("SELECT title, subject, type, filename FROM materials ORDER BY upload_date DESC")
        materials = cursor.fetchall()
        conn.close()
        
        return jsonify([{"title": row[0], "subject": row[1], "type": row[2], "filename": row[3]} for row in materials])
    except Exception as e:
        print(f"Materials API error: {e}")
        return jsonify([])

@app.route("/api/user-role")
def api_user_role():
    if 'username' not in session:
        return jsonify({"error": "Not logged in"}), 401
    role = get_user_role(session['username'])
    print(f"Debug: User {session['username']} has role: {role}")  # Debug log
    return jsonify({"role": role, "username": session['username']})

@app.route("/send-material", methods=["POST"])
def send_material():
    if 'username' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    data = request.get_json()
    material_title = data.get('title', 'Study Material')
    material_content = data.get('content', 'No content available')
    
    user_email = get_user_email(session['username'])
    if not user_email:
        return jsonify({
            "error": "No email address registered", 
            "message": "Please add your email in Profile settings to receive materials",
            "action": "profile"
        }), 400
    
    # Check for uploaded materials first
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM materials WHERE title = ?", (material_title,))
    result = cursor.fetchone()
    conn.close()
    
    pdf_path = None
    if result:
        pdf_path = os.path.join('materials', result[0])
    else:
        # Fallback to default materials
        pdf_path = PDF_MATERIALS.get(material_title)
    
    subject = f"📚 Study Material: {material_title}"
    if pdf_path and os.path.exists(pdf_path):
        message = f"Hello {session['username']},\n\nHere's your requested study material: {material_title}\n\n{material_content}\n\nPlease find the detailed PDF material attached to this email.\n\nBest regards,\nSmart Study Platform Team"
    else:
        message = f"Hello {session['username']},\n\nHere's your requested study material:\n\n{material_title}\n\n{material_content}\n\nBest regards,\nSmart Study Platform Team"
    
    if send_email(user_email, subject, message, pdf_path):
        return jsonify({"success": True, "message": f"Material sent to {user_email}!"})
    else:
        return jsonify({"error": "Failed to send email. Check Gmail configuration in app.py"}), 500

@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        
        conn = sqlite3.connect('leaderboard.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute("UPDATE users SET email = ? WHERE username = ?", (email, session['username']))
            conn.commit()
            conn.close()
            return jsonify({"success": True, "message": "Email updated successfully!"})
        except Exception as e:
            conn.close()
            return jsonify({"error": f"Failed to update email: {str(e)}"}), 500
    
    # GET request - show profile
    user_email = get_user_email(session['username'])
    user_role = get_user_role(session['username'])
    return render_template('profile.html', 
                         username=session['username'], 
                         email=user_email or '', 
                         role=user_role)

@app.route("/api/user-profile")
def api_user_profile():
    if 'username' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    user_email = get_user_email(session['username'])
    user_role = get_user_role(session['username'])
    
    return jsonify({
        "username": session['username'],
        "email": user_email,
        "role": user_role,
        "has_email": bool(user_email)
    })

@app.route("/api/quiz-questions")
def get_quiz_questions():
    try:
        with open('quizzes.json', 'r') as f:
            quiz_data = json.load(f)
        return jsonify(quiz_data['questions'])
    except Exception as e:
        return jsonify({"error": "Failed to load questions"}), 500

@app.route("/submit-exam-result", methods=["POST"])
def submit_exam_result():
    if 'username' not in session:
        return jsonify({"error": "Not logged in"}), 401
    
    data = request.get_json()
    student_name = data.get('student_name', session['username'])
    marks = int(data.get('marks', 0))
    total_marks = int(data.get('total_marks', 100))
    
    percentage = (marks / total_marks) * 100
    
    conn = sqlite3.connect('leaderboard.db')
    cursor = conn.cursor()
    
    # Insert exam score into leaderboard
    cursor.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (student_name, marks))
    
    conn.commit()
    conn.close()
    
    return jsonify({"success": True, "message": f"Score: {marks}/{total_marks} ({percentage:.1f}%) added to leaderboard!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
