import random
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

primes=[]
count=0
limit=int(input("갯수 입력 : "))
n=2                     # 2부터 시작
while True:
    if count == limit:  # 필요한 개수 채움
        break
    if (isPrime(n)):
        primes.append(n)    # 소수인경우 리스트 추가
        count+=1
    n+=1                # 다음 수

print("생성된 소수의 리스트는 ", primes)