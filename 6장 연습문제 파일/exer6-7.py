# 1~100까지 중 난수를 반복적으로 만드는데, 계속할지 여부를 물어서 계속하기 원하는 만큼 반복하도록 하는 프로그램을 작성하라

import random

cont='y'
while(cont=='y'):
    n = random.randint(1,100)
    print("생성된 난수는 = %d"% n)
    cont=input("계속하시겠습니까? (y/n)")
    
print("바이바이~~")
