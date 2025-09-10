# Smart Study Material Access Platform

A comprehensive web-based learning platform built with Flask that provides study materials, online exams, and performance tracking.

## 🚀 Features

### 📚 Study Materials
- **Search & Access** - Find study materials by subject and type
- **PDF Viewer** - View materials directly in browser
- **Email Delivery** - Send materials to your email with PDF attachments
- **Teacher Upload** - Teachers can upload new study materials

### 🎯 Online Exams
- **Interactive Quiz** - 10 multiple-choice questions
- **Timer System** - 30-minute time limit
- **Real-time Navigation** - Jump between questions
- **Automatic Scoring** - Accurate grade calculation

### 🏆 Leaderboard System
- **Performance Tracking** - View top performers
- **Real-time Updates** - Scores update after each exam
- **Database Integration** - Persistent score storage

### 👤 User Management
- **Role-based Access** - Student and Teacher accounts
- **Profile Management** - Update email preferences
- **Session Management** - Secure login/logout

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Email**: Gmail SMTP
- **Styling**: Custom CSS with animations

## 📦 Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd database
```

2. **Install dependencies**
```bash
pip install flask
```

3. **Configure email (optional)**
   - Update `EMAIL_ADDRESS` and `EMAIL_PASSWORD` in `app.py`
   - Use Gmail App Password for authentication

4. **Run the application**
```bash
python3 app.py
```

5. **Access the platform**
   - Open browser: `http://127.0.0.1:5000`

## 🎮 Usage

### For Students
1. **Register/Login** - Create account or use existing credentials
2. **Search Materials** - Browse and access study content
3. **Take Exams** - Complete 10-question quizzes
4. **View Leaderboard** - Check your ranking
5. **Email Materials** - Send PDFs to your email

### For Teachers
1. **Login as Teacher** - Use teacher credentials
2. **Upload Materials** - Add new study content
3. **Manage Content** - View uploaded materials

### Default Accounts
- **Teacher**: `teacher` / `teacher123`
- **Student**: Register new account

## 📁 Project Structure

```
database/
├── app.py                 # Main Flask application
├── quizzes.json          # Exam questions database
├── exam_database.sql     # Database schema
├── templates/            # HTML templates
│   ├── login.html
│   ├── platform.html
│   ├── exam-mode.html
│   └── ...
├── static/              # CSS and assets
│   ├── styles.css
│   └── animations.css
└── materials/           # Uploaded study materials
```

## 🗄️ Database Schema

### Tables
- **users** - User accounts and roles
- **students** - Student information
- **exams** - Exam metadata
- **exam_results** - Individual exam scores
- **leaderboard** - Performance rankings
- **materials** - Uploaded study content

## 🔧 Configuration

### Email Setup
```python
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_app_password'
```

### Quiz Questions
Edit `quizzes.json` to customize exam questions:
```json
{
  "questions": [
    {
      "id": 1,
      "question": "Your question here?",
      "options": ["A", "B", "C", "D"],
      "correct": 1,
      "subject": "Subject"
    }
  ]
}
```

## 🎯 API Endpoints

- `GET /` - Login page
- `GET /platform` - Main dashboard
- `GET /exam-mode` - Exam interface
- `POST /submit-exam-result` - Submit exam scores
- `GET /api/leaderboard` - Get rankings
- `GET /api/quiz-questions` - Get exam questions
- `POST /send-material` - Email materials

## 🚀 Features in Detail

### Exam System
- Dynamic question loading from JSON
- Answer persistence during navigation
- Automatic time management
- Real scoring based on correct answers

### Email Integration
- Gmail SMTP configuration
- PDF attachment support
- Professional email formatting
- Error handling and user feedback

### Leaderboard
- Real-time score updates
- Percentage-based ranking
- Database persistence
- Clean display interface

## 🔒 Security Features

- Session-based authentication
- Role-based access control
- Input validation
- Secure file uploads

## 📱 Responsive Design

- Mobile-friendly interface
- Smooth animations
- Clean, modern UI
- Intuitive navigation

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues or questions:
1. Check existing documentation
2. Review code comments
3. Test with default accounts
4. Verify email configuration

---

**Built with ❤️ for education and learning by shayak and team**
