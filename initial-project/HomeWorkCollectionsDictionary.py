# Create a dictionary about 'Alex'
alex = {'Age' : 32, 'Married' : 'Yes', 'Kids' : 3}

print("Alex's dictionary before 'update' : " +str(alex))

alex ['Age'] = 33
alex ['Kids'] = 4
alex ['Married'] = 'No'

alex_update_value_age = {'Age' : 35}
alex_update_value_marr = {'Married' : 'No'}
alex_update_value_kids = {'Kids' : 10}

alex.update(alex_update_value_age)
alex.update(alex_update_value_marr)
alex.update(alex_update_value_kids)

print("Alex's dictionary after 'update' : " +str(alex))

print("Get all 'values' out of the dictionary : " + str(alex.values()))
print("Get all 'keys' out of the dictionary : " + str(alex.keys()))

joe = {'Age' : 35, 'Kids': {'David': 'Boy', 'Ela' : 'Girl'}}
joe['City'] = 'Haifa'

joe_new = joe.copy()
print(joe_new)

joe_new.clear()
print(joe_new)













