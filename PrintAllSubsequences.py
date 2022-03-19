def ssq(t, i, n, s):
    if(i==n):
        # one sub sequence is reached
        print(t)
    else:
        # 2 choices : include and go forward, don't include and go forward
        ssq(t, i+1, n, s) # send recursion forward to next level without including i'th character
        t=t+s[i]    #   include i'th character
        ssq(t, i+1, n, s) # send recursion forward to next level after including i'th character
        
s="abc"
n=len(s)
ssq("", 0, n, s)
