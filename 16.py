# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0

while a < 15:

  print(a)

  a += 1  # a = a + 1

print("Loop is Done")  # True Become False

while False:

  print("Will Not Print")

print("#"*50)
#################################################################################
# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myFriends = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF))  # List Length [10]

a = 0

while a < len(myFriends):  # a < 10

  print(f"#{str(a + 1).zfill(3)} {myFriends[a]}")

  a += 1  # a = a + 1

else:

  print("All Friends Printed To Screen.")
  
print("#"*50)
############################################################################
# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later
myFavouriteWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0:

  # Input The New Website
  web = input("Website Name Without https:// ")

  # Add The New Website To The List
  myFavouriteWebs.append(f"https://{web.strip().lower()}")

  # Decrease One Number From Allowed Websites
  maximumWebs -= 1  # maximumWebs = maximumWebs - 1

  # Print The Add Message
  print(f"Website Added, {maximumWebs} Places Left")

  # Print The List
  print(myFavouriteWebs)

else:

  print("Bookmark Is Full, You Cant Add More")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0:

  # Sort The List
  myFavouriteWebs.sort()

  index = 0

  print("Printing The List Of Websites in Your Bookmark")

  while index < len(myFavouriteWebs):

    print(myFavouriteWebs[index])

    index += 1  # index = index + 1