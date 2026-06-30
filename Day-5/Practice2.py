def lserch(arr, aim):
    for i in range(len(arr)):
        if arr[i]==aim:
            return i
    return "Not Found"

arr=[3,7,12,18,25,31,4250]
aim=25
result = lserch(arr, aim)
print(result)


                   
