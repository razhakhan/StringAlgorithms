#User function Template for python3

class Solution:
    def nextPermutation(self, n, a):
        i=n-1
        while(i>0):
            if(a[i-1]>=a[i]):
                i-=1
            else:
                break
        if(i==0):
            return a[::-1]
        else:
            idx=i       # idx is a fixed no
            prev=idx    # prev is not fixed and will change if a smaller no. is found
            for j in range(idx+1, n):
                if(a[j]<a[prev] and a[j]>=a[idx-1]):
                    prev=j
            a[prev], a[idx-1] = a[idx-1], a[prev]
            arra=a[:idx]         #1,2,4
            arrb=a[idx:]         #6,5,3
            arrb=arrb[::-1]      #3,5,6
            arra.extend(arrb)    #1,2,4,3,5,6
            return arra

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends


"""

Example 1:

Input: N = 6
arr = {1, 2, 3, 6, 5, 4}
Output: {1, 2, 4, 3, 5, 6}
Explaination: The next permutation of the 
given array is {1, 2, 4, 3, 5, 6}.

Example 2:

Input: N = 3
arr = {3, 2, 1}
Output: {1, 2, 3}
Explaination: As arr[] is the last 
permutation. So, the next permutation 
is the lowest one.

"""
