# 정수를 하나 입력 받고 이 수의 약수를 모두 출력하는 프로그램을 작성하라

n=int(input("정수 하나를 입력하세요 : "))
print(n, "의 약수는 : ")

for i in range(1, n+1):
    if (n % i == 0):
        print(i , end=" ")          # end로 출력 끝 문자 설정
