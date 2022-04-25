#User function Template for python3

class Solution:
    dic = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]
    def printSequence(self,s):
        ans=""
        for i in s:
            if i==" ":      #if i is space,append 0
                ans+="0"
            else:
                ans+=self.dic[ord(i)-ord('A')]  # eg. ord(C)=67 ord(A)=65; index=  67-65=2; 
        return ans                              #value at 2 = 222; which is code for C


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        inputStr = input()

        solObj = Solution()

        print(solObj.printSequence(inputStr))
# } Driver Code Ends

"""

Example 1:

Input:
S = "GFG"
Output: 43334
Explanation: For 'G' press '4' one time.
For 'F' press '3' three times.
Example 2:

Input:
S = "HEY U"
Output: 4433999088
Explanation: For 'H' press '4' two times.
â€‹For 'E' press '3' two times. For 'Y' press '9' 
three times. For white space press '0' one time.
For 'U' press '8' two times.

"""
