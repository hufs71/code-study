# 2. K번째 수

t = int(input())
answer = []
cnt = 0

while True:
    n, s, e, k = map(int, input().split()) # 6 2 5 3
    nums = list(map(int, input().split())) # 5 2 7 3 8 9

    min = nums[s-1]
    max = nums[e-1]
    nums = nums[s-1:e] # 2 7 3 8
    nums.sort() # 2 3 7 8

    answer.append(nums[k-1])
    
    cnt += 1
    if cnt == t:
        break

print(answer)
