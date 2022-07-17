from typing import List


from typing import List


class Solution:
    
    ansmat=[]
    
    def dfs(self, mat, i, j, ans):
        ans[i]=mat[i][j]
        r=len(mat)
        c=len(mat[i])
        
        if i==r-1:
            temp=ans.copy()
            self.ansmat.append(temp)
            return
        
        if i+1<r:
            nc=len(mat[i+1])
            for k in range(nc):
                self.dfs(mat, i+1, k, ans)
    
    def sentences(self, mat : List[List[str]]) -> List[List[str]]:
        r=len(mat)
        c=len(mat[0])
        ans=[""]*r
        
        for i in range(c):
            self.dfs(mat, 0, i, ans)
            
        return self.ansmat

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class StringMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([str(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    
    a=IntArray().Input(2)
    
    
    list=StringMatrix().Input(a[0], a[1])
    
    obj = Solution()
    res = obj.sentences(list)
    
    StringMatrix().Print(res)
    

# } Driver Code Ends


'''

Given a list of word lists How to print all sentences possible taking one word from a list at a time via recursion? 

Example: 

Input: {{"you", "we"},
        {"have", "are"},
        {"sleep", "eat", "drink"}}

Output:
  you have sleep
  you have eat
  you have drink
  you are sleep
  you are eat
  you are drink
  we have sleep
  we have eat
  we have drink
  we are sleep
  we are eat
  we are drink 
  
The idea is based on a simple depth-first traversal. We start from every word of the first list as the first word of an output sentence, then recur for the remaining lists.

'''
