class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.parking = {1: big, 2: medium, 3: small}
    
    def validCarType(self, carType: int):
        return 1 <= carType <= 3
    
    def addCar(self, carType: int) -> bool:
        if not self.validCarType(carType):
            return False 

        if self.parking[carType] <= 0:
            return False 
    
        self.parking[carType] -= 1
        return True 