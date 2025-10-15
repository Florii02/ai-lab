# ============================================================================
# 24. SCHEDULING & TIME AUTOMATION
# ============================================================================
# WHAT: Schedule tasks, delays, and time-based automation
# WHY: Run tasks at specific times, automate recurring jobs, control timing
# WHEN: Daily reports, periodic checks, delayed actions, cron-like tasks
# NOTE: Uses time (built-in) and schedule (pip install schedule)

print("="*60)
print("SCHEDULING & TIME AUTOMATION")
print("="*60)

# ============================================================================
# TIME MODULE (BUILT-IN)
# ============================================================================

print("\n" + "="*60)
print("TIME MODULE - DELAYS & TIMING")
print("="*60)

import time
from datetime import datetime

print("""
💡 Time Module Basics:
- Add delays between operations
- Measure execution time
- Control automation flow
- Built-in (no installation needed)
""")

print("\n1. DELAYS WITH time.sleep():")
print("""
import time

print("Task starting...")
time.sleep(2)  # Wait 2 seconds
print("Task completed after 2 seconds")

# Use cases:
- Rate limiting (API calls)
- Polling intervals
- User-friendly pacing
- Retry delays
""")

# Demo: Simple countdown
print("\n2. COUNTDOWN TIMER:")
for i in range(3, 0, -1):
    print(f"  {i}...")
    time.sleep(1)
print("  Go! ✓")

# Measuring execution time
print("\n3. MEASURE EXECUTION TIME:")
start = time.time()
# Simulate work
time.sleep(0.5)
end = time.time()
print(f"  Execution time: {end - start:.2f} seconds")

print("""
# Better timing with timeit module
from timeit import timeit

execution_time = timeit('sum(range(1000))', number=10000)
print(f"Average time: {execution_time} seconds")
""")

# ============================================================================
# DATETIME MODULE (BUILT-IN)
# ============================================================================

print("\n" + "="*60)
print("DATETIME MODULE - DATE & TIME HANDLING")
print("="*60)

from datetime import datetime, timedelta

print("\n1. CURRENT DATE & TIME:")
now = datetime.now()
print(f"  Current datetime: {now}")
print(f"  Date: {now.strftime('%Y-%m-%d')}")
print(f"  Time: {now.strftime('%H:%M:%S')}")

