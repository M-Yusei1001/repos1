class Formula:
    def __init__(self, name):
        self.name = name

    def driver_name(self, num):

        if num == 1:
            return "Max Verstappen"
        elif num == 2:
            return "Sergio Perez"
        
    def driver_number(self, num):

        if num == 1:
            return 1
        elif num == 2:
            return 11    