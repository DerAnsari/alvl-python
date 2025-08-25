class Employee:
    def __init__(self,N,P,J):
        self.__EmployeeNumber = N
        self.__HourlyPay = P
        self.__Jobtitle = J
        self.__PayYear2022 = [0.0 for _ in range(52)]

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self,weekNum,hourNum):
        self.__PayYear2022[weekNum - 1] = hourNum * self.__HourlyPay

    def GetTotalPay(self):
        total = 0
        for i in self.__PayYear2022:
            total += i
        return total

class Manager(Employee):
    def __init__(self,N,P,J,B):
        super().__init__(N,P,J)
        self.__BonusValue =B

    def SetPay(self,weekNum,hourNum):
        hourNum += self.__BonusValue / 100.0
        super().SetPay(self,weekNum,hourNum)

EmployeeArray = []