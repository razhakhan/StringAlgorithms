class Solution:
    # Your task is to complete this function
    # Function should return an integer
    
    dp=[[]]
    
    def func(self, i, j, s):
        # initially i=0 and j=n-1
        if i>j:         # i exceeded j
            return 0
        elif i==j:      # i and j are at the same position
            return 1
        elif self.dp[i][j]!=-1:  # memoziation, using the value if already computed
            return self.dp[i][j]
        elif s[i]==s[j]:
            self.dp[i][j]=self.func(i+1, j, s)+self.func(i, j-1, s)+1    #eg. aba, b is a part of 2 palin. subseq. [aba, b]
            return self.dp[i][j]
        else:
            self.dp[i][j]=self.func(i+1, j, s)+self.func(i, j-1, s)-self.func(i+1, j-1, s)    # eg. abc, b is part of only 1 PSSQ : [b]
            return self.dp[i][j]
    
    def countPs(self,string):
        n=len(string)
        mod=1000000007
        self.dp=[[-1 for i in range(n)] for j in range(n)]
        return (self.func(0, n-1, string))%mod

#{ 
#  Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPs(input().strip()))

# } Driver Code Ends

"""

Example 1:

Input: 
Str = "abcd"
Output: 
4
Explanation:
palindromic subsequence are : "a" ,"b", "c" ,"d"
 

Example 2:

Input: 
Str = "aab"
Output: 
4
Explanation:
palindromic subsequence are :"a", "a", "b", "aa"

"""
