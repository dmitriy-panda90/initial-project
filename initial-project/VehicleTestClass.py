class Vehicle:
    def __init__(self, is_engine_running):
        self.is_engine_running = is_engine_running

    def engine_status(self):
        if self.is_engine_running == True:
            print("Engine is running")

        elif self.is_engine_running == False:
            print("Engine is off")

        else:
            print("Wrong value inserted")



class PrivateCar (Vehicle):
  def __init__(self, is_engine_running):
    self.is_engine_running = is_engine_running
    super().__init__(is_engine_running)

ford_focus = PrivateCar(True)
ford_focus.engine_status()




