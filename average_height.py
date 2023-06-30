student_heights = input("Input a list of student heights ").split()
for x in range(0 , len(student_heights)):
    # boy değerlerini tamsayıya dönüştürüyorum.
    student_heights[x] = int(student_heights[x])
print(student_heights)

# sum fonksiyonu toplamı verecek.
total_height = sum(student_heights)
# len fonksiyonu uzunluğunu verecek.
number_of_students = len(student_heights)
# bölüm sonucunu yuvarlamak için round kullandım.
average_height = round(total_height / number_of_students)
print(average_height)
