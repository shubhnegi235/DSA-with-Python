def first_occurrence(arr,aim):
    low = 0
    high = len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]==aim:
            ans=mid
            high=mid-1
        elif arr[mid]<aim:
            low=mid+1
        else:
            high=mid-1
    return ans

def last_occurrence(arr,aim):
     low = 0
     high = len(arr) - 1
     ans = -1
     while low <= high:
        mid = (low + high) // 2
        if arr[mid]==aim:
            ans=mid
            low=mid+1
        elif arr[mid]<aim:
            low=mid+1
        else:
            high=mid-1
     return ans

arr=[1,2,2,2,3,4,4,5]
aim=6
first=first_occurrence(arr,aim)
last=last_occurrence(arr,aim)
if first==-1:
    print("Not Found")
else:
    count=last-first+1
    print(count)

    