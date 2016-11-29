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

def staircase(n):
	# Recursive
	if n == 1:
		return 1
	if n == 2:
		return 2
	if n == 3:
		return 4
	return staircase(n-1) + staircase(n-2) + staircase(n-3)
# same result, but take much longer time
print 'Recursive Approach'
print staircase(1) # 1
# print staircase(30) # 53798080
# print staircase(36) # 2082876103	


memory = {1:1, 2:2, 3:4}
def staircase(n):
    if n not in memory.keys():
        memory[n] = staircase(n-1) + staircase(n-2) + staircase(n-3)
    return memory[n] 
# using memory, much more efficient
print staircase(1) # 1
print staircase(30) # 53798080
print staircase(36) # 2082876103	

# DP approach
def staircase(n):
	if n < 0:
		return 0
	elif n <= 1:
		return 1

	paths = [None] * (n + 1)
	paths[0] = 1
	paths[1] = 1
	paths[2] = 2
	for i in range(3, n + 1):
		paths[i] = paths[i - 1] + paths[i - 2] + paths[i - 3]
	return paths[n]
print 'DP'
print staircase(1) # 1
print staircase(30) # 53798080
print staircase(36) # 2082876103	

# save space 
def staircase(n):
	if n < 0:
		return 0
	elif n <= 1:
		return 1

	paths = [1,1,2]
	for i in range(3, n + 1):
		count = paths[0] + paths[1] + paths[2]
		paths[0] = paths[1]
		paths[1] = paths[2]
		paths[2] = count
	return paths[2]

print 'Another DP save space version'
print staircase(1) # 1
print staircase(30) # 53798080
print staircase(36) # 2082876103	