def calculate_area(s1, s2, s3):
    k = (s1 + s2 + s3) / 2
    area = (k * (k - s1) * (k - s2) * (k - s3)) ** 0.5
    return area

def read():
    s1 = int(input("Enter side 1 of triangle 1: "))
    s2 = int(input("Enter side 2 of triangle 1: "))
    s3 = int(input("Enter side 3 of triangle 1: "))
    
    return s1, s2, s3

a1 ,a2 ,a3 =read()
b1,b2,b3 =read()

triangle1_area = calculate_area(a1,a2,a3)
triangle2_area = calculate_area(b1,b2,b3)

print("Area of Triangle 1:", triangle1_area)
print("Area of Triangle 2:", triangle2_area)
