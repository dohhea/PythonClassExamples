# 세 개의 정수 (범위 1~100) 를 난수로 생성하고 이를 출력하라
# 생성된 수 중 가장 큰 수를 출력하도록 하라

import random

x=random.randint(1,100)
y=random.randint(1,100)
z=random.randint(1,100)
print("생성된 세 수 : ", x, ", ", y, ", ", z)

if x>=y:            # x가 가장 큰 수인 경우
    if x>=z:
        max=x
    else:
        max=z
else:               # y나 z가 가장 큰 수인 경우
    if y>=z:
        max=y
    else:
        max=z

print("가장 큰 수는 ", max, " 입니다")

'''
if x>=y and x>=z :
    max=x
else:
    if y>=z:
        max=y
    else:
        max=z

print("가장 큰 수는 ", max, " 입니다")
'''

'''
if x>=y and x>=z :
    max=x
if y>=x and y>=z :
    max=y
if z>=x and z>=y :
    max=z

print("가장 큰 수는 ", max, " 입니다")
'''