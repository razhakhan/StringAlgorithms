# cook your dish here
def possible(n, s):
    st={}
    c=0
    ans=0
    for i in range(len(s)):
        ch=s[i]
        if ch not in st:
            st[ch]=1    # in the cafe
            if c<n:
                st[ch]=2    # in the cafe, and computer is assigned
                c+=1
            else:
                ans+=1  # computer not assigned
        else:
            if st[ch]==2:
                c-=1    # decrease cnt for only computer using guys, not for waiting 
            del st[ch]  # pop out irrespective of waiting list users or present users of computer
    return ans

# n=int(input())
# s=input()
# print(possible(n, s))

print (possible(2, "ABBAJJKZKZ"))
print (possible(3, "GACCBDDBAGEE"))
print (possible(3, "GACCBGDDBAEE"))
print (possible(1, "ABCBCA"))
print (possible(1, "ABCBCADEED"))


'''

runCustomerSimulation (2, “ABBAJJKZKZ”) should return 0
runCustomerSimulation (3, “GACCBDDBAGEE”) should return 1 as ‘D’ was not able to get any computer
runCustomerSimulation (3, “GACCBGDDBAEE”) should return 0
runCustomerSimulation (1, “ABCBCA”) should return 2 as ‘B’ and ‘C’ were not able to get any computer.
runCustomerSimulation(1, “ABCBCADEED”) should return 3 as ‘B’, ‘C’ and ‘E’ were not able to get any computer.

'''
