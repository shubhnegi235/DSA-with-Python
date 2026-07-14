from collections import Counter
def min_window(s,t):
    if not s or not t:
        return ""
    need=Counter(t)
    window={}
    left=0
    min_len=float("inf")
    res=""
    have=0
    need_count=len(need)
    for right in range(len(s)):
        window[s[right]]=window.get(s[right],0)+1
        if s[right] in need and window[s[right]]==need[s[right]]:
            have+=1
        while have==need_count:
            if right-left+1<min_len:
                min_len=right-left+1
                res=s[left:right+1]
            window[s[left]]-=1
            if s[left] in need and window[s[left]]<need[s[left]]:
                have-=1
            left+=1
    return res 
    
s="ADOBECODEBANC"
t="ABC"
print(min_window(s,t))
           