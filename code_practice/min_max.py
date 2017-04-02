#!/bin/python

"""
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Input Format

A single line of five space-separated integers.

Constraints

    Each integer is in the inclusive range .

Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

Sample Input

1 2 3 4 5

Sample Output

10 14


"""

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
arr =a,b,c,d,e
n = len(arr)
sum1 = long(0)
sum2 = long(0)
arr = sorted(arr)
for num in range(0,n-1):
    if(arr[num]>=1 and arr[num]<(1000000000)):
        sum1 += arr[num]
    else:
        sum2 +=0
for j in range(1,n):
    if(arr[j]>= 1 and arr[j] <(1000000000)):
        sum2 += arr[j]
    else:
        sum2 +=0
print sum1,
print sum2
