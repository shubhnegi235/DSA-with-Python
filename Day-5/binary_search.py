def binary_search(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return "Not Found"

arr=[2,4,7,10,15,18,21]
target=7
result=binary_search(arr,target)
print(result)