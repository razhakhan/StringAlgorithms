"""

Given a binary string str of length N, the task is to find the maximum count of consecutive substrings str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.
Example: 
 

Input: str = “0100110101” 
Output: 4 
The required substrings are “01”, “0011”, “01” and “01”.
Input: str = “0111100010” 
Output: 3 

Input: str = “0000000000” 

Output: -1

"""



def findcnt(s):
    c0=0
    c1=0
    ans=0
    for i in s:
        if i=='0':
            c0+=1
        else:
            c1+=1
        if(c0==c1):
            ans+=1
    
    if(c0!=c1):
        return -1
    
    return ans

s=input()
print(findcnt(s))
