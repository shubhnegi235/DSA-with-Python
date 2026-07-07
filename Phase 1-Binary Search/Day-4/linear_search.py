def lsearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return "Found"
    return "Not Found"
arr=[12,45,23,67,89,90]
target=45
result=lsearch(arr, target)
print(result)