## Test cases for ParkingSystem
from parking_system import ParkingSystem 
import pytest 

# Write test cases for state transitions

def test_parking_system():
    parking_system = ParkingSystem(1, 1, 0)
    
    # Test adding cars of valid types
    assert parking_system.addCar(1) == True  # Big car
    assert parking_system.addCar(2) == True  # Medium car
    assert parking_system.addCar(3) == False # Small car (no spots)
    
    # Test adding cars when spots are full
    assert parking_system.addCar(1) == False # Big car (no spots)
    assert parking_system.addCar(2) == False # Medium car (no spots)
    
    # Test adding cars of invalid types
    assert parking_system.addCar(0) == False # Invalid car type
    assert parking_system.addCar(4) == False # Invalid car type


def test_invalid_initialization():
    # Test with zero parking spots
    parking_system = ParkingSystem(0, 0, 0)
    assert not parking_system.addCar(1)
    assert not parking_system.addCar(2)
    assert not parking_system.addCar(3)
    
    # Test with negative parking spots (should be treated as zero)
    parking_system = ParkingSystem(-1, -1, -1)
    assert not parking_system.addCar(1)
    assert not parking_system.addCar(2)
    assert not parking_system.addCar(3)

def test_invalid_car_types():
    parking_system = ParkingSystem(1, 1, 1)
    assert not parking_system.addCar(0)  # Invalid car type
    assert not parking_system.addCar(4)  # Invalid car type
    assert not parking_system.addCar(-1) # Invalid car type
    assert parking_system.addCar(1)      # Valid car type

if __name__ == "__main__":
    pytest.main()
