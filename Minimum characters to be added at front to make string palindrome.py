def minCharsforPalindrome(s):

    # Write your code here
    n=len(s)
    i=0
    j=n-1
    c=0
    while(i<j):
        if(s[i]==s[j]):
            i+=1
            j-=1
        else:
            i=0
            c=n-j
            while(s[i]==s[j]):
                c-=1
                i+=1
            j-=1
    return c

'''

Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.

Input  : str = "AACECAAAA";
Output : 2
We can make above string palindrome as AAAACECAAAA
by adding two A's at front of string.

Approach :
Take left pointer as 0 and right and n-1 and compare both characters

If both are same left++ and right–;

else

we can think that we have to add N-right elements at front to make last (N-right) characters palindrome so added = (n-right)

Now left again point to 0 as we have to check the string from 0th index .

but if character at right position is same as 0th index char then we can add one less character at front  , now left will point to 1.

'''
