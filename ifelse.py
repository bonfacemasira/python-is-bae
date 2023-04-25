a = 33
b = 200

# An "if statement" is written by using the if keyword
if b > a:
    print(f"b({b}) is greater than a({a})")


# Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b")
print("A") if a > b else print("B")


print('A') if a > b else print('=') if a == b else print('B')

# And
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#   Or
if a > b or a > c:
    print("At least one of the conditions is True")

# Not
if not a > b:
  print("a is NOT greater than b")

# Nested If
x = 11
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
if a > b and c > a:
  print("Both conditions are True")

if a > b or a > c:
  print("At least one of the conditions is True")

if not a > b:
  print("a is NOT greater than b")

if a > b:
  pass