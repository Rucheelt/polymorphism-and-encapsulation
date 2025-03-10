class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Hello , i am a cat and my name is {self.name} and my age is {self.age}")
        print("I make the sound meow")


class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"Hello , i am a dog and my name is {self.name} and my age is {self.age}")
        print("I make the sound BOW called as barking")


c=cat("Pilli",3)
d=dog("Kukka",5)

for animals in c,d:
 animals.info()