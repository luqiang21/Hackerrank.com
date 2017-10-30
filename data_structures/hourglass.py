# Context
# Given a  2D Array, :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
#
# a b c
#   d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
#
# Task
# Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.
#
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.
#
# Input Format
#
# There are  lines of input, where each line contains  space-separated integers describing 2D Array ; every value in  will be in the inclusive range of  to .
#
# Constraints
#
# Output Format
#
# Print the largest (maximum) hourglass sum found in .
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output
#
# 19
# Explanation
#
#  contains the following hourglasses:
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0
#
# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0
#
# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0
#
# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0
# The hourglass with the maximum sum () is:
#
# 2 4 4
#   2
# 1 2 4
#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


total_m = -9 * 7 # minimum sum
for row in range(len(arr)-2):
    for col in range(len(arr[0])-2):
        tl = arr[row][col]
        tc = arr[row][col+1]
        tr = arr[row][col+2]
        mc = arr[row+1][col+1]
        bl = arr[row+2][col]
        bc = arr[row+2][col+1]
        br = arr[row+2][col+2]
        total = tl + tc + tr + mc + bl + bc + br
        total_m = max(total, total_m)
print(total_m)
