def if_possible(mid,n):
    return mid*mid<=n

n=int(input("Enter a number:"))
low=0
high=n
answer=-1
while low<=high:
    mid=(low+high)//2
    if if_possible(mid,n):
        answer=mid
        low=mid+1
    else:
        high=mid-1
print("The square root of",n,"is",answer)

