class Solution:
    def minstrlen(strs): # to find string with the minimum length
        m=1000000000
        for i in strs:
            if(len(i)<m):
                m=len(i)
        return m 
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        ans=""
        minlen=Solution.minstrlen(strs) 
        for i in range(minlen): 
            for j in range(1,n):
                if(strs[j][i]!=strs[0][i]): # comaring ith character of 1st string with ith character of all other strings
                    return ans              # return longest till now string if unequal is found  
            ans=ans+strs[0][i]              # if equal add it to the ans string and go to next character comparision
        return ans                          # when all strings are equal and same
      
""" 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
