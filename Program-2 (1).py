nums = int(input())
start = 1
ans = list()
for _ in range(nums):
    ans.append(start)
    start+=2
print(", ".join(map(str,ans)))
