# -----------------------------
# -- Lists --
# -----------
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
myAwesomeList[0:3] = ["A","B","C"]
print(myAwesomeList)
print("#############################################################")
########################################################################
# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["O", "B", "S"]
myOldFriends = ["H", "W", "Z"]

myFriends.append("A")
myFriends.append(myOldFriends)
print(myFriends[4][1]) # Samah

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()

x = [1, 2, 3, 4, 5, "O", True, "O", "O"]
x.remove("O")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "O", 100]
z.reverse()
print(z)

# clear()

a = [1, 2, 3, 4]
a.clear() #Empty List
print(a)

# copy()

b = [1, 2, 3, 4]
c=b.copy()
print(b)  # Main List
print(c)  # Copied List

b.append(5)

print(b)  # Main List
print(c)  # Copied List

# count()

d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1)) #3

# index()

e = ["O", "A", "S", "R", "A", "R"]
print(e.index("R"))

# insert()

f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0,50)
print(f)

# pop()

g = [1, 2, 3, 4, 5, "A", "B"]

print(g.pop(-3))
print(g)
