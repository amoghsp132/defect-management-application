# Web-Based Defect Management Application (Python Edition)

**Institution:** S D M College of Engineering & Technology, Dharwad (SDMCET)  
**Department:** Department of Computer Science & Engineering  
**Course:** Software Testing (22UCSES731) - VII Semester  
**Student Name:** Amogh S Patil  
**USN:** 2SDS23CS011  
**Academic Year:** 2026-27  

---

## 🎯 Project Overview

This project is a full-stack, enterprise-grade **Defect Management Application** developed in **Python (Flask)** with **SQLite** database persistence and designed for cloud deployment on **Render**.

It is built specifically to address:
1. **Curriculum Section 1.9 (Defect Management):** Direct and comprehensive implementation of the 6 essential subprocesses:
   - **Subprocess 1: Defect Prevention:** Root Cause Analysis (RCA), prevention checklists, and shared knowledge base.
   - **Subprocess 2: Defect Discovery:** Tagging test stages (Unit, Integration, System, UAT, Security) and test environments.
   - **Subprocess 3: Defect Recording & Reporting:** Comprehensive defect logging with Bugzilla / FogBugz attributes and CSV exports.
   - **Subprocess 4: Defect Classification:** Multi-dimensional categorization by Severity, Priority, Type, and Functional Module.
   - **Subprocess 5: Defect Resolution:** Complete 6-phase defect lifecycle (`New` ➔ `Assigned` ➔ `In Progress` ➔ `Resolved` ➔ `Verified` ➔ `Closed`).
   - **Subprocess 6: Defect Prediction:** Module defect density forecasting, weighted severity scoring, and high-risk alerts.
2. **Slide Reference (Defect Tools):** Bugzilla (open-source) and FogBugz (commercial) architecture compatibility, including complexity-based defect prediction.

---

## 🛠️ Tech Stack

- **Backend Framework:** Python 3, Flask, Gunicorn
- **Database:** SQLite with pre-seeded enterprise defects and automated schema migration
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5.3, FontAwesome 6
- **Data Visualization:** Chart.js (Severity Doughnut, Lifecycle Bar Chart, Discovery Polar Area)
- **Deployment Platform:** Render (Free Web Service tier)

---

## 🚀 Local Installation & Execution

### Prerequisites
- Python 3.10+ installed.

### Steps
1. Navigate to the project directory:
   ```bash
   cd Project_2_Defect_Management_Application
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5001
   ```

---

## 🌐 Cloud Deployment on Render

This project includes `Procfile`, `runtime.txt`, `render.yaml`, and `requirements.txt` for 1-click deployment on Render:
1. Push this directory to your GitHub account.
2. Log in to [Render](https://render.com) and create a **New Web Service**.
3. Link your repository.
4. Render auto-configures:
   - **Environment:** `Python`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
5. Click **Deploy**. Your live service will be accessible globally.
