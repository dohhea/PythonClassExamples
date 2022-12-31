def isPrime(x) :
    prime=True
    for i in range(2,x):
        if x%i == 0:
            prime=False
    return prime
'''
def isPrime(x) :
    for i in range(2,x):
        if x%i == 0:
            return False
    return True
'''
n=int(input("수 입력 : "))

print("2 부터 %d까지 존재하는 소수는 : "%n, end="")
for i in range(2, n+1):
    if isPrime(i):
        print(i, end=" ")
print()
