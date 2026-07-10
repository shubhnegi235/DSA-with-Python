def max_sum(arr, k):
    w_sum=sum(arr[:k])
    m_sum=w_sum
    for i in range(k, len(arr)):
        w_sum=w_sum-arr[i-k]+arr[i]
        m_sum=max(m_sum, w_sum)
    return m_sum

arr=[1,12,-5,-6,50,3]
k=4
print(max_sum(arr, k))