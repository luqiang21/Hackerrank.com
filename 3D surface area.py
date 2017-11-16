'''
link to the problem https://www.hackerrank.com/contests/w35/challenges/3d-surface-area/problem
Madison, is a little girl who is fond of toys. Her friend Mason works in a toy
manufacturing factory . Mason has a 2D board  of size  with  rows and  columns.
The board is divided into cells of size  with each cell indicated by it's coordinate .
The cell  has an integer  written on it. To create the toy Mason stacks number of cubes of size  on the cell .

Given the description of the board showing the values of  and that the price of
the toy is equal to the 3d surface area find the price of the toy.


Input Format

The first line contains two space-separated integers  and  the height and the width of the board respectively.

The next  lines contains  space separated integers. The  integer in  line denotes .

Constraints

Output Format

Print the required answer, i.e the price of the toy, in one line.

Sample Input 0

1 1
1
Sample Output 0

6
Explanation 0


Sample Input 1

3 3
1 3 4
2 2 3
1 2 4
Sample Output 1

60
Explanation 1

The sample input corresponds to the figure described in problem statement.
'''
from tools import timing

@timing
def surfaceArea(A):
    # Complete this function
    rows = len(A)
    cols = len(A[0])
    # every cube has at least one surface not blocked
    surfaces = [[2 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            # compare with four neighbors
            if i == 0:
                surfaces[i][j] += A[i][j]
            else:
                surfaces[i][j] += max(0, A[i][j] - A[i-1][j])

            if j == 0:
                surfaces[i][j] += A[i][j]
            else:
                surfaces[i][j] += max(0, A[i][j] - A[i][j-1])

            if i == rows - 1:
                surfaces[i][j] += A[i][j]
            else:
                surfaces[i][j] += max(0, A[i][j] - A[i+1][j])

            if j == cols - 1:
                surfaces[i][j] += A[i][j]
            else:
                surfaces[i][j] += max(0, A[i][j] - A[i][j+1])
    #print(surfaces)
    return sum([sum(l) for l in surfaces])
A = [[1]]
result = surfaceArea(A)
print(result)

A = [[1, 3, 4],
     [2, 2, 3],
     [1, 2, 4]]
result = surfaceArea(A)
print(result)
