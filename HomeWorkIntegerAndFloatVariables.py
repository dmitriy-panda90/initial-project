gross_salary = 10000
health_insurance = 430.99
rent = 1200
food = 400.5
tax = 0.2 # 20%
donation_to_the_poor = 0.1 # 10%

# Calculate net salary
tax_amount_in_money = gross_salary * tax
net_salary = gross_salary - tax_amount_in_money - health_insurance -rent -food
print("Net salary : " +str (net_salary))

# Donation to poor, taken from net salary
donation_amount = net_salary * donation_to_the_poor

print("Donation amount in $ : " +str(round(donation_amount,2)))

print("Donation amount in $ : " + "{:.2f}".format(donation_amount))







