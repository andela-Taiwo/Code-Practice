"""
Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to are acceptable.

Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains space-separated integers describing an array of numbers .

Output Format

You must print the following lines:

    A decimal representing of the fraction of positive numbers in the array.
    A decimal representing of the fraction of negative numbers in the array.
    A decimal representing of the fraction of zeroes in the array

"""

#!/bin/python

import sys

counter_pos =long(0)
counter_neg = long(0)
counter_zero= long(0)
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
for number in arr:
    if number<0:
        counter_neg +=1
    elif number>0:
        counter_pos +=1
    else:
        counter_zero +=1
    
print("%.6f") %(float(counter_pos)/n)
print("%.6f") %(float(counter_neg)/n)
print("%.6f") %(float(counter_zero)/n)
