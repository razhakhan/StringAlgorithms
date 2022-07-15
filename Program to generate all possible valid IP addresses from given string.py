#Your Function should return a list containing all possible IP address
#No need to worry about order

'''

https://www.youtube.com/watch?v=qu4W3idglP4

Example 1:

Input:
S = 1111
Output: 1.1.1.1
Example 2:

Input:
S = 55
Output: -1

'''


class Solution:
    
    def isValid(self, s):
        if(s[0]=='0'):  # starting with zero
            return False
        val=int(s)
        if(val<=255):   # less than equal to 255
            return True
        else:
            return False
        
    def helper(self, s, i, par, ans, res):
        # base case
        n=len(ans)
        if(i==len(s) or par==4):        # reached the last index or 4 parts are formed
            if(i==len(s) and par==4):   # reached the last index and 4 parts are formed, so valid IP is found
                res.append(ans[0:n-1])  # to remove dot at ending
            return                      # invalid ( for invalid IP, no appending it to res, directly return)
        
        # backtracking
        self.helper(s, i+1, par+1, ans+s[i]+'.', res)   # place dot after 1 character
        
        if(i+2<=len(s) and self.isValid(s[i:i+2])):     # place dot after 2 characters
            self.helper(s, i+2, par+1, ans+s[i:i+2]+'.', res)   
            
        if(i+3<=len(s) and self.isValid(s[i:i+3])):     # place dot after 3 characters
            self.helper(s, i+3, par+1, ans+s[i:i+3]+'.', res)
    
    def genIp(self, s):
        res=[]
        self.helper(s, 0, 0, "", res)
        return res

#{ 
#  Driver Code Starts
#Main
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
# } Driver Code Ends
