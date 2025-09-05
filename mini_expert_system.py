import csv
import os

# File for logging results
CSV_FILE = "logic_results.csv"

# Initialize CSV with headers if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Student", "Rule", "Condition", "Result"])


def log_result(student, rule, condition, result):
    """Logs results into CSV file"""
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student, rule, condition, result])


# ===== Rules =====
def attendance_rule(student, present_days, total_days):
    condition = f"{present_days}/{total_days}"
    if present_days / total_days >= 0.75:
        result = "Attendance OK"
    else:
        result = "Attendance Low"
    log_result(student, "Attendance Rule", condition, result)
    return result


def grading_rule(student, score):
    condition = f"Score = {score}"
    if score >= 75:
        result = "Pass"
    else:
        result = "Fail"
    log_result(student, "Grading Rule", condition, result)
    return result


def login_system_rule(student, username, password, correct_user, correct_pass):
    condition = f"User={username}, Pass={password}"
    if username == correct_user and password == correct_pass:
        result = "Login Successful"
    else:
        result = "Login Failed"
    log_result(student, "Login System Rule", condition, result)
    return result


def bonus_points_rule(student, activity_done):
    condition = f"Activity Done = {activity_done}"
    if activity_done:
        result = "Bonus Points Awarded"
    else:
        result = "No Bonus"
    log_result(student, "Bonus Points Rule", condition, result)
    return result


# ===== New Rule (Example: Library Borrowing) =====
def library_rule(student, id_valid):
    condition = f"ID Valid = {id_valid}"
    if id_valid:
        result = "Allowed to Borrow"
    else:
        result = "Not Allowed"
    log_result(student, "Library Rule", condition, result)
    return result


# ===== Testing the System with 3 Students =====
students = [
    {"name": "Alice", "attendance": (18, 20), "score": 85, "login": ("alice", "1234"), "activity": True, "id_valid": True},
    {"name": "Bob", "attendance": (10, 20), "score": 65, "login": ("bob", "wrongpass"), "activity": False, "id_valid": False},
    {"name": "Charlie", "attendance": (16, 20), "score": 75, "login": ("charlie", "abcd"), "activity": True, "id_valid": True}
]

# Correct credentials for login rule
correct_user = "alice"
correct_pass = "1234"

for s in students:
    print(f"\n--- Results for {s['name']} ---")
    print(attendance_rule(s["name"], *s["attendance"]))
    print(grading_rule(s["name"], s["score"]))
    print(login_system_rule(s["name"], s["login"][0], s["login"][1], correct_user, correct_pass))
    print(bonus_points_rule(s["name"], s["activity"]))
    print(library_rule(s["name"], s["id_valid"]))

print("\n✅ All results logged into logic_results.csv")
