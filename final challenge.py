class Car:
    def _init_(self, model, year, carnumber):
        self.model = model
        self.year = year
        self.carnumber = carnumber
        self.available = True  
    
    def display_details(self):
        print(f"Model: {self.model}, Year: {self.year}, Car Number: {self.carnumber}")
    
    def is_available(self):
        return self.available
    
    def rent(self):
        self.available = False
    
    def return_car(self):
        self.available = True

class CarRentalSystem:
    def _init_(self):
        self.available_cars = []
    
    def register_car(self, model, year, carnumber):
        car = Car(model, year, carnumber)
        self.available_cars.append(car)
        print(f"Car {car.model} registered successfully.")
    
    def display_available_cars(self):
        print("Available Cars:")
        for car in self.available_cars:
            if car.is_available():
                car.display_details()
    
    def rent_car(self):
        self.display_available_cars()
        car_model = input("Enter the model of the car you want to rent: ")
        
        for car in self.available_cars:
            if car.model == car_model and car.is_available():
                car.rent()
                print(f"Car {car.model} rented successfully.")
                return
        print(f"Car {car_model} is not available.")

if_name_ == "_main_":
 rental_system = CarRentalSystem()
 rental_system.register_car("Alto", 2017, "MP40AA0808")
 rental_system.register_car("Swift", 2019, "MP38DA0841")
 rental_system.register_car("Nexon", 2024, "MP18PA4444")

 rental_system.rent_car()    

