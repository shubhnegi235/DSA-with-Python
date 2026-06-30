count=0
arr=[4,7,9,2,10,3,8]
for i in range(len(arr)):
    if arr[i]%2==0:
        count+=1
print("The number of even numbers in the array is:", count)
