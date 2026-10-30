# 🚀 DevConnect – Developer Collaboration Platform

**Connect. Collaborate. Build.**

DevConnect is a web-based developer collaboration platform that helps developers discover projects, connect with like-minded people, and build teams based on their technical skills and interests.

The platform provides a centralized space where developers can create projects, apply to join teams, communicate with team members, and collaborate on development ideas.

## ✨ Key Features

### 👤 User Authentication & Profiles
- User registration and login.
- Developer profiles with bio, college and technical skills.
- GitHub and LinkedIn profile links.
- Resume upload and profile management.

### 💻 Project Management
- Create and publish development projects.
- Specify required skills, experience level and team size.
- Browse and search available projects.
- Edit and manage created projects.

### 🤝 Team Formation
- Apply to join projects.
- Project owners can accept or reject applications.
- Team formation based on accepted applications.
- Project status management.

### 💬 Real-Time-Style Team Chat
- Dedicated project team chat.
- Text messaging.
- Image, file and voice-note attachments.
- Reply, edit and delete messages.
- Emoji reactions.

### 🔔 Notifications
- Notifications for application updates.
- Updates when project requests are accepted or rejected.

### ⭐ Additional Features
- Save interesting projects.
- Skill-based project recommendations.
- Developer compatibility matching.
- Resume-based skill extraction.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript |
| Styling | Tailwind CSS |
| Database | SQLite |
| Version Control | Git, GitHub |
| Additional Tools | PDFPlumber |

## 📂 Project Structure

```text
DevConnect/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── forms.py
│
├── projects/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── urls.py
│
├── devconnect/
│   ├── settings.py
│   └── urls.py
│
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Anshika-techie/DevConnect.git
cd DevConnect
```

### 2. Create a virtual environment

```bash
python -m venv env
```

Activate it:

**Mac/Linux**
```bash
source env/bin/activate
```

**Windows**
```bash
env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Set a secure Django secret key before running the application.

```bash
export DJANGO_SECRET_KEY="your-secret-key"
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

Open in your browser:

http://127.0.0.1:8000/

## 🎯 Project Objective

The objective of DevConnect is to simplify developer collaboration by bringing project discovery, team formation, skill matching and team communication into one platform.

It aims to help developers move from individual project ideas to collaborative development.

## 👩‍💻 Developer

**Anshika Srivastava**

B.Tech – Computer Science & Engineering

Graphic Era Deemed To Be University

GitHub: https://github.com/Anshika-techie

---

⭐ If you find this project interesting, feel free to explore the repository!
