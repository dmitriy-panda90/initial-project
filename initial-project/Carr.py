class Car():

    def __init__(self, car_data_list):
        self.car_data_list = car_data_list

    def insurance_calculation(self):
         year_of_release = self.car_data_list[0]
         car_price = self.car_data_list[1]
         model = self.car_data_list[2]

         if 2020 >= year_of_release >= 2010 and 6000 <= car_price <= 17000:
             calculated_insurance = car_price * 0.05

         else:
             calculated_insurance = car_price * 0.07

         print("Calculated Insurance price is %s " %calculated_insurance)

    def doors_closed(self):
       pass
    def get_car_data(self):
       pass

# List of ford
ford_focus_list = [2005, 5000, "ford_focus", True]
ford_focus_insurance = Car(ford_focus_list)


audi_a3_list = [2011, 15000, "audi_a3", False]
