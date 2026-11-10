# BugVortex — Web-Based Defect Management Application (Python Edition)

**System Name:** BugVortex  
**Category:** Intelligent Defect Lifecycle & Quality Assurance Platform  
**Academic Module:** Software Testing (VII Semester)  

---

## 🎯 Project Overview

**BugVortex** is a full-stack, enterprise-grade **Defect Management Application** developed in **Python (Flask)** with **SQLite** database persistence and a modern **Google Material Design** web interface.

It is engineered specifically to implement:
1. **Curriculum Section 1.9 (Defect Management):** Direct and comprehensive implementation of the 6 essential subprocesses:
   - **Subprocess 1: Defect Prevention:** Root Cause Analysis (RCA), prevention checklists, and shared knowledge base.
   - **Subprocess 2: Defect Discovery:** Tagging test stages (Unit, Integration, System, UAT, Security) and test environments.
   - **Subprocess 3: Defect Recording & Reporting:** Comprehensive defect logging with Bugzilla / FogBugz attributes and CSV exports.
   - **Subprocess 4: Defect Classification:** Multi-dimensional categorization by Severity, Priority, Type, and Functional Module.
   - **Subprocess 5: Defect Resolution:** Complete 6-phase defect lifecycle (`New` $\rightarrow$ `Assigned` $\rightarrow$ `In Progress` $\rightarrow$ `Resolved` $\rightarrow$ `Verified` $\rightarrow$ `Closed`).
   - **Subprocess 6: Defect Prediction:** Module defect density forecasting, weighted severity scoring, and high-risk alerts.
2. **Slide Reference (Defect Tools):** Bugzilla (open-source) and FogBugz (commercial) architecture compatibility, including complexity-based defect prediction.

---

## 🎨 Material Design Interface

Designed following **Google Material Design 3 (M3)** standards:
- **Material Top App Bar:** Clean product header with quick CSV export and refresh actions.
- **Material Metric Cards:** Summary metric tiles for Total Defects, Open/Active, Resolved, and High-Risk Module.
- **Predictive Quality Alert Banner:** Highlights high-risk modules requiring additional regression testing.
- **Visual Analytics:** Chart.js Doughnut (Severity), Bar (Lifecycle Status), and Polar Area (Discovery Phase).
- **Material Tabs:** Seamless navigation across the 4 primary workflows (Tracker, Logging, Prevention, Prediction).

---

## 🛠️ Local Installation & Execution

```bash
cd Project_2_Defect_Management_Application
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```
Open **`http://127.0.0.1:5001`** in your browser.
