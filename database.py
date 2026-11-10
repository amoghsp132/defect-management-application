"""
Database Layer for Defect Management Application (SQLite)
SDM College of Engineering & Technology, Dharwad
Author: Amogh S Patil (2SDS23CS011)
"""

import sqlite3
import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'defects.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create Defects Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS defects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        defect_code TEXT UNIQUE,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        steps_to_reproduce TEXT,
        expected_behavior TEXT,
        actual_behavior TEXT,
        module TEXT NOT NULL,
        type TEXT NOT NULL,
        severity TEXT NOT NULL,
        priority TEXT NOT NULL,
        discovery_phase TEXT NOT NULL,
        environment TEXT NOT NULL,
        status TEXT NOT NULL,
        reporter TEXT NOT NULL,
        assignee TEXT DEFAULT 'Unassigned',
        prevention_guideline TEXT,
        resolution_notes TEXT,
        created_at TEXT NOT NULL,
        updated_at TEXT NOT NULL
    )
    ''')

    # Create Prevention Guidelines & RCA Knowledge Base Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prevention_guidelines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        module TEXT NOT NULL,
        category TEXT NOT NULL,
        guideline TEXT NOT NULL,
        root_cause_pattern TEXT NOT NULL,
        added_by TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    ''')

    conn.commit()

    # Seed initial realistic data if table is empty
    cursor.execute('SELECT COUNT(*) as count FROM defects')
    count = cursor.fetchone()['count']
    if count == 0:
        seed_data(cursor)
        conn.commit()

    conn.close()

