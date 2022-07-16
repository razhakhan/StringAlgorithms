#User function Template for python3


class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        sdic={}
        pdic={}
        slen=len(s)
        plen=len(p)
        if(slen<plen):
            return "-1"
        ans=len(s)
        
        for i in p:
            if i not in pdic:
                pdic[i]=1
            else:
                pdic[i]+=1
                
        for i in s:
            if i not in pdic:
                pdic[i]=-1

        n=len(pdic)
        c=0
        i=0
        j=0
        start=-1
        while(j<len(s)):
            
            ch=s[j]
            
            if s[j] not in sdic:
                sdic[ch]=1
            else:
                sdic[ch]+=1
                
            if(sdic[ch]<=pdic[ch]):
                c+=1
                
            if(c==plen):
                while(sdic[s[i]]>pdic[s[i]]):
                    sdic[s[i]]-=1
                    i+=1
            
                winlen=j-i+1
                if(winlen<ans):
                    ans=winlen
                    start=i
                
            j+=1
            
        if(start==-1):
                return "-1"
            
        return s[start : start+ans]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
        print(ob.smallestWindow(s,p))
# } Driver Code Ends


'''

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output: 
toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.
Example 2:

Input:
S = "zoomlazapzo"
P = "oza"
Output: 
apzo
Explanation: "apzo" is the smallest 
substring in which "oza" can be found.

'''
