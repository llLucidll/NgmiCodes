class Car:
    def __init__(self, id: int, make: str, model: str, year: int):
        self.id = id
        self.make = make
        self.model = model 
        self.year = year 
        self._status = True # Status if the car is rented or not

    def __repr__(self) -> str:
        return f"Car Make: {self.make} ; Car Model: {self.model} ; Car Year: {self.year} ; Car status: {self.status}" 
    
    def available(self):
        return self._status
    def setStatus(self, status: bool):
        self._status = status     

class CarRental:
    def __init__(self, cars):
        self.cars = cars # Cars is initially a hashmap of Car objects
    
    # returns a list of cars that fit the available criteria
    def displayCars(self, make, model, year):
        available = [] 
        
        for _, car in self.cars.items():
            if car.available() == True:
                if make == None or car.make == make:
                    if model == None or car.model == model:
                        if year == None or car.year == year:
                            available.append(car)
        
        return available 
    
    def rentCar(self, car_id) -> bool:
        chosenCar = self.cars.get(car_id, None) 

        # Exception Handling
        if chosenCar == None:
            raise ValueError("Car does not exist")

        if chosenCar.available() == False:
            raise ValueError("Car is not available to rent")
        
        chosenCar.setStatus(False)
        return True
    
    def returnCar(self, car_id) -> bool:
        returnCar = self.cars.get(car_id, None)

        if returnCar == None:
            raise ValueError("Cannot return a car that isn't in rental company")

        if returnCar.available() == True:
            raise ValueError("Car cannot be returned as it is not rented")
        
        returnCar.setStatus(True)
        return True 






