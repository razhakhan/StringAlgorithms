#User function Template for python3

class Solution:
    def LongestRepeatingSubsequence(self, s):
        
        n=len(s)
        s1=s # rows
        s2=s # columns
        dp=[["" for i in range(n+1)] for j in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if(s[i-1]==s[j-1] and i!=j):
                    dp[i][j]=dp[i-1][j-1]+s[i-1]    #when two characters match, we remove it from string, hence i-1, j-1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1], key=len)   # max of top and left
                    
        return len(dp[n][n])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.LongestRepeatingSubsequence(str)
        print(ans)

# } Driver Code Ends


"""

https://www.youtube.com/watch?v=ZqG89Z-dKpI

Example 1:

Input:
str = "axxxy"
Output: 2
Explanation:
The given array with indexes looks like
a x x x y 
0 1 2 3 4

The longest subsequence is "xx". 
It appears twice as explained below.

subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str 


subsequence B
x x
0 1  <-- index of subsequence B
------
2 3  <-- index of str 

We are able to use character 'x' 
(at index 2 in str) in both subsequences
as it appears on index 1 in subsequence A 
and index 0 in subsequence B.
Example 2:

Input:
str = "aab"
Output: 1
Explanation: 
The longest reapting subsequenece is "a".


"""
