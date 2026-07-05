def if_possible(stalls, cows, distance):
    count=1
    last_stall=stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i]-last_stall>=distance:
            count+=1
            last_stall=stalls[i]
    return count>=cows

stalls=[1,2,4,8,9]
cows=3
stalls.sort()
low=1
high=stalls[-1]-stalls[0]
ans=-1
while low<=high:
    mid=(low+high)//2
    if if_possible(stalls, cows, mid):
        ans=mid
        low=mid+1
    else:
        high=mid-1
print(ans)


   