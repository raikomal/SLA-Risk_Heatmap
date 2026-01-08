import csv
import os
from datetime import datetime

# =========================
# REPORT FOLDER & FILE
# =========================
REPORT_DIR = "reports"

os.makedirs(REPORT_DIR, exist_ok=True)

TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
REPORT_FILE = os.path.join(
    REPORT_DIR,
    f"ui_report_{TIMESTAMP}.csv"
)

# =========================
# START NEW REPORT
# =========================
def start_new_report():
    with open(REPORT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Project",
            "Application",
            "Micro_Application",
            "Title",
            "Description",
            "Steps",
            "Expected_Result",
            "Actual_Result",
            "Status",
            "Remark",
            "Task_ID",
            "Ticket_ID"
        ])

# =========================
# WRITE TEST REPORT
# =========================
def write_test_report(
    project,
    application,
    micro_application,
    title,
    description,
    steps,
    expected_result,
    actual_result,
    status,
    remark="",
    task_id="",
    ticket_id=""
):
    with open(REPORT_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            project,
            application,
            micro_application,
            title,
            description,
            steps,
            expected_result,
            actual_result,
            status,
            remark,
            task_id,
            ticket_id
        ])

# =========================
# AUTO FAIL REPORT
# =========================
def write_fail_report(title, error_message):
    write_test_report(
        "Tower Track",
        "Web",
        "Auto Failure",
        title,
        "Test execution",
        "Test should pass",
        "Test failed",
        "Fail",
        error_message[:500],
        "AUTO-FAIL",
        ""
    )
