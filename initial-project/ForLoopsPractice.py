# Create a list of businesses
businesses_list = [1500, 2542, 2001, 3500, 5300, 5555, 17000, 21000, 10, 15001]
total_taxes = 0

for single_income in businesses_list:
    if single_income>=1 or single_income<=2000:

        tax = single_income * 0.05

    if single_income>=2001 and single_income<=5000:
        tax = single_income * 0.1

    if single_income>=5001 and single_income<=15000:
        tax = single_income * 0.15


    else:
        tax = single_income * 0.17

    net_income = single_income - tax
    income_after_healthcare_reduction = net_income * 0.98

    print("Printing income after healthcare reduction : " +str(income_after_healthcare_reduction))

    total_taxes = total_taxes + tax

    print("Print the total of taxes : " +str(total_taxes))

