
salary = [1000,2000,3000,4000,5000,6000,7000,8000,9000]
for place in range(0, 6, 2):
    if place == 0:
        pass

    else:
        salary_with_bonus = salary[place] + place * 1000
        print(salary_with_bonus)