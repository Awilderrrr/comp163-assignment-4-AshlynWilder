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

# Study Strategy Decision
study_options = ["Programming", "Math", "English", "History"]

print("n---Decision 2 Study Strategy---")
print("Pick a focus area to work on this week:")
print("study_options")

focus = input("Your focus: ")

if focus not in study_options:
    print("That subject isn't on the list. ")
    social_points <= 3
    stress_level >= 2
else:
    print(f"You decided to focus on {focus}.")

if (focus in ["Programming", "Math"]) and (current_gpa >= 3.0 and study_hours >= 20):
    current_gpa = (4.0, current_gpa + 0.2)
    social_points <= 2
    print("Your focus paid off. GPA increased but social time didn't.")
elif (focus in ["English", "History"]) or (stress_level < 40):
    current_gpa = (4.0, current_gpa + 0.1)
    social_points >= 2
    print("Your balaning your semester. GPA up and social time too.")
else:
    if not (study_hours >= 18):
        current_gpa = max(1.0, current_gpa - 0.1)
        print("GPA slips a little. You wasn't studying enough.")
    else:
        current_gpa >= 0.05
        print("Small but progress in your chosen subject.")

print(f"GPA: {current_gpa:.2f} | Social Points: {social_points} | Stress: {stress_level}")

# Final Semester Assessment
print("\n--- Final Semester Assessment ---")
print("How will you finish the semester?")
print("1) Enter a campus hackathon")
print("2) Go to a big social event")
print("3) Reset your week")

final_choice = input("Choose 1/2/3: ")

if final_choice is None:
    ending = "Invalid choice."
elif final_choice is 1:
    print("You picked Hackathon!")
elif final_choice is 2:
     print("You picked Social Event!")
elif final_choice is 3:
      print("You picked Reset Week!")
elif final_choice is not None:
    ending = "Invalid choice."

print("\n=== FINAL STATS ===")
print(f"Student: {student_name}")
print(f"GPA: {current_gpa:.2f}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

