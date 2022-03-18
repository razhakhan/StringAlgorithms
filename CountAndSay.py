#User function Template for python3

class Solution:

    def lookandsay(self, n):
        if(n==1):
            return "1"
        if(n==2):
            return "11"
        else:
            s="11"
            for i in range(3, n+1):
                t=""
                c=1
                s+="$"
                for j in range(1, len(s)):
                    if(s[j]!=s[j-1]):
                        t+=str(c)
                        t+=s[j-1]
                        c=1
                    else:
                        c+=1
                s=t
            return t

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends

"""

Given an integer n. Return the nth row of the following look-and-say pattern.
1
11
21
1211
111221
Look-and-Say Pattern:

To generate a member of the sequence from the previous member, read off the digits of the previous member, counting the number of digits in groups of the same digit. For example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.
 


Example 1:

Input:
n = 5
Output: 111221
Explanation: The 5th row of the given pattern
will be 111221.
Example 2:

Input:
n = 3
Output: 21
Explanation: The 3rd row of the given pattern
will be 21.

"""


