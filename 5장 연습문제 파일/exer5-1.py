# 한 개의 정수 (범위 -5~5) 를 난수로 생성하고 이를 출력하라
# 생성된 수의 절대값을 출력하도록 하라

import random

x=random.randint(-5,5)
print("생성된 수 : ", x)

if x<0:
    y = -x
else:
    y = x

print(x, "의 절대값은 ", y, " 입니다.")
