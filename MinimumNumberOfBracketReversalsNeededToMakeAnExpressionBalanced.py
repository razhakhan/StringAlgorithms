
class Solution:
    
    pair={'{':'}', '[':']', '(':')'}
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        st=[]
        co=0    # count open braces
        cc=0    # count closing braces
        if(len(x)%2!=0):
            return -1
        else:
            for i in x:
                if i in self.pair:  # opening braces
                    st.append(i)
                    co+=1
                else:               # closing braces
                    if st:          
                        x=st.pop()
                        if(i==self.pair[x]):    # check if respective opening brace exists
                            co-=1
                            continue
                    else:                       # if doesnt exists or stack is empty
                        cc+=1
        
        co=co//2 if co%2==0 else (co//2)+1  # }} }{ {{{{ -> (3/2)+1=2 swaps ( at 1, 2) for co; 
        cc=cc//2 if cc%2==0 else (cc//2)+1  # }} }{ {{{{ -> (5/2)+1=3 swaps ( at 7, 5, 3) for cc; 
        return co+cc                        # 01 23 4567    
                                            # }} {{ {{        (if co or cc is even, swaps=c//2) 
                                            
def countRev (s):
    obj=Solution()
    x=obj.ispar(s)
    return x

#{ 
#  Driver Code Starts

t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# } Driver Code Ends

"""

Example 1:

Input:
S = "}{{}}{{{"
Output: 3
Explanation: One way to balance is:
"{{{}}{}}". There is no balanced sequence
that can be formed in lesser reversals.
â€‹Example 2:

Input: 
S = "{{}{{{}{{}}{{"
Output: -1
Explanation: There's no way we can balance
this sequence of braces.

"""
