#User function Template for python3

class Solution:
    def longestPalin(self, s):
        start=0
        end=1
        n=len(s)
        for i in range(1, n):
            
            # if the palindromic substring is even
            low=i-1
            high=i
            while(low>=0 and high<n and s[low]==s[high]):
                if(high-low+1>end):
                    start=low
                    end=high-low+1
                low-=1
                high+=1
        
            # if the palindromic substring is odd
            low=i-1
            high=i+1
            while(low>=0 and high<n and s[low]==s[high]):
                if(high-low+1>end):
                    start=low
                    end=high-low+1
                low-=1
                high+=1
                
        return s[start:start+end]
            
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends



"""

Example 1:

Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".
Example 2:

Input: 
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the 
longest palindromes with same length.
The result is the one with the least
starting index.

"""