print("\n2. DATE ARITHMETIC:")
tomorrow = datetime.now() + timedelta(days=1)
next_week = datetime.now() + timedelta(weeks=1)
print(f"  Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print(f"  Next week: {next_week.strftime('%Y-%m-%d')}")

print("\n3. CHECK TIME RANGES:")
current_hour = datetime.now().hour
if 9 <= current_hour < 17:
    print("  ✓ Business hours (9am-5pm)")
else:
    print("  ✗ Outside business hours")

print("""
# Practical example: Check if weekend
import datetime

today = datetime.datetime.now()
if today.weekday() >= 5:  # 5=Saturday, 6=Sunday
    print("It's the weekend!")
else:
    print("It's a weekday")
""")

# ============================================================================
# SCHEDULE MODULE - TASK SCHEDULING
# ============================================================================

print("\n" + "="*60)
print("SCHEDULE MODULE - CRON-LIKE SCHEDULING")
print("="*60)

print("""
💡 Why Use Schedule Module?
- Run tasks at specific times
- Recurring jobs (daily, hourly, etc.)
- Simpler than cron
- Cross-platform

Install: pip install schedule
""")

print("\n1. BASIC SCHEDULING:")
print("""
import schedule
import time

def job():
    print("Task executed!")

# Schedule jobs
schedule.every(10).seconds.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every().monday.do(job)

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
""")

print("\n2. SCHEDULING EXAMPLES:")
print("""
# Every 30 minutes
schedule.every(30).minutes.do(job)

# Daily at specific time
schedule.every().day.at("09:00").do(send_report)

# Every Monday at 8am
schedule.every().monday.at("08:00").do(weekly_backup)

# Every hour on the hour
schedule.every().hour.at(":00").do(check_status)

# Every 5 hours
schedule.every(5).hours.do(sync_data)
""")

print("\n3. SCHEDULING WITH PARAMETERS:")
print("""
def greet(name):
    print(f"Hello, {name}!")

# Pass parameters
schedule.every().day.at("09:00").do(greet, name="Alice")
""")

# ============================================================================
# PRACTICAL AUTOMATION EXAMPLES
# ============================================================================

print("\n" + "="*60)
print("PRACTICAL AUTOMATION EXAMPLES")
print("="*60)

print("""
💡 Real-World Use Cases (FROM ATBS):

1. Daily Report Generator
   - Schedule: Every day at 9am
   - Action: Fetch data, generate report, email it

   def daily_report():
       data = fetch_data()
       create_report(data)
       email_report("manager@company.com")

   schedule.every().day.at("09:00").do(daily_report)

2. Website Monitoring
   - Schedule: Every 5 minutes
   - Action: Check if website is up, alert if down

   def check_website():
       response = requests.get("https://example.com")
       if response.status_code != 200:
           send_alert("Website is down!")

   schedule.every(5).minutes.do(check_website)

3. Database Backup
   - Schedule: Every night at 2am
   - Action: Backup database to cloud

   def backup_database():
       os.system("pg_dump mydb > backup.sql")
       upload_to_s3("backup.sql")

   schedule.every().day.at("02:00").do(backup_database)

4. Price Scraper
   - Schedule: Every 6 hours
   - Action: Scrape prices, compare, alert if changed

   def scrape_prices():
       price = scrape_product_price()
       if price < threshold:
           send_sms(f"Price dropped to ${price}!")

   schedule.every(6).hours.do(scrape_prices)

5. Social Media Poster
   - Schedule: Specific times
   - Action: Post scheduled content

   schedule.every().day.at("10:00").do(post_to_twitter)
   schedule.every().day.at("14:00").do(post_to_linkedin)
   schedule.every().day.at("18:00").do(post_to_instagram)

6. Log Cleanup
   - Schedule: Weekly on Sunday
   - Action: Delete old log files

   def cleanup_logs():
       for file in Path("logs").glob("*.log"):
           if file.stat().st_mtime < (time.time() - 30*24*3600):
               file.unlink()

   schedule.every().sunday.at("03:00").do(cleanup_logs)
""")

# ============================================================================
# COMPLETE EXAMPLE: SCHEDULED REPORT
# ============================================================================

print("\n" + "="*60)
print("COMPLETE EXAMPLE: SCHEDULED DAILY REPORT")
print("="*60)

print("""
import schedule
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def fetch_daily_metrics():
    # Simulate fetching data
    return {
        "sales": 1234,
        "users": 567,
        "revenue": 8900
    }

def send_daily_report():
    print(f"[{datetime.now()}] Generating daily report...")

    # Get data
    metrics = fetch_daily_metrics()

    # Create email
    body = f\"\"\"
    Daily Report - {datetime.now().strftime('%Y-%m-%d')}

    Sales: {metrics['sales']}
    New Users: {metrics['users']}
    Revenue: ${metrics['revenue']}

    Automated Report System
    \"\"\"

    # Send email (simplified)
    # send_email(to="manager@company.com", subject="Daily Report", body=body)
    print("✓ Report sent!")

# Schedule the job
schedule.every().day.at("09:00").do(send_daily_report)

# Keep the script running
print("Scheduler started. Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute
""")

# ============================================================================
# ADVANCED: APScheduler
# ============================================================================

print("\n" + "="*60)
print("ADVANCED: APSCHEDULER")
print("="*60)

print("""
For production use, consider APScheduler:
- More robust than schedule
- Persistent job storage
- Multiple job stores
- Better for long-running apps

Install: pip install apscheduler

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', hours=1)
def job_function():
    print(f"Job executed at {datetime.now()}")

@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=9)
def weekday_job():
    print("Weekday morning task")

scheduler.start()

Features:
- Interval triggers (every X seconds/minutes/hours)
- Cron-style triggers (specific times)
- Date triggers (one-time execution)
- Job persistence (survive restarts)
- Multiple backends (SQLite, Redis, MongoDB)
""")

# ============================================================================
# PLATFORM-SPECIFIC SCHEDULING
# ============================================================================

print("\n" + "="*60)
print("PLATFORM-SPECIFIC SCHEDULING")
print("="*60)

print("""
🐧 Linux/Mac: Cron
-----------------
# Edit crontab
crontab -e

# Run Python script daily at 9am
0 9 * * * /usr/bin/python3 /path/to/script.py

# Every 5 minutes
*/5 * * * * python3 /path/to/monitor.py

# Every Monday at 8am
0 8 * * 1 python3 /path/to/weekly_task.py

Cron format: minute hour day month day_of_week


🪟 Windows: Task Scheduler
--------------------------
# Via Command Line (schtasks)
schtasks /create /tn "DailyReport" /tr "python C:\\scripts\\report.py" /sc daily /st 09:00

# Via GUI
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily, time)
4. Action: Start a program
5. Program: python
6. Arguments: C:\\path\\to\\script.py


☁️ Cloud Scheduling
------------------
# AWS CloudWatch Events / EventBridge
# Google Cloud Scheduler
# Azure Logic Apps / Functions
# Perfect for serverless Python automation
""")

# ============================================================================
# INTEGRATION WITH WORKFLOWS
# ============================================================================

print("\n" + "="*60)
print("INTEGRATION WITH BI/AUTOMATION WORKFLOWS")
print("="*60)

print("""
🔗 Scheduling in Data Pipelines:

1. ETL Pipeline Automation
   - Schedule: Daily at 2am
   - Extract: Pull data from APIs
   - Transform: Clean and process
   - Load: Push to Power BI / Database
   - Notify: Email success/failure report

2. Make.com / n8n Scheduling
   - Use platform's built-in scheduler
   - Trigger Python scripts via webhook
   - Or: Python script triggers Make.com workflow
   - Hybrid: Schedule in Python, execute in n8n

3. AI/LLM Workflows
   - Schedule: Daily at 8am
   - Fetch: Latest news/data
   - Process: Send to LLM for summary
   - Deliver: Email insights to team

4. Monitoring & Alerts
   - Schedule: Every 5 minutes
   - Check: API health, database status
   - Alert: SMS/Email if issues found
   - Log: Track uptime metrics

💡 Best Practice Stack:
   - Development/Testing: schedule module
   - Production: APScheduler or cron/Task Scheduler
   - Cloud: Platform-native schedulers
   - Complex workflows: Make.com / n8n + Python
""")

# ============================================================================
# ERROR HANDLING & BEST PRACTICES
# ============================================================================

print("\n" + "="*60)
print("ERROR HANDLING & BEST PRACTICES")
print("="*60)

print("""
⚠️ Important Considerations:

1. Error Handling in Scheduled Tasks
   try:
       scheduled_task()
   except Exception as e:
       log_error(e)
       send_alert(f"Task failed: {e}")

2. Logging
   import logging

   logging.basicConfig(
       filename='scheduler.log',
       level=logging.INFO,
       format='%(asctime)s - %(message)s'
   )

   logging.info("Task started")
   logging.error("Task failed")

3. Timeout Handling
   import signal

   def timeout_handler(signum, frame):
       raise TimeoutError("Task took too long")

   signal.signal(signal.SIGALRM, timeout_handler)
   signal.alarm(300)  # 5 minute timeout

   try:
       long_running_task()
   finally:
       signal.alarm(0)

4. Avoid Overlapping Executions
   - Check if previous task still running
   - Use lock files or flags
   - Skip if already in progress

5. Environment & Dependencies
   - Use virtual environments
   - Absolute paths in cron/scheduler
   - Set working directory
   - Load environment variables

6. Testing Scheduled Tasks
   - Test functions independently first
   - Use short intervals for testing
   - Monitor logs during trial period
   - Dry-run mode for safety

Example: Robust Scheduled Task
------
import schedule
import logging
from pathlib import Path

logging.basicConfig(filename='tasks.log', level=logging.INFO)

def safe_task():
    lock_file = Path("task.lock")

    # Check if already running
    if lock_file.exists():
        logging.warning("Task already running, skipping")
        return

    # Create lock
    lock_file.touch()

    try:
        # Your task here
        result = perform_task()
        logging.info(f"Task completed: {result}")
    except Exception as e:
        logging.error(f"Task failed: {e}")
        send_alert(f"Task error: {e}")
    finally:
        # Always remove lock
        lock_file.unlink()

schedule.every().hour.do(safe_task)
""")

print("\n✓ Scheduling & time automation concepts covered!")
print("\n📦 Required packages:")
print("  - time, datetime: Built-in")
print("  - schedule: pip install schedule")
print("  - APScheduler: pip install apscheduler")
