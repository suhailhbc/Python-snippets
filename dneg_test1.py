#!/usr/bin/env python

import time

A = '4622661'

print (time.time())
N = len(A)
result = 0
for i in range(N):
	for j in range(N):
		if A[i] == A[j]:
			result = max(result, abs(i - j))
print (result)
print (time.time())

print ("\n\n\n")

print (time.time())
result = 0
for i, j in enumerate(A):
	for x, n in enumerate(A):
		if A[i] == A[x]:
			result = max(result, abs(i - x))
print (result)
print (time.time())
