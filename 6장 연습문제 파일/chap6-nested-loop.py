# 중첩루프의 예로 구구단을 출력하는 프로그램

for i in range(1,10):
    for j in range(1,10):
        print(i*j, end="\t")
    print("")


# 주어진 수 만큼의 별을 그 수만 큼 반복해서 출력하는 프로그램 작성

n=int(input("정수를 하나 입력하세요 : "))

for i in range(n):
    for j in range(n):
        print("*", end="")
    print("")
    