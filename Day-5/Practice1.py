import math
def bsearch(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return math.sqrt(arr[mid])
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return "Not Found"

arr=[12,34,36,78,92,100]
target=36
result=bsearch(arr,target)
print(result)
     