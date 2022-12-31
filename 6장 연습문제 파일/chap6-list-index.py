lst=[10, 5, 23, 45, 96, 77]

# 리스트의 원소를 인덱스를 사용하여 접근 (출력)
print("리스트의 원소 출력")
for i in range(len(lst)):
    print(lst[i])

# 리스트의 원소를 인덱스를 사용하여 거꾸로 출력
print("리스트의 원소 거꾸로 출력. 방법1")
length=len(lst)
for i in range(length):
    print(lst[length-1-i])

print("리스트의 원소 거꾸로 출력. 방법2")
for i in range(1,len(lst)+1):
    print(lst[-i])
