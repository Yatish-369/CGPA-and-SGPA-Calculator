def calculate_sgpa(grades, credits):
    total_credits = sum(credits)
    if total_credits == 0:
        return 0.0, 0
    weighted_sum = sum(g * c for g, c in zip(grades, credits))
    return round(weighted_sum / total_credits, 2), total_credits

def calculate_updated_cgpa(past_cgpa, past_credits, new_sgpa, new_credits):
    total_credits = past_credits + new_credits
    if total_credits == 0:
        return 0.0
    total_weighted = (past_cgpa * past_credits) + (new_sgpa * new_credits)
    return round(total_weighted / total_credits, 2)

def get_grade_point_from_marks(marks):
    if 90 <= marks <= 100:
        return 10  # O
    elif 80 <= marks < 90:
        return 9   # E
    elif 70 <= marks < 80:
        return 8   # A
    elif 60 <= marks < 70:
        return 7   # B
    elif 50 <= marks < 60:
        return 6   # C
    elif 40 <= marks < 50:
        return 5   # D
    else:
        return 4   # F

def get_grade_point_from_letter(grade):
    grade = grade.upper()
    grade_mapping = {'O': 10, 'E': 9, 'A': 8, 'B': 7, 'C': 6, 'D': 5, 'F': 4}
    return grade_mapping.get(grade, 0)

def input_subjects_data(num_subjects, method_label):
    grades = []
    credits = []
    for i in range(num_subjects):
        print(f"\n{method_label} - Subject {i+1}:")
        if method_label == "Marks":
            marks = float(input("Enter marks (0-100): "))
            grade_point = get_grade_point_from_marks(marks)
        else:
            grade_letter = input("Enter grade (O/E/A/B/C/D/F): ")
            grade_point = get_grade_point_from_letter(grade_letter)
        credit = int(input("Enter subject credits: "))
        grades.append(grade_point)
        credits.append(credit)
    return grades, credits

def main():
    print("🎓 SGPA & CGPA Calculator\n")

    method = input("Choose input method (marks/grades): ").strip().lower()
    method_label = "Marks" if method == "marks" else "Grades"

    option = input("Do you know your past CGPA? (yes/no): ").strip().lower()
    if option == 'yes':
        past_cgpa = float(input("Enter your past CGPA: "))
        past_credits = int(input("Enter total credits till previous semester: "))
    else:
        total_semesters = int(input("Enter number of completed semesters: "))
        past_grades = []
        past_credits_list = []
        for sem in range(total_semesters):
            print(f"\n--- Semester {sem+1} ---")
            num_subjects = int(input("Enter number of subjects: "))
            grades, credits = input_subjects_data(num_subjects, method_label)
            past_grades.extend(grades)
            past_credits_list.extend(credits)
        past_cgpa, past_credits = calculate_sgpa(past_grades, past_credits_list)
        print(f"\n📘 Calculated Past CGPA: {past_cgpa}")

    print("\n--- Current Semester ---")
    num_subjects = int(input("Enter number of subjects in current semester: "))
    curr_grades, curr_credits = input_subjects_data(num_subjects, method_label)

    current_sgpa, current_credits = calculate_sgpa(curr_grades, curr_credits)
    updated_cgpa = calculate_updated_cgpa(past_cgpa, past_credits, current_sgpa, current_credits)

    print(f"\n📘 SGPA for Current Semester: {current_sgpa}")
    print(f"📊 Updated CGPA: {updated_cgpa}")

if __name__ == "__main__":
    main()
