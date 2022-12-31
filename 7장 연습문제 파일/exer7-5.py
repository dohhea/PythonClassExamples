import random
def biggest(list):
    max=list[0]     # 현재로서는 첫번째 원소가 가장 큼
    
    for i in range(1, len(list)-1):
        if max < list[i]:
            max = list[i]
    return max

lst = []
for i in range(10):
    lst.append(random.randint(1,100))
    
print("list = ", lst)
print("가장 큰 값은 ", biggest(lst))
