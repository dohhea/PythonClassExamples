import random

# 10개의 랜덤 수 1~100 생성
lst=[]
for i in range(10):
    lst.append(random.randint(1,100))
    
print(lst)

for i in range(len(lst)-1):         # 총 수행해야 하는 큰 loop의 수
    for j in range(len(lst)-i-1):   # 매번 수행해야 하는 작은 loop의 수
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print(lst)