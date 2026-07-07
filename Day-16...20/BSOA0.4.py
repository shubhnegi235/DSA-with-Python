def median(num1, num2, k):
    if len(num1)>len(num2):
        num1,num2=num2,num1

        n1=len(num1)
        n2=len(num2)

        low=max(0,k-n2)
        high=min(k,n1)
        while low<=high:
            cut1=(low+high)//2
            cut2=k-cut1 

            l1=float('-inf') if cut1==0 else num1[cut1-1]
            l2=float('-inf') if cut2==0 else num2[cut2-1]
            r1=float('inf') if cut1==n1 else num1[cut1]
            r2=float('inf') if cut2==n2 else num2[cut2]

            if l1<=r2 and l2<=r1:
               return max(l1,l2)
            elif l1>r2:
                high=cut1-1
            else:
                low=cut1+1

arr1=[2,3,6,7,9]
arr2=[1,4,8,10]
k=5
print(median(arr1,arr2, k))