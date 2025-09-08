import pytest
from CarRentalSystem import Car, CarRental
## Car Tests

def test_set_status():
    car = Car(1, "BMW", "x7", "2020")
    car.setStatus(False)
    assert car.available == False


## Car Rental Tests


def test_rent_car():
    car = Car(1, "BMW", "x7", "2020")
    carRental = CarRental(car)
    assert car.available == True

    assert carRental.rentCar(car.id) == True

    
