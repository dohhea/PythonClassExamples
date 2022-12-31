# 주어진 수 만큼의 별을 그 수만 큼 반복해서 다양한 별을 출력하는 프로그램 작성

n=int(input("정수를 하나 입력하세요 : "))

# 왼쪽 위 탑
for i in range(n):
    print("*"*(i+1))
    
# 오른쪽 위 탑
for i in range(n):
    stars=i+1               # 행마다 출력할 별의 개수
    blanks=n-stars          # 행마다 출력할 공백의 개수
    print(" "*blanks, end="")
    print("*"*stars)

# 왼쪽 아래 탑
for i in range(n):
    stars=n-i               # 행마다 출력할 별의 개수
    print("*"*stars)
    
# 오른쪽 아래 탑
for i in range(n):
    stars=n-i               # 행마다 출력할 별의 개수
    blanks=n-stars          # 행마다 출력할 공백의 개수
    print(" "*blanks, end="")
    print("*"*stars)
