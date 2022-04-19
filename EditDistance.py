class Solution:
    def editDistance(self, s, t):
        m=len(s)
        n=len(t)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                
                if(i==0):           # if m pointer reached the end and n pointer didn't reach, 
                    dp[i][j]=j      # there will be n+1 deletion operations in the 2nd string
                elif(j==0):
                    dp[i][j]=i
                elif(s[i-1]==t[j-1]):         #if both characters are same, recur for the remaining string
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j])) # replace, insert, remove
                    
        return dp[m][n]
            

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        s, t = input().split()
        ob = Solution();
        ans = ob.editDistance(s, t)
        print(ans)
# } Driver Code Ends


"""
Given two strings s and t. Return the minimum number of operations required to convert s to t.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.

Input: 
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required 
inserting 's' between two 'e's of str1.
Example 2:

Input : 
s = "gfg", t = "gfg"
Output: 
0
Explanation: Both strings are same.
"""
