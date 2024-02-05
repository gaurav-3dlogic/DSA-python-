class Cat:

    def __init__(self):
        self.__sound = "meow"

    def speak(self):
        print(f"Cat says: {(self.__sound)}")


c = Cat()
c.speak()

# change the price
c.sound = "bow-wow"
c.speak()