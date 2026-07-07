def matrix(arr, target):
    low=0
    high=len(arr)*len(arr[0])-1
    while low<=high:
        mid=low+(high-low)//2
        row=mid//len(arr[0])
        col=mid%len(arr[0])
        if arr[row][col]==target:
            return True
        elif arr[row][col]<target:
            low=mid+1
        else:
            high=mid-1
    return False

arr=[[1,3,5,7],
      [10,11,16,20],
      [23,30,34,60]]
target=7
result=matrix(arr, target)
print(result)