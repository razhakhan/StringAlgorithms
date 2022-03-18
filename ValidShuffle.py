# valid shuffle : order of appearance of characters won't change

def validShuffle(s1, s2, res):
    n1=len(s1)
    n2=len(s2)
    k=len(res)
    if(k!=n1+n2):
        return False
    i=0
    j=0
    ptr=0
    while(ptr<k):
        if(i<n1 and s1[i]==res[ptr]):
            i+=1
        elif(j<n2 and s2[j]==res[ptr]):
            j+=1
        else:
            return False
        ptr+=1
    return True

s1="xy"
s2="12"
res="x1y2"
print(validShuffle(s1, s2, res))
