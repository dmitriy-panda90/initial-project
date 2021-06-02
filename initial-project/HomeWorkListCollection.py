# Create a list of employees
list_of_employees = ["Adam", "John", "Greg", "Danna", "Ashly"]

# Print the list and length of the list
print("List of employees : " +str(list_of_employees))
print("Length of the list: " + str(len(list_of_employees)))

# Add new employee
new_employee_a = list_of_employees[1] = "Jack"
print("List after adding 'Jack' instead 'John': " +str(list_of_employees))

# Add new employee
new_employee_b = list_of_employees.insert(3,"Mavrik")
print("List after adding 'Mavrik' into index '3': " +str(list_of_employees))

# Remove employee from the 'list_of_employees'
remove_employee = list_of_employees.remove("Mavrik")
print("List after removed 'Mavrik' : " +str(list_of_employees))

# Add employee to last int the list
add_employee = list_of_employees.append("Mavrik")
print("List after adding employee to last in the list : " +str(list_of_employees))

# Remove employee from list (pop)
remove_employee = list_of_employees.pop(5)
print("List after removing employee : " +str(list_of_employees))

# Sort list
print(sorted(list_of_employees))

numbers = [5,9,4,1,6,3,8,7,52,41,652,88]
print(sorted(numbers,reverse=True))






