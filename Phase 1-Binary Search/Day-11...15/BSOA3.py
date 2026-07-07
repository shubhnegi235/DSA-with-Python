def if_possible(capacity, weights, days):
    days_used=1
    total=0
    for i in weights:
        if total+i<=capacity:
            total+=i
        else:
            days_used+=1
            total=i
    return days_used<=days

weights=[1,2,3,4,5,6,7,8,9,10]
capacity=5
low=max(weights)
high=sum(weights)
ans=-1
while low<=high:
    mid=(low+high)//2
    if if_possible(mid, weights, capacity):
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)

