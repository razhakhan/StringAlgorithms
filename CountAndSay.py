#User function Template for python3

class Solution:

    def lookandsay(self, n):
        if(n==1):
            return "1"
        if(n==2):
            return "11"
        else:
            s="11"
            for i in range(3, n+1):
                t=""
                c=1
                s+="$"
                for j in range(1, len(s)):
                    if(s[j]!=s[j-1]):
                        t+=str(c)
                        t+=s[j-1]
                        c=1
                    else:
                        c+=1
                s=t
            return t

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends
