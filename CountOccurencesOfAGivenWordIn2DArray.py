#User function Template for python3

class Solution:
    
    def backtrack(self, mat,s,i,j,r,c, idx, slen):
        found=0
        if(i>=0 and j>=0 and i<r and j<c and s[idx]==mat[i][j]):
            temp=mat[i][j]
            mat[i][j]=0     # mark as visited
            idx+=1
            if(idx==slen):  # all letters in given string are covered
                found=1     # found 1
            else:
                obj=Solution()
                found+=obj.backtrack(mat,s,i-1,j,r,c, idx, slen)
                found+=obj.backtrack(mat,s,i+1,j,r,c, idx, slen)
                found+=obj.backtrack(mat,s,i,j-1,r,c, idx, slen)
                found+=obj.backtrack(mat,s,i,j+1,r,c, idx, slen)
            mat[i][j]=temp  # change visited mark i.e 0 to original character ( backtrack )
        return found
            
    
    def findOccurrence(self,mat,s):
        x=0
        cnt=0
        r=len(mat)
        c=len(mat[0])
        obj=Solution()
        for i in range(r):
            for j in range(c):
                cnt+=obj.backtrack(mat, s, i, j, r, c, 0, len(s))   
        return cnt

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        R=int(line[0])
        C=int(line[1])
        mat=[]
        for _ in range(R):
            mat.append( [x for x in input().strip().split()] )
        target=input()
        obj = Solution()
        print(obj.findOccurrence(mat,target))
# } Driver Code Ends


"""
Example 1:

Input: 
R = 4, C = 5
mat = {{S,N,B,S,N},
       {B,A,K,E,A},
       {B,K,B,B,K},
       {S,E,B,S,E}}
target = SNAKES
Output:
3
Explanation: 
S N B S N
B A K E A
B K B B K
S E B S E
Total occurrence of the word is 3
and denoted by color.

Example 2:

Input:
R = 3, C = 3 
mat = {{c,a,t},
       {a,t,c},
       {c,t,a}}
target = cat
Output:
5
Explanation: Same explanation
as first example.

"""
