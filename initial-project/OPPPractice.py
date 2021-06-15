class Car():

    def __init__(self, car_data_list):
        self.car_data_list = car_data_list

    def insurance_calculation(self):
        year_of_release = self.car_data_list[0]
        car_price = self.car_data_list[1]
        model = self.car_data_list[2]

        if 2020>=year_of_release and 6000<=car_price <=17000:
            calculated_insurance = car_price * 0.05

        else:
            calculated_insurance = car_price * 0.07

        print("Calculated Insurance price for the model %s: , is %s " % (model,calculated_insurance))

    def doors_closed(self):
        doors_status = self.car_data_list[-1]
        if doors_status == True:
            print("Doors are closed")

        elif doors_status == False:
            print("Doors are open")

        else:
            print("Wrong value inserted")

    def get_car_data(self):
        print("The car model is %s, it was release at the year %s, and it costs %s " %(self.car_data_list[2], self.car_data_list[0], self.car_data_list[1]))

# List of ford
ford_focus_list = [2005, 5000,"ford_focus" , True]

# Instance of ford_focus
ford_focus_instance = Car(ford_focus_list)

# Execute methods for ford_focus instance
ford_focus_instance.insurance_calculation()
ford_focus_instance.doors_closed()
ford_focus_instance.get_car_data()

print("\n")

# List of Audi

audi_a3_list = [2011, 15000, "audi_a3", False]

# Instance of audi_a3
audi_a3_instance = Car (audi_a3_list)

# Execute methods for audi_a3
audi_a3_instance.insurance_calculation()
audi_a3_instance.doors_closed()
audi_a3_instance.get_car_data()
