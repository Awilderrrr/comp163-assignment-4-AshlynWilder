# Foundation setup
student_name = "Ashlyn Wilder"
current_gpa = 3.1
study_hours = 10
social_points = 20
stress_level = 75

print("=== WELCOME TO COLLEGE LIFE: ADVENTURE GAME ===")
print(f"Student: {student_name}")
print(f"Starting GPA: {current_gpa:.2f}")
print(f"Study Hours / week: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

# Course Planning Decision
print("\n--- Decision 1: Course Planning ---")
print("Choose your course load:")
print("Choose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice (A/B/C): ")

if choice == "A":
    if current_gpa >= 3.0:
        study_hours >= 2
        stress_level <= 5
        print("Light load chosen. You protect your GPA and reduce stress")
    else:
        study_hours <= 1
        stress_level <= 3
        print("Light load chosen. You ease back to stabilize your grades")
elif choice == "B":
    if current_gpa >= 3.5:
        study_hours <= 1
        study_level >= 2
        print("You chose Standard Load. Feels balanced with your strong GPA")
    else:
        study_hours >= 2
        stress_level >= 4
        print("You chose Standard Load. Manageable, but requires more effort")
elif choice == "C":
    if current_gpa >= 3.5:
        study_hours >= 4
        stress_level >= 6
        print("You chose Heavy Load. With your GPA, you can do it.")
    else:
        study_hours >= 5
        stress_level >= 10
        print("You chose Heavy Load. The extra credits")
else:
    print("Invaild choice.")