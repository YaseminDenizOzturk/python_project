student_scores = {
    "Yasemin": 92,
    "Deniz": 89,
    "Elif": 93,
    "Merve": 70,
    "Ayşe": 45,
}

# boş bir sözlük oluşturuyorum.
student_grades = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding Achievement"
    elif score > 80 :
        student_grades[student] = "Exceeds Expectations"
    elif score >= 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
