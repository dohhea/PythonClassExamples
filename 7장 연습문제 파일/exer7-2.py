def calculate_area (radius):
    area = 3.14 * radius**2
    return area


while (True):
    radius = int(input("반지름을 입력하세요 : "))
    if radius <= 0:
        break
    print("면적은 : ", calculate_area (radius))
    
print("바이바이~~")



