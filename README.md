# 🚀 Focus Tracker Pro

> A full-stack web application to help you manage and track your focus tasks efficiently. Built as my first capstone project during my internship journey.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![SQLite](https://img.shields.io/badge/SQLite-Database-yellow.svg)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)

## 📖 About This Project

**Focus Tracker Pro** is my first full-stack capstone project during my internship. It demonstrates how frontend, backend, and database layers work together to create a complete web application.

The app includes user authentication with secure passwords, a clean dashboard, and task management features—all built from scratch to learn full-stack development fundamentals.

## ✨ Features

### 🔐 Authentication
- **User Registration**: Create a new account with secure password hashing
- **User Login**: Secure login system with session management
- **Password Security**: Passwords are hashed using industry-standard werkzeug security
- **Session Management**: Persistent sessions to keep users logged in

### 📝 Task Management
- **Add Focus Entries**: Create and save your focus tasks/goals
- **View All Tasks**: Display all your saved tasks in a clean table format
- **Delete Tasks**: Remove completed or unnecessary tasks with one click
- **Real-time Updates**: Instant feedback when adding or deleting tasks

### 🎨 User Interface
- **Modern Design**: Glassmorphism UI with gradient backgrounds
- **Responsive Layout**: Works seamlessly on desktop, tablet, and mobile devices
- **Bootstrap Integration**: Beautiful, professional UI components
- **Smooth Navigation**: Intuitive navigation between login, register, and dashboard

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Flask (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 5.3 |
| **Database** | SQLite3 |
| **Security** | Werkzeug (password hashing) |
| **Font** | Google Fonts (Poppins) |
| **Styling** | Custom CSS + Bootstrap |

## 📋 Project Structure

```
focus-tracker/
│
├── app.py                      # Main Flask application
├── focus.db                    # SQLite database (auto-generated)
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
├── README.md                   # This file
│
└── templates/
    ├── index.html             # Dashboard/Home page
    ├── login.html             # Login page
    └── register.html          # Registration page
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR-USERNAME/focus-tracker.git
   cd focus-tracker
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📖 How to Use

### First Time Users

1. **Register an Account**
   - Click "Create new account" on the login page
   - Enter a username and password
   - Submit to create your account

2. **Login**
   - Return to the login page
   - Enter your credentials
   - Click "Login" to access the dashboard

### Using the Application

1. **Add Focus Entry**
   - Enter your task/goal in the input field
   - Click the "Save" button
   - Your entry is saved and displayed in the table

2. **View Entries**
   - All your saved tasks appear in the "Your Saved Entries" table
   - Each entry shows the ID and task name

3. **Delete Entry**
   - Click the "Delete" button next to any task
   - The task is removed immediately

4. **Logout**
   - Click the "Logout" button in the navigation bar
   - You'll be returned to the login page

## 🔑 Test Credentials

For testing purposes, you can use these credentials after registration:

| Username | Password |
|----------|----------|
| john | password123 |
| alice | secure123 |
| testuser | test1234 |

> **Note**: You need to register first. The above are just examples of what you can use.

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
);
```

### Data Table
```sql
CREATE TABLE data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);
```

## 🔒 Security Features

- ✅ Secure password hashing with werkzeug
- ✅ SQL injection prevention with parameterized queries
- ✅ Session-based authentication
- ✅ User data isolation
- ✅ CSRF protection via Flask

## 📱 Screenshots

### Dashboard - Add & Manage Tasks
![Dashboard](./screenshots/dashboard.png)

### Login Page
![Login](./screenshots/login.png)

### Registration Page
![Register](./screenshots/register.png)

## 🎓 Learning Outcomes

✅ Building REST routes and handling HTTP requests  
✅ Creating responsive, user-friendly interfaces  
✅ Database design and query optimization  
✅ Secure password hashing and user authentication  
✅ Connecting all layers: frontend ↔ backend ↔ database  
✅ Deploying and managing a complete web application

## 🚧 Future Enhancements

Potential features for future versions:

- [ ] Task editing functionality
- [ ] Task categories/tags
- [ ] Priority levels for tasks
- [ ] Due dates and reminders
- [ ] Task completion status
- [ ] User profile page
- [ ] Dark mode toggle
- [ ] Task search functionality
- [ ] Export/import tasks
- [ ] Email notifications

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **� Author

**Shreyankyah**  
- 🔗 GitHub: [@Shreyankyah](https://github.com/Shreyankyah)
- 📧 Email: shreyankyah@example.com

## 🎯 Key Takeaway

Building this project taught me that full-stack development is about connecting all the pieces—from database design to UI/UX. It's a practical lesson in how the web actually works

**⭐ If you found this project helpful or interesting, please consider giving it a star!**

Made with ❤️ during my internship journey
