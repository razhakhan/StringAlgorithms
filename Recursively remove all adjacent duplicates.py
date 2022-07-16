#User function Template for python3

class Solution:
    def rremove (self, S):
		new=[]
        i=0
        n=len(S)
        while i<len(S):
            temp=0
            while (i<n-1 and S[i]==S[i+1]):
                temp=1
                i+=1
            if temp==0:
                new.append(S[i])
            i+=1
        if len(new)<n:
            return self.rremove(new)
        return ''.join(new)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends

'''

Example 1:

Input:
S = "geeksforgeek"
Output: "gksforgk"
Explanation: 
g(ee)ksforg(ee)k -> gksforgk

Example 2:

Input: 
S = "abccbccba"
Output: ""
Explanation: 
ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->""(empty string)

'''
