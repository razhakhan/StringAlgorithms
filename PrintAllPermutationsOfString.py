def prints(arr,s,n):
    l=[]
    for i in range(s,n):
        l.append(arr[i])
    print("".join(l))
    return
    
def permutation(arr, s, n):
    if(s==n):
        prints(arr,0,n)
    for i in range(s, n):
        arr[i], arr[s] = arr[s], arr[i]
        permutation(arr, s+1, n)
        arr[i], arr[s]=arr[s], arr[i]
        
st="abc"
arr=list(st)
n=len(st)
permutation(arr,0,n)


"""
Alternative approach :

from itertools import *
S="abc"
l=["".join(i) for i in list(permutations(S))]
return sorted(l)

"""
