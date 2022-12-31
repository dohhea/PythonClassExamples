# 사용자가 입력하는 숫자의 합 구하기를 무한 loop과 break 문을 활용하여 다시 구현

total = 0
while True:                             # 무한 루프
    number = int(input("숫자를 입력하시오:  "))
    total = total + number
    answer = input("계속?(yes/no): ")
    if answer == "no" :                 # 계속하지 않는 경우 loop 빠져나옴
        break
print("합계는 : ", total)
