class Solution:
    def nextPermutation(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(a)
        idx=-1
        i=n-1
        while(i>0):
            if(a[i-1]<a[i]):
                idx=i       # idx is a fixed no
                break
            i-=1
        if(idx==-1):
            a.reverse()
        else:    
            prev=idx    # prev is not fixed and will change if a smaller no. is found
            for j in range(idx+1, n):
                if(a[j]<=a[prev] and a[j]>a[idx-1]):
                    prev=j
            a[prev], a[idx-1] = a[idx-1], a[prev]   # 1,2,3,6,5,4 to 1,2,4,6,5,3
            arra=a[:idx]         #1,2,4
            arrb=a[idx:]         #6,5,3
            arrb=arrb[::-1]      #3,5,6
            arra.extend(arrb)    #1,2,4,3,5,6
            # or simply instead of last 4 lines arr[idx:]=reversed(arr[idx:])
            a.clear()
            for i in arra:
                a.append(i)


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
