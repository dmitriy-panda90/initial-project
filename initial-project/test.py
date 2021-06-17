def my_function(country="Canda"):
    print("I am from " + country)


my_function("Italy")
my_function()
my_function("Germany")


def my_function2(x):
    return 5 * x


number = my_function2(5)
print(number)


def phone_brands(brand1, brand2, brand3):
    print("The 3rd brand is " + brand3)


phone_brands("Apple", "LG", "Xiaomi")


def clothing_companies(*clothing_companies):
    print("Tha last company is: " + clothing_companies[0])


clothing_companies("Nike", "Adidas", "Under Armour", "Saucony")


def companies(**company_info):
    print("His last company is " + company_info["model"])


companies(brand='Apple', model='Iphone_X')
