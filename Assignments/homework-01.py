"""
Name: Andrew Bomer
Email: bomer.andrew@yahoo.com
Assignment: Homework 1 - Lists and Dictionaries
Due: 19 Sep @ 1:00 p.m.
"""

"""
Question A:
"""
a = [1, 5, 4, 2, 3] 
print(a[0], a[-1])
# Prints: 1 3

a[4] = a[2] + a[-2]
print(a)
# Prints: [1, 5, 4, 2, 6]

print(len(a))
# Prints: 5

print(4 in a)
# Prints: True

a[1] = [a[1], a[0]]
print(a)
# Prints: [1, [5, 1], 4, 2, 6]


"""
Question B:
"""
b = [1, 2, 3, 1, 4, 5, 1, 3]

def remove_all(x, lst):
	while x in lst:
		lst.remove(x)
	
remove_all(1, b)
print(b)


"""
Question C:
"""
def add_this_many(x, y, lst):
	for x in range(0, x):
		lst.append(y)

add_this_many(3, 4, b)
print(b)


"""
Question D:
"""
d = [3, 1, 4, 2, 5, 3]
print(d[:4])
# Prints: [3, 1, 4, 2]

print(d)
# Prints: [3, 1, 4, 2, 5, 3]

print(d[1::2])
# Prints: [1, 2, 3]

print(d[:])
# Prints: [3, 1, 4, 2, 5, 3]

print(d[4:2])
# Prints: []

print(d[1:-2])
# Prints: [1, 4, 2]

print(d[::-1])
# Prints: [3, 5, 2, 4, 1, 3]


"""
Question E:
"""
def reverse(lst):
	lst.reverse()

reverse(d)
print(d)


"""
Question F:
"""
z = [1, 2, 3, 4, 5, 6]

def rotate(lst, x):
	
	
rotate(z,3)
print(z)




"""
Question H:
"""
superbowls = {'joe montana': 4, 'tom brady':3, 'joe flacco': 0}
print(superbowls['tom brady'])

superbowls['peyton manning'] = 1
print(superbowls)

superbowls['joe flacco'] = 1
print(superbowls)

print('colin kaepernick' in superbowls)
#Prints: False

print(len(superbowls))
#Prints: 4

print(superbowls['peyton manning'] == superbowls['joe montana'])
#Prints: False

superbowls[('eli manning', 'giants')] = 2
print(superbowls)
#Prints: {'joe flacco': 1, ('eli manning', 'giants'): 2, 'peyton manning': 1, 'joe montana': 4, 'tom brady': 3}

superbowls[3] = 'cat'
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 3: 'cat', 'tom brady': 3, 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}


superbowls[('eli manning', 'giants')] =  superbowls['joe montana'] + superbowls['peyton manning']
print(superbowls)
#Prints: {('eli manning', 'giants'): 2, 3: 'cat', 'tom brady': 3, 'peyton manning': 1, 'joe montana': 4, 'joe flacco': 1}

superbowls['steelers', '49ers'] = 11
print(superbowls)
#Prints: {'joe montana': 4, ('steelers', '49ers'): 11, 'joe flacco': 1, 3: 'cat', 'peyton manning': 1, ('eli manning', 'giants'): 5, 'tom brady': 3}


"""
Question I:
"""
e = {1: {2:3, 3:4}, 2:{4:4, 5:3}}

def replace_all(d, x, y):
	for ky in d.keys():
		if type(d[ky]) == dict:
			replace_all(d[ky], x, y)
		else:
			d[ky] = y if d[ky] == x else d[ky]
			
replace_all(e, 3, 8)
print(e)


"""
Question J:
"""
f = {1:2, 2:3, 3:2, 4:3}

def rm(d, x):
	dlt = [ky for ky in d if d[ky] == x]
	for ky in dlt:
		del d[ky]

rm(f, 2)
print(f)
