import sys

def minimunMoves(arr, n):
	ans = sys.maxsize   #infinity
	# i loop is used to take a base string for the current iteration 
	# and find the rotations needed to make other strings equal to this string
	for i in range(n):  
		curr_count = 0  #no. of total rotations for current base string
		for j in range(n):  # j loop iterates all strings to compare with base string i
			tmp = arr[j] + arr[j]       # when j=1, tmp=1234112341 
			index = tmp.find(arr[i]) 
			# index = 4, it implies 4 elements should be rotated in 12341
			# to get 11234
			if (index == -1):   #if string not found, rotation not possible
				return -1
				
			curr_count += index #add the rotation cound for this jth string
		ans = min(curr_count, ans)  # find the base string i with the min rotations 
	return ans  #return ans

# Driver Code
if __name__ == "__main__":
	arr = ["11234", "12341", "34112"]
	n = len(arr)
	print( minimunMoves(arr, n))
