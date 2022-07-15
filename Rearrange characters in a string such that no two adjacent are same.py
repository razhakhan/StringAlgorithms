#User function Template for python3

class Solution :
    def rearrangeString(self, s):
        n=len(s)
        if(n==0):
            return ""
        dic={}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        mx = max(dic, key=dic.get)
        freq=dic[mx]
        
        if(freq>(n+1)//2):
            return '-1'
            
        res=[0]*n
        
        i=0
        while(freq):
            res[i]=mx
            i+=2
            freq-=1
        x=dic.pop(mx)
        
        for ele in dic:
            while(dic[ele]>0):
                i=1 if i>=n else i
                res[i]=ele
                i+=2
                dic[ele]-=1
        
        res="".join(res)
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=='-1':
            print(0)
        elif sorted(str1)!=sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i]==str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
        
# } Driver Code Ends
