# Collections Dictionary Practice (Advanced)

# Create a dictionary of building attendants
build_attendants = {'floor_1' : {'first_apartment' : 'Rachel' , 'second_apartment' : 'Jeen'},
                    'floor_2' : {'third_apartment' : 'Jack'}}

print("(1) - Print of the dictionary : " +str(build_attendants))

# Extract the nested cell items
print("(2) - 1st floor items of the dictionary : " +str(build_attendants['floor_1']))

# Extract of who ever lives in the second apartment = 'Jeen'
print("(3) - Print of the attendant in the 2nd apartment : " +str(build_attendants['floor_1']['second_apartment']))

# Add a 4th apartment on floor 2
build_attendants['floor_2']['forth_apartment'] = "Carrol"

print("The dictionary after adding 'Carrol': " +str(build_attendants))

# Remove the 1st apartment of the dictionary
build_attendants['floor_1'].pop('first_apartment')
print("Print of the dictionary after removing 1st apartment : " + str(build_attendants))

