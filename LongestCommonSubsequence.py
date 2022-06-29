#User function Template for python3

'''
                                  lcs(abc, ac)
                lcs(abc, a)                           lcs(ab, ac)
        lcs(ab,a)       lcs(abc, )            lcs(a,ac)               lcs(ab, a)
    lcs(a,a)  lcs(a, )                    lcs(,a)  lcs(a,a)        lcs(ab, )   lcs(a, a)
    
    
Example 1:

Input:
A = 6, B = 6
str1 = ABCDGH
str2 = AEDFHR
Output: 3
Explanation: LCS for input Sequences
“ABCDGH” and “AEDFHR” is “ADH” of
length 3.
Example 2:

Input:
A = 3, B = 2
str1 = ABC
str2 = AC
Output: 2
Explanation: LCS of "ABC" and "AC" is
"AC" of length 2.

'''

class Solution:
    
    def __init__(self):
        self.dp=[[-1 for i in range(1001)] for j in range(1001)]
        
    def func(self, x, y, s1, s2):
        
        if(x==-1 or y==-1): # reached the end of any string 
            return 0
            
        if(self.dp[x][y]!=-1):   # already processed
            return self.dp[x][y]
            
        if(s1[x]==s2[y]):   # equal found, 
            self.dp[x][y]=1+self.func(x-1, y-1, s1, s2)
            return self.dp[x][y]
            
        self.dp[x][y]=max(self.func(x, y-1, s1, s2), self.func(x-1, y, s1, s2))     # move back, once for 1st string, next for other string
        return self.dp[x][y]
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        return self.func(x-1, y-1, s1, s2)
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends
