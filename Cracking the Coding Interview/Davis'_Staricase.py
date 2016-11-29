'''
Davis' staircase, climb by 1, 2 or 3 steps when given n stairs
in a staircase
'''
import numpy as np
def staircase(n):
	# this function is written based on discussion of this problem on 
	# the website
	A = [1,2,4]
	A.append(sum(A))
	A.append(A[1] + A[2] + A[3])
	M = np.array([[1,1,0],[1,0,1],[1,0,0]])
	An = np.array([[A[4], A[3], A[2]], [A[3],\
	 				A[2], A[1]], [A[2], A[1], A[0]]])
	if n < 5:
		return A[n-1]
	else:
		return np.dot(An, np.matrix(M)**(n-5)).item(0)
print staircase(1) # 1
print staircase(30) # 53798080
print staircase(36) # 2082876103