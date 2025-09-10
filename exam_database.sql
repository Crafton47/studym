-- Exam and Leaderboard Database Schema

-- Students table
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    student_id TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exams table
CREATE TABLE IF NOT EXISTS exams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exam_name TEXT NOT NULL,
    subject TEXT NOT NULL,
    total_marks INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exam results table
CREATE TABLE IF NOT EXISTS exam_results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    exam_id INTEGER,
    marks_obtained INTEGER NOT NULL,
    percentage REAL NOT NULL,
    grade TEXT,
    exam_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (exam_id) REFERENCES exams (id)
);

-- Leaderboard view (automatically updated from exam results)
CREATE TABLE IF NOT EXISTS leaderboard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    total_score INTEGER NOT NULL,
    average_percentage REAL NOT NULL,
    exams_taken INTEGER NOT NULL,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample students
INSERT OR REPLACE INTO students (id, name, email, student_id) VALUES 
(1, 'Alex Johnson', 'alex@example.com', 'STU001'),
(2, 'Sarah Chen', 'sarah@example.com', 'STU002'),
(3, 'Mike Davis', 'mike@example.com', 'STU003'),
(4, 'Emma Wilson', 'emma@example.com', 'STU004'),
(5, 'John Smith', 'john@example.com', 'STU005');

-- Insert sample exams
INSERT OR REPLACE INTO exams (id, exam_name, subject, total_marks) VALUES 
(1, 'Mathematics Quiz 1', 'Mathematics', 100),
(2, 'Physics Test', 'Physics', 100),
(3, 'Chemistry Lab Exam', 'Chemistry', 100);

-- Insert sample exam results
INSERT OR REPLACE INTO exam_results (student_id, exam_id, marks_obtained, percentage, grade) VALUES 
(1, 1, 95, 95.0, 'A+'),
(2, 1, 92, 92.0, 'A'),
(3, 1, 88, 88.0, 'B+'),
(4, 1, 85, 85.0, 'B'),
(5, 1, 82, 82.0, 'B'),
(1, 2, 90, 90.0, 'A'),
(2, 2, 94, 94.0, 'A+'),
(3, 2, 86, 86.0, 'B+');

-- Update leaderboard with calculated scores
INSERT OR REPLACE INTO leaderboard (id, student_name, total_score, average_percentage, exams_taken) VALUES 
(1, 'Alex Johnson', 95, 95.0, 2),
(2, 'Sarah Chen', 93, 93.0, 2),
(3, 'Mike Davis', 87, 87.0, 2),
(4, 'Emma Wilson', 85, 85.0, 1),
(5, 'John Smith', 82, 82.0, 1);