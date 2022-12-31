# 1. 두개의 정수 (범위 1~5) 를 난수로 생성하고 이를 출력하라
# 2. 두개의 중 더 큰 수를 출력하라. 만약 두 수가 동일하면 수가 같다고 출력하게 하라

import random

x=random.randint(1,5)
y=random.randint(1,5)
print("생성된 두 수 : ", x, ", ", y)

if x==y:
    print("두 수는 같습니다.")
else:
    if (x>y):
        print("더 큰 수는 ", x, " 입니다")
    else:
        print("더 큰 수는 ", y, " 입니다")
        
# 또는

'''
if x==y:
    print("두 수는 같습니다.")
elif (x>y):
    print("더 큰 수는 ", x, " 입니다")
else:
    print("더 큰 수는 ", y, " 입니다")
'''        
      
