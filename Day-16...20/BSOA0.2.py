def if_possible(mid, nums, k):
    split_count=1
    total=0
    for i in nums:
        if total+i<=mid:
            total+=i
        else:
            split_count+=1
            total=i
    return split_count<=k

nums=[7,2,5,10,8]
k=2
low= max(nums)
high=sum(nums)
ans=-1
while low<=high:
    mid=(low+high)//2
    if if_possible(mid, nums, k):
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)