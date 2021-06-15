# Methods Practice
#PART - A
def sorting(*language_list):
    for language in language_list:
        if language == 'Java':
            print("Java language found")

            for character in language:
                print(character)
        else:
            print("Java was not found")

sorting("Python", "JS","C++")
sorting("Python", "Java")
sorting("Python", "Java", "Go")

#PART - B

def tax_calculation (gross_salary, tax):

    net_salary = gross_salary * (1-tax)
    print("Net salary is : " +str(net_salary))
    return net_salary

def salary_limit_tester(net_salary_variable):

    if net_salary_variable >=5800:
        print("Success! The salary is : " +str(net_salary_variable))
    else:
        print("The Salary is under 5800, it is : " + str(net_salary_variable))

net_salary_1 = tax_calculation(5000,0.2)
salary_limit_tester(net_salary_1)

net_salary_2 = tax_calculation(6000, 0.2)
salary_limit_tester(net_salary_2)

net_salary_3 = tax_calculation(10000,0.2)
salary_limit_tester(net_salary_3)
