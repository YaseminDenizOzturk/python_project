student_scores = input("Input a list of student scores: ").split()
for s in range(0 , len(student_scores)):
    # skorları tamsayıya dönüştürüyorum.
    student_scores[s] = int(student_scores[s])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest sore in the class is: {highest_score}")
