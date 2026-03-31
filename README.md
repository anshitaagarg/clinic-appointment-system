# 🏥 Clinic Appointment & Token Management System
A web-based system to manage clinic appointments, generate tokens, and display real-time patient queues.
---
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![Database](https://img.shields.io/badge/Database-SQLite-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Repo Size](https://img.shields.io/github/repo-size/anshitaagarg/clinic-appointment-system)
![Last Commit](https://img.shields.io/github/last-commit/anshitaagarg/clinic-appointment-system)
![Stars](https://img.shields.io/github/stars/anshitaagarg/clinic-appointment-system?style=social)

---

## 🏗️ System Architecture

The project follows the MVC (Model-View-Controller) architecture:

- Models: Handle database structure (Patient, Doctor, Appointment, Token)
- Views: Business logic and request handling
- Templates: User interface rendering

## 🔁 Workflow

1. Patient registers
2. Books appointment
3. System checks doctor availability
4. Appointment is created
5. Token is automatically generated
6. Queue is updated and displayed

## 🧪 Testing

- Appointment creation tested
- Token generation verified (FIFO logic)
- Queue display validated
- Reports checked for accuracy

## 🚀 Features

- 👤 Patient Registration & Management  
- 👨‍⚕️ Doctor Scheduling & Availability  
- 📅 Appointment Booking  
- 🎟️ Automatic Token Generation (FIFO)  
- 📺 Real-Time Queue Display  
- 🔔 Notifications (Mock SMS/Email)  
- 📊 Reports Dashboard (Daily & Doctor-wise)
- Automatic token generation using FIFO logic
- Real-time queue display
- Integrated reporting system
---

## 🛠️ Tech Stack

- Backend: Django (Python)  
- Frontend: HTML, CSS  
- Database: SQLite  
- Tools: VS Code  
---

## 📊 Sample Output

The system displays:
- Current token being served
- Waiting queue list
- Doctor-wise patient analytics

## ⚠️ Challenges Faced

- Managing token generation logic correctly
- Handling template rendering issues
- Integrating different modules smoothly

## 🚧 Limitations

- Notifications are mock (not real SMS/Email)
- No user authentication system yet

## ⚙️ How to Run

```bash
# Activate virtual environment
venv\Scripts\activate

# Go to project folder
cd clinic_system

# Run server
python manage.py runserver
```
