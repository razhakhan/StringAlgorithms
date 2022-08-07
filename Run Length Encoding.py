#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    n=len(arr)
    i=0
    s=""
    c=1
    while(i<n-1):
        if(arr[i]==arr[i+1]):
            c+=1
        else:
            s+=arr[i]
            s+=str(c)
            c=1
        i+=1
    s+=arr[n-1]
    s+=str(c)
    return s
    

#{ 
 # Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends

'''

Example 1:

Input:
str = aaaabbbccc
Output: a4b3c3
Explanation: a repeated 4 times
consecutively b 3 times, c also 3
times.
Example 2:

Input:
str = abbbcdddd
Output: a1b3c1d4


'''
