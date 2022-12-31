snacks={'꼬깔콘':1500, '새우깡':1300, '프링글즈': 2500, '고소미':1400}
print(snacks)

top='꼬깔콘'

# for key in list(snacks.keys())[1:]:
for key in snacks.keys():
    if snacks[top] < snacks[key]:
        top=key

print(f"가장 비싼 과자는 {top}이고 가격은 {snacks[top]}원 입니다")

print(list(snacks.keys()))