#User function Template for python3
'''

str = [ ] ] ] ] [ [ ] [ [ ]
open stores no of open brackets
close stores no of closed brackets

'''

class Solution:
    def minimumNumberOfSwaps(self,s):
        open=0
        close=0
        unbalanced=0
        swaps=0
        for i in s:
            if i=='[':
                open+=1
                if(unbalanced>0):   # there is at least 1 closing bracket that has no open bracket before it
                    swaps=swaps+unbalanced  # move this open bracket to the left for those many number of closed brackets
                    unbalanced-=1   # now one pair is balanced, so decrease unbalanced count
            else:
                close+=1
                unbalanced=close-open   # check for no. of close brackets without an opening bracket before
        return swaps
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends
