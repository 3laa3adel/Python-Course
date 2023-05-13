# -----------------------------
# -- Set --
# ---------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"A", "B", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"O", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"A", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "A", "One", "A", 1}
print(mySetFour)
print("###########################################################################")
####################################################################################
# -----------------
# -- Set Methods --
# -----------------

# clear()

a = {1, 2, 3}
a.clear()
print(a)

# union()

b = {"One", "Two", "Three"}
c = {"1", "2", "3"}
x = {"Zero", "Cool"}

print(b | c)
print(b.union(c, x))

# add()

d = {1, 2, 3, 4}
d.add(5)
d.add(6)
print(d)

# copy()

e = {1, 2, 3, 4}
f = e.copy()

print(e)
print(f)

e.add(6)

print(e)
print(f)

# remove()

g = {1, 2, 3, 4}
g.remove(1)
# g.remove(7)
print(g)

# discard()

h = {1, 2, 3, 4}
h.discard(1)
h.discard(7)
print(h)

# pop()

i = {"A", True, 1, 2, 3, 4, 5}
print(i.pop())#Random

# update()

j = {1, 2, 3}
k = {1, "A", "B", 2}
j.update({'Html', "Css"})
j.update(k)

print(j)
print("###########################################################################")
####################################################################################
# -----------------
# -- Set Methods --
# -----------------

# difference() Does Not Affect

a = {1, 2, 3, 4}
b = {1, 2, 3, "A", "B"}
print(a)
print(a.difference(b))  # a - b
print(a)

print("=" * 40)  # Separator

# difference_update() Affect

c = {1, 2, 3, 4}
d = {1, 2,"A", "B"}
print(c)
c.difference_update(d)  # c - d
print(c)

print("=" * 40)  # Separator

# intersection() Does Not Affect

e = {1, 2, 3, 4, "X", "A"}
f = {"A", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

print("=" * 40)  # Separator

# intersection_update() Affect

g = {1, 2, 3, 4, "X", "A"}
h = {"A", "X", 2}
print(g)
g.intersection_update(h)  # g & h
print(g)

print("=" * 40)  # Separator

# symmetric_difference() Does Not Affect

i = {1, 2, 3, 4, 5, "X"}
j = {"A", "B", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)

print("=" * 40)  # Separator

# symmetric_difference_update() Affect

k = {1, 2, 3, 4, 5, "X"}
l = {"A", "B", 1, 2, 4, "X"}
print(k)
#k.symmetric_difference_update(l)  # k ^ l
print(k^l)
print("###########################################################################")
####################################################################################
# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True