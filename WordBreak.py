#User function Template for python

dp={}

def wordBreak(s, dic):
    n=len(s)
    if(n==0):       # when line="", n=0, that means full string processing is completed
        return 1
    if s in dp:     # if substring is already processed before, return the value
        return dp[s]
    
    for i in range(1, n+1):
        f=0         # flag variable
        substr=s[:i]    #substring till i
        if substr in dic:   
            f=1
        if f==1 and wordBreak(s[i:], dic)==1:   #recur for remaining string
            dp[s]=1     #substring s exists in dic
            return 1
    dp[s]=-1    # substring s doesnt exist in dic
    return 0
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        number_of_elements = int(input())
        dictionary = [word for word in input().strip().split()]
        line = input().strip()
        res = wordBreak(line, dictionary)
        if res:
            print(1)
        else:
            print(0)
# } Driver Code Ends

"""

Example 1:

Input:
n = 12
B = { "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream",
"man", "go", "mango" }
A = "ilike"
Output:
1
Explanation:
The string can be segmented as "i like".

Example 2:

Input:
n = 12
B = { "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream", 
"man", "go", "mango" }
A = "ilikesamsung"
Output:
1
Explanation:
The string can be segmented as 
"i like samsung" or "i like sam sung".

"""

