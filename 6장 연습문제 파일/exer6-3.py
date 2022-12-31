# 정수를 하나 입력 받아 이 수가 소수 (prime number) 인지 아닌지를 판단하여 출력하는 프로그램을 작성하라


n=int(input("정수 하나를 입력하세요 : "))

isPrime=True

for i in range(2, n//2):
    if (n%i ==0):
        isPrime=False

if isPrime:
    print("%d는 소수입니다."%n)
else:
    print("%d는 소수가 아닙니다."%n)
    
    