# Collections - Lists, practice (basics)

cars = ["Bmw","Toyota","Tesla","Kia"]
print("Cars list print : " +str(cars))

# Print the 'one-before-last' item out of 'cars' list
print("One before last item of the list: " +str(cars[-2]))

# Compare list's item on index '1', to 'Toyota' string
print("Comparison between call '1' from 'cars', to 'Toyota' : " +str(cars[1]=='Toyota'))

# Create a new list called 'mixed_values'
mixed_values = ["Jim",3500,"Alex", 2.53,True]
print("Print the list mixed_values : " +str(mixed_values))

# Print out the values out 'mixed_values' , from the cels 0-3 (including '3'
print(mixed_values[0:4])

# Print out the value of index 6 out of "mixed_values"
# print(mixed_values[6])

# Add the value 'Alpha - Romeo' to the 'cars' list
cars.append("Alpha Romeo")
print("Cars list printed after adding 'Alpha-Romeo' : " +str(cars))

new_var = mixed_values[0] = "Hello"
mixed_values.append("Good")
print(mixed_values)

mixed_values.insert(3,15)
mixed_values.remove('Hello')
mixed_values.pop(1)
print(mixed_values)







