from sys import maxsize

class Solution:
    def findSubString(self, s):
        dic={}
        ans=len(s)
        for i in s:
            if i not in dic:
                dic[i]=0
        dic[s[0]]+=1
        n=len(dic)
        c=1
        i=0
        j=1
        while(i<=j and j<len(s)):
            if(c<n):
                if(dic[s[j]]==0):
                    c+=1
                dic[s[j]]+=1
                j+=1
            elif(c==n):
                ans=min(ans, j-i)
                if(dic[s[i]]==1):
                    c-=1
                dic[s[i]]-=1
                i+=1
        while(c==n):
            ans=min(ans, j-i)
            if(dic[s[i]]==1):
                c-=1
            dic[s[i]]-=1
            i+=1
        return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        str = input()
        ob=Solution()
        print(ob.findSubString(str))
        
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends

'''

Example 1:
Input : "AABBBCBBAC"
Output : 3
Explanation : Sub-string -> "BAC"

Example 2:
Input : "aaab"
Output : 2
Explanation : Sub-string -> "ab"
 
Example 3:
Input : "GEEKSGEEKSFOR"
Output : 8
Explanation : Sub-string -> "GEEKSFOR"

'''
