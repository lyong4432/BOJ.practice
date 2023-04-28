class FourCal:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        if self.second == 0:
            return 0 
        else:
            return self.first / self.second
    def mul(self):
        result = self.first * self.second
        return result

a = FourCal(3,5)
b = FourCal(6,2)
print(a.add(),b.mul())

# 상속
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(6,2)
print(a.pow())

# from 점프투파이썬
