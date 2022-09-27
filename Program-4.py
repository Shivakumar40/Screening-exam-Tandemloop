

check_multiples = range(1,10)
ans = dict()
nums = list(map(int,input().split()))

for i in range(1,10):
    ans[i]=0
    for n in nums:
        if n%i==0:
            ans[i]+=1

print(ans)
