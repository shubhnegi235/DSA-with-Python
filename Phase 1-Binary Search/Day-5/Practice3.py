import math
def bsearch(arr, aim):
    count=0
    low=0
    high=len(arr)-1
    while low<=high:
        count+=1
        mid=(low+high)//2
        if arr[mid]==aim:
           return math.sqrt(arr[mid]),"Target found after",count,"iterations" 
        elif arr[mid]<aim:
            low=mid+1
        else:
            high=mid-1
    return "Not Found"

arr=[2,4,6,8,10,14]
aim=8
result=bsearch(arr, aim)
print(result)