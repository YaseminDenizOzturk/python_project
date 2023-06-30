import math

def paint_area_calculator(height,width,cover):
    area = height * width
    how_many_cans = math.ceil(area / cover)
    print(f"You will need {how_many_cans} cans of paint")

height1 = int(input("Height of wall: "))
width1 = int(input("Width of wall: "))
coverage = 5
paint_area_calculator(height= height1 , width= width1 , cover= coverage)

