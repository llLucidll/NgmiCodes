class Robot:
    def __init__(self, position: tuple = (0, 0)):
        self.position = position 
        self._direction = 0 # Basically acts as the index of our availableDirs array.
        self.availableDirections = ["N", "E", "S", "W"]
    
    def status(self):
        x, y = self.position 
        return x, y, self.availableDirections[self._direction]
    
    def printHelpMessage(self):
        print("Hello Robot coming online!")
        print("Command the robot with")
        print("L - turn left")
        print("R - turn right")
        print("F - move forward")
        print("Q - shut down robot")
    
    def turnLeft(self):
        if self._direction == 0:
            self._direction = 3
        else:
            self._direction -= 1

    def turnRight(self):
        if self._direction == 3:
            self._direction = 0
        else:
            self._direction += 1
    
    def moveForward(self):
        direction = self.availableDirections[self._direction]
        if direction == "N":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "E":
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "S":
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "W":
            self.position = (self.position[0] - 1, self.position[1])
    
    def followCommand(self, command) -> bool:
        if command == "L":
            self.turnLeft()
        elif command == "R":
            self.turnRight()
        elif command == "F":
            self.moveForward()
        else:
            return False
        
        return True
    
    def __repr__(self) -> str:
        repr = f"Current Direction: {self.availableDirections[self._direction]} \n Current Position: X: {self.position[0]} Y: {self.position[1]}"
        return repr
    
    

def main():
    robot = Robot((0,0))
    robot.printHelpMessage()
    command = ""
    while command != "Q":
        command = input(">").strip().upper()[:1]
        response = robot.followCommand(command)
        if not response:
            print("Error: Invalid Command")
            robot.printHelpMessage()
    
    print("Robot Shutting Down")





        
