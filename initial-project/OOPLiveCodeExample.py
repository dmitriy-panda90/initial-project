class Building():

    def __init__(self, season_in_year, apartment_number, apartment_size):
        self.season_in_year = season_in_year
        self.apartment_number = apartment_number
        self.apartment_size = apartment_size

    def rent_calculation(self):

        base_price_per_month = 2000
        season_price_buffer = 0

        if self.season_in_year == "summer":
            season_price_buffer = 1.5

        elif self.season_in_year == "winter":
            season_price_buffer = 1.1

        elif self.season_in_year == "spring":
            season_price_buffer = 1.3

        elif self.season_in_year == "autumn":
            season_price_buffer == 1.2

        else:
            season_price_buffer = None

        if self.apartment_size > 130:
            season_price_buffer += 0.1

        total_rent_price = base_price_per_month * season_price_buffer

        # String Formatting
        print("The buffer is :%s" % season_price_buffer)
        print("The total price is %s" % (total_rent_price))

        return total_rent_price

    def montly_maintenance_pay(self, rent_price):

        maintenance = 0

        if rent_price > 3000:
            maintenance = 100

        else:
            maintenance = 50

        print("The maintenance is : %s " % maintenance)


lease_contract_1 = Building("summer", 4, 135)
rent_price_1 = lease_contract_1.rent_calculation()

lease_contract_1.montly_maintenance_pay(rent_price_1)

lease_contract_2 = Building("spring", 6, 100)

rent_price_2 = lease_contract_2.rent_calculation()
lease_contract_2.montly_maintenance_pay(rent_price_2)
