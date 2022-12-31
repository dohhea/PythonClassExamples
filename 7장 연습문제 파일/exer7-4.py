import random
def biggest(a, b, c):
    if a >= b and a >= c: 
        return a
    elif b >= a and b >= c: 
        return b
    else:
        return c

'''
def biggest(a,b,c):
    big = a
    if b>=big:
        big = b
    if c>=big:
        big=c
    return big
'''

a=random.randint(1,100);
b=random.randint(1,100);
c=random.randint(1,100);

# print(f"{a}, {b}, {c} 중 가장 큰 수는 {biggest(a,b,c)}")
print("{}, {}, {} 중 가장 큰 수는 {}".format(a,b,c,biggest(a,b,c)))


    