# If statements basics part 2

age = 30
name = 'James'

# Example number 1 - logical operator 'and'
if age>20 and name == 'James':
    print("Example 1 - My name is James, and I'm over 20")

else: print("Example1 - Default exist point")


# Example number 2 - Logical operator 'or'
if age > 20 or name =='James':
    print("Example 2 - My name is James, and I'm over 20")

else:
    print("Example 2 - Default exist point")

# Example - Nested 'if' statement
married = False
if age > 20  and name == 'James':
    if married == True:
        print("Example 3 - Good luck,its  gonna be a long (happy) ride : ")
    else: print("Example 3 - Nested 'else' ")
else: print("Example 3 - Parent 'else' ")

