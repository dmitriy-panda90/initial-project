# Create dictionary of employees
employees = {"Jack":6, "Russel":10, "Keren":2}

print("Print of employees dictionary " +str(employees))

# Find an employee for 5-8 hours, use 'elif'

if employees ["Jack"] >= 5 and employees ["Jack"] <=8:
     print("Take Jack for this one")
elif employees["Russel"] >= 5 and employees["Russel"] <= 8:
      print("Russel is the MAN for this job!")
elif employees["Keren"] >= 5 and employees["Keren"] <= 8:
       print("Take Keren for this shift")
else:
    print("Default exist point")

# Find someone to work the weekend, available for 2 - 4 hours
if employees ["Jack"] == 2 or employees ["Jack"] ==4:
     print("Jack is selected for the weekend shift")
elif employees["Russel"] == 2 or employees["Russel"] == 4:
      print("Russel fits for weekend shift")
elif employees["Keren"] == 2 or employees["Keren"] == 4:
       print("Keren will go work the weekend")

       if employees["Keren"] == 2:
           print("xxxxx")
       elif employees["Keren"] == 4:
           pass
       else:
           print("Nested 'else' print")
else:
    print("Print the 'else' default exist point")

# Find someone to work the weekend, available for 2 - 4 hours