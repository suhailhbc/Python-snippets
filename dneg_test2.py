#!/usr/bin/env python

S = "13 DUP 5 DUP + DUP + -"
#S = "5 6 + -"

def listpop(lst):
	pop = 0
	if len(lst):
		pop = lst.pop()
	return (lst, pop)

ls = S.split(' ')

nls = []

for x in ls:
	if x.isdigit():
		nls.append(x)
	elif x == 'DUP':
		a = nls[len(nls) - 1]
		nls.append(str(a))
	elif x == 'POP':
		nls.pop()
	elif x == '+':
		a = nls[len(nls) - 1]
		b = nls[len(nls) - 2]
		nls = listpop(nls)[0]
		nls = listpop(nls)[0]
		addvalue = int(a) + int(b)
		nls.append(str(addvalue))
	elif x == '-':
		#import pdb; pdb.set_trace()
		a = nls[len(nls) - 1]
		b = nls[len(nls) - 2]
		nls = listpop(nls)[0]
		nls = listpop(nls)[0]
		subvalue = int(a) - int(b)
		nls.append(str(subvalue))
	print (nls)
#print (nls)
