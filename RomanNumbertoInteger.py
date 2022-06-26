#User function Template for python3

class Solution:
    
    def value(x):
        if(x=='I'):
            return 1
        if(x=='V'):
            return 5
        if(x=='X'):
            return 10
        if(x=='L'):
            return 50
        if(x=='C'):
            return 100
        if(x=='D'):
            return 500
        if(x=='M'):
            return 1000
        return -1
    
    def romanToDecimal(self, s):
        n=len(s)
        if(n==1):
            return Solution.value(s[0])
        i=0
        ans=0
        while(i<n-1):
            s1=Solution.value(s[i])
            s2=Solution.value(s[i+1])
            if(s1>=s2):
                ans+=s1
                i+=1
            else:
                ans+=(s2-s1)
                i+=2
        if(i==n-1):
            ans+=Solution.value(s[n-1])
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends


"""
THEORY : 

SYMBOL       VALUE
  I            1
  IV           4
  V            5
  IX           9
  X            10
  XL           40
  L            50
  XC           90
  C            100
  CD           400
  D            500
  CM           900 
  M            1000
Approach: A number in Roman Numerals is a string of these symbols written in descending order(e.g. M’s first, followed by D’s, etc.). However, in a few specific cases, to avoid four characters being repeated in succession(such as IIII or XXXX), subtractive notation is often used as follows: 

I placed before V or X indicates one less, so four is IV (one less than 5) and 9 is IX (one less than 10).
X placed before L or C indicates ten less, so forty is XL (10 less than 50) and 90 is XC (ten less than a hundred).
C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand).


MAIN ALGORITHM IN THE PROGRAM :

Algorithm to convert Roman Numerals to Integer Number:  

Split the Roman Numeral string into Roman Symbols (character).
Convert each symbol of Roman Numerals into the value it represents.
Take symbol one by one from starting from index 0: 
If current value of symbol is greater than or equal to the value of next symbol, then add this value to the running total.
else subtract this value by adding the value of next symbol to the running total.

"""
