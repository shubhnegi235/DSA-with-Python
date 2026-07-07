def foccurrence(arr, target):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            ans=mid
            high=mid-1
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return ans

arr=[2,4,4,4,7,9,11]
target=4
print(foccurrence(arr,target))

