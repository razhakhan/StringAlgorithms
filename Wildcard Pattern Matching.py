# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    
    dp=[[]]
    
    def helper(self, s, p, i, j):
        
        if i==-1 and j==-1:
            return 1
            
        if i==-1:
            for k in range(j):
                if p[k] != '*':
                    return 0
            return 1
            
        if j==-1:
            return 0
            
        if self.dp[i][j]!=-1:
            return self.dp[i][j]
            
        if s[i]==p[j] or p[j]=='?':
            self.dp[i][j]=self.helper(s,p,i-1,j-1)
            return self.dp[i][j]
            
        if p[j]=='*':
            x=self.helper(s,p,i-1,j)
            y=self.helper(s,p,i,j-1)
            self.dp[i][j]= x or y
            return self.dp[i][j]
        
        self.dp[i][j]=0
        return self.dp[i][j]
    
    def wildCard(self,pattern, string):
        plen=len(pattern)
        slen=len(string)
        self.dp=[[-1 for i in range(plen)] for j in range(slen)]
        return self.helper(string, pattern, slen-1, plen-1)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends

'''

Given two strings 'str' and a wildcard pattern 'pattern' of length N and M respectively,  You have to print '1' if the wildcard pattern is matched with str else print '0' .

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

Note: The matching should cover the entire str (not partial str).

 

Example 1:

Input:
pattern = "ba*a?"
str = "baaabab"
Output: 1
Explanation: replace '*' with "aab" and 
'?' with 'b'. 
Example 2:

Input:
pattern = "a*ab"
str = "baaabab"
Output: 0
Explanation: Because of'a' at first position,
pattern and str can't be matched. 

'''
