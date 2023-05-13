# -------------
# -- Strings --
# -------------

myStringOne = 'This is Single Quote'
myStringTwo = "This is Double Quotes"

print(myStringOne)
print(myStringTwo)

myStringThree = 'This is Single Quote "Test"'
myStringFour = "This is Double Quotes 'Test'"

print(myStringThree)
print(myStringFour)

myStringFive = '''First
Second 'Test' "Test"
Third'''

myStringSix = """First
Second "Test" \\\ 'Test'
Third"""

print(myStringFive)
print(myStringSix)
print("#############################################################################")
######################################################################################
# ---------------------------------
# Strings Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

# Indexing ( Access Single Item )

myString = "I Love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First Character From End
print(myString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data

print(myString[0::1])  # Full Data
print(myString[::1])  # Full Data

print(myString[::2])
print(myString[::3])
print("#############################################################################")
######################################################################################
# ---------------------
# -- Strings Methods --
# ---------------------

# strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())

# zfill

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

# upper()

g = "hello"

print(g.upper())

# lower()

h = "HELLO"

print(h.lower())
print("#############################################################################")
######################################################################################
# ---------------------
# -- Strings Methods --
# ---------------------

# split() rsplit()

a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3))

# center()

e = "Hellooo"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @

# count()

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))
print("#############################################################################")
######################################################################################
