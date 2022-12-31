def above(list, bound=50):
    upper, lower = 0, 0
    for n in list:
        if n >= bound:
            upper+=1
        else:
            lower+=1
    return upper, lower

import random
# list=[random.randint(1,100) for i in range(10)]
list=[]
for i in range(10):
    list.append(random.randint(1,100))
print("list =", list)
u, l = above(list, 30)
print(f"기준 {30}에서의 큰수 개수 {u} 작은 수 개수 {l} ")

u, l = above(list)
print(f"기준 {50}에서의 큰수 개수 {u} 작은 수 개수 {l} ")

u, l = above(list, 70)
print(f"기준 {70}에서의 큰수 개수 {u} 작은 수 개수 {l} ")