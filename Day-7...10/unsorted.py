def unsorted_search(arr, aim):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==aim:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=aim<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<aim<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1

arr = [15, 18, 2, 3, 6, 12]
aim = 3
print(unsorted_search(arr, aim))