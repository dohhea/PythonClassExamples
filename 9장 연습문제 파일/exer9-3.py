import random
freq=[0]*10

for i in range(100):
    n=random.randint(0,9)
    freq[n]+=1

print("0~9 도수는 ", freq)