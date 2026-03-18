# Internship Management System

class Student:
    def __init__(self, username):
        self.username = username
        self.applications = []

class Internship:
    def __init__(self, title, company):
        self.title = title
        self.company = company
        self.applicants = []

class Application:
    def __init__(self, student, internship):
        self.student = student
        self.internship = internship
        self.status = "Under Review"

# Data storage
students = {}
internships = [
    Internship("Software Developer Intern", "Google"),
    Internship("Data Analyst Intern", "Microsoft"),
    Internship("IT Support Intern", "Local Company")
]

# Register student
def register():
    username = input("Enter username: ")
    if username in students:
        print("User already exists!")
    else:
        students[username] = Student(username)
        print("Registration successful!")

# Login
def login():
    username = input("Enter username: ")
    if username in students:
        print("Login successful!")
        student_menu(students[username])
    else:
        print("User not found!")

# Student menu
def student_menu(student):
    while True:
        print("\n1. View Internships")
        print("2. Apply for Internship")
        print("3. View My Applications")
        print("4. Logout")

        choice = input("Choose option: ")

        if choice == "1":
            view_internships()

        elif choice == "2":
            apply(student)

        elif choice == "3":
            view_applications(student)

        elif choice == "4":
            break

# View internships
def view_internships():
    for i, internship in enumerate(internships):
        print(f"{i+1}. {internship.title} at {internship.company}")

# Apply
def apply(student):
    view_internships()
    choice = int(input("Select internship: ")) - 1

    if 0 <= choice < len(internships):
        internship = internships[choice]
        application = Application(student, internship)

        student.applications.append(application)
        internship.applicants.append(application)

        print("Application submitted!")
    else:
        print("Invalid choice!")

# View applications
def view_applications(student):
    if not student.applications:
        print("No applications yet.")
    else:
        for app in student.applications:
            print(f"{app.internship.title} - {app.status}")

# Admin review
def admin_panel():
    print("\n--- Admin Panel ---")
    for internship in internships:
        for app in internship.applicants:
            print(f"{app.student.username} applied for {internship.title} [{app.status}]")

            decision = input("Accept (a) / Reject (r) / Skip (s): ")
            if decision == "a":
                app.status = "Accepted"
            elif decision == "r":
                app.status = "Rejected"

# Main menu
def main():
    while True:
        print("\n--- Internship System ---")
        print("1. Register")
        print("2. Login")
        print("3. Admin Panel")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            admin_panel()
        elif choice == "4":
            break

# Run program
main()
