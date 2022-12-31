import random
nums=[]
for i in range(10):
    nums.append(random.randint(1,100))
# 또는
# nums=[random.randint(1,100) for i in range(10)]

print("생성된 리스트는 : ", nums)
sum=0
for n in nums:
    sum += n
# 또는
# sum=sum(nums)

print("합은 %d, 평균은 %f"%(sum, sum/10))

max=nums[0]
min=nums[0]
for i in range(1,len(nums)):
    if max < nums[i]:
        max = nums[i]
    if min > nums[i]:
        min = nums[i]
# 또는
# max=max(nums)
# min=min(nums)

print("최대값은 %d, 최소값은 %d"%(max, min))