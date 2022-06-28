#User function Template for python3
'''
Example 1:

Input:
S = "001"
Output: 1
Explanation: 
We can flip the 0th bit to 1 to have
101.


Example 2:

Input:
S = "0001010111" 
Output: 2
Explanation: We can flip the 1st and 8th bit 
bit to have "0101010101"
101.


Explanation :
s=0001010111
1st case : make it 0101010101 i.e. even index =1 , odd index = 0, cost for transformation = c1
2nd case : make it 1010101010 i.e. even index = 0, odd index = 1,  cost for transformation = c2

'''

class Solution:
    def minFlips(self, s):
        c1=0
        c2=0
        n=len(s)
        for i in range(n):
            if(i&1 and s[i]=='0'):      # odd=0, checking for 1010101010
                c1+=1
            if(i%2==0 and s[i]=='1'):   # even=1, checking for 1010101010
                c1+=1
            if(i&1 and s[i]=='1'):      # odd=0, checking for 0101010101
                c2+=1
            if(i%2==0 and s[i]=='0'):   # even=1, checking for 0101010101
                c2+=1
        return min(c1, c2)
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        S=input()
        Obj=Solution()
        ans=Obj.minFlips(S)
        print(ans)
# } Driver Code Ends
