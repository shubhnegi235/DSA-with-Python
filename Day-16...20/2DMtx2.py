def matrix(arr, aim):
    row=0
    col=len(arr[0])-1
    while row<len(arr) and col>=0:
        if arr[row][col]==aim:
            return True
        elif arr[row][col]<aim:
            row+=1
        else:
            col-=1
    return False    

arr = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target = 16
result = matrix(arr, target)
print(result)