''' Solution 1 (TLE in python, passed all TC in cpp) ''' 

class Solution:
    def transfigure(self, A, B): 
        m=len(A)
        n=len(B)
        if m!=n:
            return -1
        
        count = [0] * 256
 
        for i in range(n):          
            count[ord(A[i])] += 1   # +1 for A characters
            count[ord(B[i])] -= 1   # -1 for B characters
            
        for i in range(256):       # resultant should be zero if equal strings
            if count[i]:
                return -1
                
        ans=0
        i=m-1
        j=n-1
        while(i>=0):
            if(A[i]==B[j]):
                j-=1
            else:
                ans+=1  # add the unmatched char at the start
            i-=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))


# } Driver Code Ends

''' Solution 2 Passed all TC '''


class Solution:
    def transfigure(self, A, B):
      
        from collections import Counter
        if Counter(A) != Counter(B):
            return -1
 
        ans=0
        i=j=len(A)-1
        while(i>=0):
            if(A[i]==B[j]):
                j-=1
            i-=1
        return j+1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        A = line[0]
        B = line[1]
        obj = Solution();
        print(obj.transfigure(A,B))


# } Driver Code Ends


'''

Example 1:

Input: 
A = "GEEKSFORGEEKS" 
B = "FORGEEKSGEEKS"
Output: 3
Explanation:The conversion can take place 
in 3 operations:
1. Pick 'R' and place it at the front, 
   A="RGEEKSFOGEEKS"
2. Pick 'O' and place it at the front, 
   A="ORGEEKSFGEEKS"
3. Pick 'F' and place it at the front, 
   A="FORGEEKSGEEKS"
Example 2:

Input: 
A = "ABC" 
B = "BCA"
Output: 2
Explanation: The conversion can take place 
in 2 operations:
1. Pick 'C' and place it at the front, 
   A = "CAB"
2. Pick 'B' and place it at the front, 
   A = "BCA"

'''
