import random

def findout(list):
    even, odd, zero, positive, negative = 0,0,0,0,0
    for n in list:
        if n%2==0:
            even +=1
        else:
            odd +=1
        if n>0:
            positive +=1
        elif n<0:
            negative +=1
        else:
            zero +=1
    return even, odd, zero, positive, negative
list=[]
for n in range(10):
    list.append(random.randint(-10,10))
print("list = ", list)

even,odd,zero, positive,negative = findout(list)

print(f"양수={positive}, 음수={negative}, 영={zero}, 홀수={odd}, 짝수={even}")