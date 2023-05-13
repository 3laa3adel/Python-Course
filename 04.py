# ---------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)

a = "I Love Python"
#print(a.index("Py"))  # Index Number 7
#print(a.index("Py", 0, 10))  # Index Number 7
#print(a.index("P", 0, 5))  # Through Error

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(Width, Fill Char) ljust(Width, Fill Char)

c = "Hello"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Hello"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines() #Return All In List

e = """First Line
Second Line
Third Line"""

print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(8))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "hello_world"
eight = "HelloWorld100"
nine = "Hello--World100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())
print("###############################################################")
#############################################################################
# replace(Old Value, New Value, Count)

a = "Hello One Two Three One One"
print(a.replace("One", "1")) #"Hello 1 Two Three 1 1"
print(a.replace("One", "1", 1)) #"Hello 1 Two Three One One"
print(a.replace("One", "1", 2)) #"Hello 1 Two Three 1 One"

# join(Iterable)

myList = ["Python", "SQL", "Java"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))