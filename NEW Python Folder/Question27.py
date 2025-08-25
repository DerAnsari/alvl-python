class Vehicle:
    def __init__(self, ID, M, IA):
        self.ID = ID
        self.MaxSpeed = M
        self.CurrentSpeed = 0
        self.IncreaseAmmount = IA
        self.HorizontalPosition = 0

    def GetCurrentSpeed(self):
        return self.CurrentSpeed

    def GetIncreaseAmmount(self):
        return self.IncreaseAmmount

    def GetHorizontalPosition(self):
        return self.HorizontalPosition

    def GetMaxSpeed(self):
        return self.MaxSpeed

    def SetCurrentSpeed(self, C):
        self.CurrentSpeed = C

    def SetHorizontalPosition(self, H):
        self.HorizontalPosition = H

    def IncreaseSpeed(self):
        self.CurrentSpeed += self.IncreaseAmmount
        if self.CurrentSpeed > self.MaxSpeed:
            self.MaxSpeed = self.CurrentSpeed
        self.HorizontalPosition += self.CurrentSpeed

    def OutputCurrentPosition(self):  # ⬅ added method to class
        print("Current position =", self.GetHorizontalPosition())
        print("Current speed =", self.GetCurrentSpeed())


class Helicopter(Vehicle):
    def __init__(self, ID, M, IA, Vc, Mh):
        super().__init__(ID, M, IA)
        self.VerticalChange = Vc
        self.MaxHeight = Mh
        self.VerticalPosition = 0

    def GetVerticalPosition(self):
        return self.VerticalPosition

    def IncreaseSpeed(self):
        # Vertical movement
        self.VerticalPosition += self.VerticalChange
        if self.VerticalPosition > self.MaxHeight:
            self.VerticalPosition = self.MaxHeight

        # Horizontal movement
        new_speed = self.GetCurrentSpeed() + self.GetIncreaseAmmount()
        if new_speed > self.GetMaxSpeed():
            new_speed = self.GetMaxSpeed()
        self.SetCurrentSpeed(new_speed)
        self.SetHorizontalPosition(self.GetHorizontalPosition() + self.GetCurrentSpeed())

    def OutputCurrentPosition(self):  # ⬅ override for Helicopter
        print("Current position =", self.GetHorizontalPosition())
        print("Current speed =", self.GetCurrentSpeed())
        print("Current vertical position =", self.VerticalPosition)


# Example usage
Car = Vehicle("Tiger", 100, 20)
Heli1 = Helicopter("Lion", 350, 40, 3, 100)

Car.IncreaseSpeed()
Car.IncreaseSpeed()
Car.OutputCurrentPosition()

print("")

Heli1.IncreaseSpeed()
Heli1.IncreaseSpeed()
Heli1.OutputCurrentPosition()
