'''

Example 1:

Input: grid = {{a,b,c},{d,r,f},{g,h,i}},
word = "abc"
Output: {{0,0}}
Explanation: From (0,0) one can find "abc"
in horizontally right direction.
Example 2:

Input: grid = {{a,b,a,b},{a,b,e,b},{e,b,e,b}}
,word = "abe"
Output: {{0,0},{0,2},{1,0}}
Explanation: From (0,0) one can find "abe" in 
right-down diagonal. From (0,2) one can
find "abe" in left-down diagonal. From
(1,0) one can find "abe" in Horizontally right 
direction.

'''

'''

APPROACH 1:

'''

class Solution:
    
    def backtrack(self, mat,s,i,j,r,c, idx, slen, dn):
        found=False
        if(i>=0 and j>=0 and i<r and j<c and s[idx]==mat[i][j]):
            temp=mat[i][j]
            mat[i][j]=0     # mark as visited
            idx+=1
            obj=Solution()
            if(idx==slen):  # all letters in given string are covered
                found=True
                # found 1
            elif(dn=="none"):
                top=obj.backtrack(mat,s,i-1,j,r,c, idx, slen, "top")
                bottom=obj.backtrack(mat,s,i+1,j,r,c, idx, slen, "bottom")
                left=obj.backtrack(mat,s,i,j-1,r,c, idx, slen, "left")
                right=obj.backtrack(mat,s,i,j+1,r,c, idx, slen, "right")
                topleft=obj.backtrack(mat,s,i-1,j-1,r,c, idx, slen, "topleft")
                bottomright=obj.backtrack(mat,s,i+1,j+1,r,c, idx, slen, "bottomright")
                bottomleft=obj.backtrack(mat,s,i+1,j-1,r,c, idx, slen, "bottomleft")
                topright=obj.backtrack(mat,s,i-1,j+1,r,c, idx, slen, "topright")
                found=top or bottom or left or right or topleft or bottomright or bottomleft or topright
            elif(dn=="top"):
                found=obj.backtrack(mat,s,i-1,j,r,c, idx, slen, "top")
            elif(dn=="bottom"):
                found=obj.backtrack(mat,s,i+1,j,r,c, idx, slen, "bottom")
            elif(dn=="left"):
                found=obj.backtrack(mat,s,i,j-1,r,c, idx, slen, "left")
            elif(dn=="right"):
                found=obj.backtrack(mat,s,i,j+1,r,c, idx, slen, "right")
            elif(dn=="topleft"):
                found=obj.backtrack(mat,s,i-1,j-1,r,c, idx, slen, "topleft")
            elif(dn=="bottomright"):
                found=obj.backtrack(mat,s,i+1,j+1,r,c, idx, slen, "bottomright")
            elif(dn=="bottomleft"):
                found=obj.backtrack(mat,s,i+1,j-1,r,c, idx, slen, "bottomleft")
            else:
                found=obj.backtrack(mat,s,i-1,j+1,r,c, idx, slen, "topright")
            mat[i][j]=temp  # change visited mark i.e 0 to original character ( backtrack )
        return found
    
    def searchWord(self, mat, s):
        x=0
        cnt=0
        res=[]
        r=len(mat)
        c=len(mat[0])
        obj=Solution()
        for i in range(r):
            for j in range(c):
                found=obj.backtrack(mat, s, i, j, r, c, 0, len(s), "none")
                if(found):
                    res.append([i, j])
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n); m = int(m);
        grid = []
        for _ in range(n):
            cur  = input()
            temp = []
            for __ in cur:
                temp.append(__)
            grid.append(temp)
        word = input()
        obj = Solution()
        ans = obj.searchWord(grid, word)
        for _ in ans:
            for __ in _:
                print(__, end = " ")
            print()
        if len(ans)==0:
            print(-1)

# } Driver Code Ends


'''

APPROACH 2 (MODIFYING CountOccurencesOfAGivenWordIn2DArray.py)

'''



class Solution:
    
    def backtrack(self, mat,s,i,j,r,c, idx, slen, dn):
        found=0
        if(i>=0 and j>=0 and i<r and j<c and s[idx]==mat[i][j]):
            temp=mat[i][j]
            mat[i][j]=0     # mark as visited
            idx+=1
            obj=Solution()
            if(idx==slen):  # all letters in given string are covered
                found=1
                # found 1
            elif(dn=="none"):
                '''
                no need to found+= actually, it's used to count no. of words identified
                (this program is a modified version of CountOccurencesOfAGivenWordIn2DArray.py)
                but here even if one word is identified it's enough
                '''
                found+=obj.backtrack(mat,s,i-1,j,r,c, idx, slen, "top")
                found+=obj.backtrack(mat,s,i+1,j,r,c, idx, slen, "bottom")
                found+=obj.backtrack(mat,s,i,j-1,r,c, idx, slen, "left")
                found+=obj.backtrack(mat,s,i,j+1,r,c, idx, slen, "right")
                found+=obj.backtrack(mat,s,i-1,j-1,r,c, idx, slen, "topleft")
                found+=obj.backtrack(mat,s,i+1,j+1,r,c, idx, slen, "bottomright")
                found+=obj.backtrack(mat,s,i+1,j-1,r,c, idx, slen, "bottomleft")
                found+=obj.backtrack(mat,s,i-1,j+1,r,c, idx, slen, "topright")
            elif(dn=="top"):
                found+=obj.backtrack(mat,s,i-1,j,r,c, idx, slen, "top")
            elif(dn=="bottom"):
                found+=obj.backtrack(mat,s,i+1,j,r,c, idx, slen, "bottom")
            elif(dn=="left"):
                found+=obj.backtrack(mat,s,i,j-1,r,c, idx, slen, "left")
            elif(dn=="right"):
                found+=obj.backtrack(mat,s,i,j+1,r,c, idx, slen, "right")
            elif(dn=="topleft"):
                found+=obj.backtrack(mat,s,i-1,j-1,r,c, idx, slen, "topleft")
            elif(dn=="bottomright"):
                found+=obj.backtrack(mat,s,i+1,j+1,r,c, idx, slen, "bottomright")
            elif(dn=="bottomleft"):
                found+=obj.backtrack(mat,s,i+1,j-1,r,c, idx, slen, "bottomleft")
            else:
                found+=obj.backtrack(mat,s,i-1,j+1,r,c, idx, slen, "topright")
            mat[i][j]=temp  # change visited mark i.e 0 to original character ( backtrack )
        return found
    
    def searchWord(self, mat, s):
        x=0
        cnt=0
        res=[]
        r=len(mat)
        c=len(mat[0])
        obj=Solution()
        for i in range(r):
            for j in range(c):
                cnt=obj.backtrack(mat, s, i, j, r, c, 0, len(s), "none")
                if(cnt>0):
                    res.append([i, j])
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n); m = int(m);
        grid = []
        for _ in range(n):
            cur  = input()
            temp = []
            for __ in cur:
                temp.append(__)
            grid.append(temp)
        word = input()
        obj = Solution()
        ans = obj.searchWord(grid, word)
        for _ in ans:
            for __ in _:
                print(__, end = " ")
            print()
        if len(ans)==0:
            print(-1)

# } Driver Code Ends
