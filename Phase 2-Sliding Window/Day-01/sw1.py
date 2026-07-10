def two_sum(num, aim):
    left=0
    right=len(num)-1
    while left<right:
        total=num[left]+num[right]
        if total==aim:
            return [left+1, right+1]
        elif total<aim:
            left+=1
        else:
            right-=1
    return None

num=[2,7,11,15]
aim=9
print(two_sum(num, aim))