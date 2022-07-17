'''
first check for str1 to str2 mapping then str2 to str1 mapping and don't forget to compare their length before all this

Time → O(N) 

Space → O(256)

'''



#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        dic1={}
        dic2={}
        
        m=len(str1)
        n=len(str2)
        
        if(m!=n):
            return False
        
        for i in range(m):
            dic1[ str1[i] ] = str2[i]
        
        for i in range(m):
            if( str2[i] != dic1[str1[i]] ):
                return False
                
        for i in range(n):
            dic2[str2[i]]=str1[i]
            
        for i in range(n):
            if( str1[i] != dic2[str2[i]] ):
                return False
        
        return True
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends


'''

Example 1:

Input:
str1 = aab
str2 = xxy
Output: 1
Explanation: There are two different
charactersin aab and xxy, i.e a and b
with frequency 2and 1 respectively.
Example 2:

Input:
str1 = aab
str2 = xyz
Output: 0
Explanation: There are two different
charactersin aab but there are three
different charactersin xyz. So there
won't be one to one mapping between
str1 and str2.


why we have to check mapping of both strings
For Input: 
pijthbsfy
fvladzpbf

It's Correct output is: 
0
'''