def seed_data(cursor):
    today = datetime.date.today().isoformat()
    yesterday = (datetime.date.today() - datetime.timedelta(days=2)).isoformat()
    past_week = (datetime.date.today() - datetime.timedelta(days=6)).isoformat()

    initial_defects = [
        (
            "DEF-101",
            "Payment Gateway Timeout during UPI Checkout",
            "When user confirms high-volume UPI transaction, backend gateway hangs without sending callback ACK.",
            "1. Add item to cart\n2. Proceed to checkout\n3. Select UPI Payment\n4. Observe spinner infinite loop",
            "Gateway should return SUCCESS or FAILURE with transaction reference ID within 5 seconds.",
            "Spinner spins indefinitely; session times out without saving transaction record.",
            "Payments",
            "Backend/API",
            "Critical",
            "P1 (High)",
            "System Testing",
            "Staging / QA",
            "In Progress",
            "Amogh Patil (QA Lead)",
            "Karthik (Backend Eng)",
            "Implement resilient circuit breaker and 5-second socket read timeout with asynchronous webhook verification.",
            "Investigating third-party sandbox latency and adding fallback polling.",
            past_week,
            yesterday
        ),
        (
            "DEF-102",
            "JWT Token Not Invalidated on User Logout",
            "Revoked tokens remain valid until expiration timestamp, allowing unauthorized session reuse.",
            "1. Login as user\n2. Copy Bearer token\n3. Click Logout\n4. Send GET /api/user with old token",
            "Server must reject revoked token with HTTP 401 Unauthorized.",
            "Server responds with HTTP 200 OK and confidential user profile data.",
            "Authentication",
            "Security",
            "Blocker",
            "P1 (High)",
            "Security Audit",
            "Pre-Production",
            "Assigned",
            "Rohan (Security Auditor)",
            "Priya (Auth Team)",
            "Maintain an in-memory Redis blacklist or use short-lived access tokens with rotating refresh tokens.",
            "Assigned to sprint 14 auth security patch.",
            past_week,
            today
        ),
        (
            "DEF-103",
            "Cart Pricing Discrepancy with Tiered Quantity Discounts",
            "Bulk purchase calculation applies 20% discount twice when coupon code is also applied.",
            "1. Add 10 units of Item A\n2. Bulk tier discount applies\n3. Enter promo coupon FESTIVE10\n4. Observe total",
            "Final total should reflect combined discount capped at maximum 25%.",
            "Discounts compound multiplicatively, resulting in negative subtotal.",
            "Cart & Checkout",
            "Business Logic",
            "Major",
            "P2 (Medium)",
            "Integration Testing",
            "Development",
            "Resolved",
            "Sneha (QA Analyst)",
            "Amogh Patil (Dev)",
            "Enforce strict discount cap validators in cart calculation pipeline before checkout commit.",
            "Applied maximum clamp limit at line 84 of pricing_service.py. Verified by automated tests.",
            yesterday,
            today
        ),
        (
            "DEF-104",
            "Inventory Stock Count Becomes Negative Under Concurrent Orders",
            "Simultaneous order placement for the last item reduces available stock below zero.",
            "1. Set item stock to 1\n2. Run 5 concurrent checkout threads\n3. Inspect inventory balance in DB",
            "Only 1 transaction should succeed; remaining 4 must fail with Out of Stock.",
            "Stock balance recorded as -4 in database.",
            "Inventory",
            "Database",
            "Critical",
            "P1 (High)",
            "Load & Concurrency Testing",
            "Staging / QA",
            "Verified",
            "Vikram (Performance QA)",
            "Deepak (DBA)",
            "Implement row-level database locking (SELECT ... FOR UPDATE) or atomic conditional decrement.",
            "Added atomic DB constraint: CHECK (stock_quantity >= 0). Regression verified.",
            past_week,
            yesterday
        ),
        (
            "DEF-105",
            "Responsive Navigation Bar Overlaps Header on Mobile Displays",
            "Hamburger navigation menu covers top-level banner text on screen widths under 576px.",
            "1. Resize browser to 400px width\n2. Expand navigation menu\n3. Header text overlaps navigation drawer",
            "Menu drawer should collapse properly and slide over z-indexed overlay.",
            "Text layers collide and navigation links cannot be clicked.",
            "UI/Frontend",
            "UI/UX",
            "Minor",
            "P3 (Low)",
            "Cross-Device Testing",
            "QA Staging",
            "Closed",
            "Ananya (UI Tester)",
            "Amogh Patil (Frontend)",
            "Add mobile-first media queries and CSS z-index stacking context checks in design system.",
            "Updated CSS z-index and added Bootstrap 5 offcanvas component. Closed after QA review.",
            past_week,
            past_week
        ),
        (
            "DEF-106",
            "SMS OTP Delivery Fails Due to International Phone Format",
            "Users entering international prefix (+91 or +1) without hyphen receive generic server error.",
            "1. Navigate to Sign Up\n2. Enter phone +919876543210\n3. Click Send OTP\n4. Observe 500 error",
            "System should normalize phone string to E.164 format and transmit OTP.",
            "Regex fails validation and uncaught exception triggers 500 Internal Server Error.",
            "Notification Service",
            "Functional Bug",
            "Major",
            "P2 (Medium)",
            "User Acceptance Testing (UAT)",
            "QA Staging",
            "New",
            "Manoj (Product Manager)",
            "Unassigned",
            "Utilize standardized phonenumbers library and sanitize all telephone inputs prior to API dispatch.",
            "",
            today,
            today
        )
    ]

    cursor.executemany('''
    INSERT INTO defects (
        defect_code, title, description, steps_to_reproduce, expected_behavior, actual_behavior,
        module, type, severity, priority, discovery_phase, environment, status,
        reporter, assignee, prevention_guideline, resolution_notes, created_at, updated_at
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', initial_defects)

    initial_prevention = [
        ("Payments", "Architecture & Resilience", "Implement idempotent transaction keys and circuit breaker patterns to prevent payment double-charging.", "Third-party network timeouts without retry boundaries.", "Amogh Patil", past_week),
        ("Authentication", "Security Standards", "Always use short-lived access tokens with cryptographic rotation. Never store plaintext tokens or passwords.", "Improper token revocation during session termination.", "Amogh Patil", past_week),
        ("Inventory", "Database Concurrency", "Enforce atomic database updates and row-level locking for inventory balances to prevent race conditions.", "Unconstrained concurrent reads before write operations.", "Deepak DBA", past_week),
        ("Cart & Checkout", "Defensive Programming", "Validate discount totals against strict business threshold ceilings before committing checkout transactions.", "Compound discount calculation omitting boundary checks.", "Sneha QA", past_week)
    ]

    cursor.executemany('''
    INSERT INTO prevention_guidelines (
        module, category, guideline, root_cause_pattern, added_by, created_at
    ) VALUES (?, ?, ?, ?, ?, ?)
    ''', initial_prevention)
