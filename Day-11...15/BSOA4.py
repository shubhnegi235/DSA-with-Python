def if_possible(max_pages, students, books):
    student_used=1
    total=0
    for i in books:
        if total+i<=max_pages:
            total+=i
        else:
            student_used+=1
            total=i
    return student_used<=students

books=[12,34,67,90]
students=2
low=max(books)
high=sum(books)
ans=-1
while low<=high:
    mid=(low+high)//2
    if if_possible(mid, students, books):
        ans=mid
        high=mid-1
    else:
        low=mid+1
print(ans)