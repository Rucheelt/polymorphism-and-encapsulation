class phone:
    def __init__(self):
        self.__maxprice=1000
    def sell(self):
        print(f"the max price of the phone is {self.__maxprice}")
  
    
    def newmaxprice(self,price):
        self.__maxprice=price
    
c=phone()
c.sell()

c.__maxprice=1000
c.sell()

c.newmaxprice(900)
c.sell()