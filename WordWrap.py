#User function Template for python3

class Solution:
    def solveWordWrap(self, arr, k):
        inf=2147483647
        n=len(arr)
        
        dp=[0]*n    #calculates cost
        ans=[0]*n   #ans[i] stores the index of the ending word of the line starting with the word arr[i]
        
        dp[n-1]=0   #cost for last line is 0
        ans[n-1]=n-1    #last line ends with last word
        
        for i in range(n-2, -1, -1):    #back to front
            dp[i]=inf
            lenofline=-1
            for j in range(i, n):       # from i to n-1. (front to back)
                
                lenofline+=(arr[j]+1)   #add len of all words
                
                if(lenofline>k):    # if exceeds max line length
                    break
                
                if(j==n-1): # if currently processing last word, no need to calculate cost for spaces
                    cost=0
                else:
                    cost=(k-lenofline)*(k-lenofline)+dp[j+1]    #find square and add min cost of substring arr[j+1] to arr[n-1]
                    
                if(cost<dp[i]):     #cost of current set of words in the line
                    dp[i]=cost
                    ans[i]=j
                    
        return dp[0]
        
        """
        to print words in each line : 
        i = 0
        while (i < n):
            print(i + 1 , ans[i] + 1, end = " ")
            i = ans[i] + 1
            
        o/p: 1 1 2 3 4 4
        """

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        ans = obj.solveWordWrap(nums, k)
        print(ans)


# } Driver Code Ends


"""
Example 1:

Input: nums = {3,2,2,5}, k = 6
Output: 10
Explanation: Given a line can have 6
characters,
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 3
Line number 3: From word no. 4 to 4
So total cost = (6-3)2 + (6-2-2-1)2 = 32+12 = 10.
As in the first line word length = 3 thus
extra spaces = 6 - 3 = 3 and in the second line
there are two word of length 2 and there already
1 space between two word thus extra spaces
= 6 - 2 -2 -1 = 1. As mentioned in the problem
description there will be no extra spaces in
the last line. Placing first and second word
in first line and third word on second line
would take a cost of 02 + 42 = 16 (zero spaces
on first line and 6-2 = 4 spaces on second),
which isn't the minimum possible cost.
Example 2:

Input: nums = {3,2,2}, k = 4
Output: 5
Explanation: Given a line can have 4 
characters,
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 2
Line number 3: From word no. 3 to 3
Same explaination as above total cost
= (4 - 3)2 + (4 - 2)2 = 5.

"""
