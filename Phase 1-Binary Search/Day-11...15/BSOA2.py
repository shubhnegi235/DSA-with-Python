import math
def if_possible(speed, piles, h):
    total_hours=0
    for i in piles:
        total_hours+=math.ceil(i/speed)
        return total_hours<=h
    
piles=[3,6,7,11]
h=8
low=1
high=max(piles)
ans=0
while low<=high:
    mid=(low+high)//2
    if if_possible(mid,piles,h):
        ans=mid
        high=mid-1
    else:
        low=mid+1
print("The minimum eating speed is",ans)