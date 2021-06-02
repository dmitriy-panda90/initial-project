# Collections - Dictionary (basics)

# Create a new dictionary
new_employee = {'first_name' : 'David','salary' : 10000,'company' : 'Google'}

# Print the dictionary
print("Print the dictionary : " +str(new_employee))

# Get cell 'value' - first way
print("Get1 'value' of 'first_name' key : " +str(new_employee['first_name']))

# Get cell 'value' - second way
print("Get 'value' of 'salary' key : "+str(new_employee.get('salary')))

# Remove dictionary cell by using '.pop()'
new_employee.pop('salary')
print("Remove dictionary cell by using '.pop()' : " +str(new_employee))

# Print out all 'keys' of the dictionary
print("Get all 'keys' out of the dictionary : " +str(new_employee.keys()))

# Print out all 'values' of the dictionary
print("Get all 'values' out of the dictionary : " +str(new_employee.values()))

job_title_value = "developer"
new_dictionary = {'job_title': job_title_value }

print("Print the 'new dictionary' : " +str(new_dictionary))
print ('\n')
new_employee_a = {'one' : 'Hello','two' : 'my', 'three' : 'world'}
print(new_employee_a)

new_employee_a ['four']='Hi'
print(new_employee_a)

