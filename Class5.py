# class MathOperations:
#     @staticmethod
#     def add_numbers(a, b):
#         return a + b
#
# # Example usage:
# result = MathOperations.add_numbers(5, 3)
# print(result)  # Output: 8
# class MathOperations:
#     @staticmethod
#     def multiply_numbers(a, b):
#         return a * b
#
# # Example usage:
# result = MathOperations.multiply_numbers(5, 3)
# print(result)  # Output: 15
# class Person:
#     # Class variable to count instances
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         # Increment the count each time a new instance is created
#         Person.count += 1
#
#     @classmethod
#     def get_count(cls):
#         # Class method to return the current count
#         return cls.count
#
# # Example usage:
# person1 = Person("Alice")
# person2 = Person("Bob")
# person3 = Person("Charlie")
#
# print(f"Number of people created: {Person.get_count()}")  # Output: 3
# class TemperatureConverter:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32
#
# # Example usage:
# temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(25)
# print(f"25°C is {temp_in_fahrenheit}°F")  # Output: 25°C is 77.0°F
# 8# Output: Animal sound
# class Animal:
#     def sound(self):
#         print("Animal sound")
#
# class Dog(Animal):
#     def sound(self):
#         print("Bark")
#
# # Example usage:
# animal = Animal()
# animal.sound()  # Output: Animal sound
#
# dog = Dog()
# dog.sound()  # Output: Bark
# class Bird:
#     def fly(self):
#         print("Flying")
#
# # Example usage:
# bird = Bird()
# bird.fly()  # Output: Flying
# class Fish:
#     def swim(self):
#         print("Swimming")
#
# # Example usage:
# fish = Fish()
# fish.swim()  # Output: Swimming
# class Bird:
#     def fly(self):
#         print("Flying")
#
# class Fish:
#     def swim(self):
#         print("Swimming")
#
# class Duck(Bird, Fish):
#     def quack(self):
#         print("Quack")
#
# # Example usage:
# duck = Duck()
# duck.fly()   # Output: Flying
# duck.swim()  # Output: Swimming
# duck.quack() # Output: Quack
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# # Example of a concrete class that inherits from Shape
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# # Example usage:
# rectangle = Rectangle(5, 3)
# print(f"Area of the rectangle: {rectangle.area()}")  # Output: Area of the rectangle: 15
# from abc import ABC, abstractmethod
# import math
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
# # Example usage:
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
#
# print(f"Area of the circle: {circle.area():.2f}")  # Output: Area of the circle: 78.54
# print(f"Area of the rectangle: {rectangle.area()}") # Output: Area of the rectangle: 24
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdrew: ${amount:.2f}")
#         else:
#             print("Invalid withdrawal amount.")
#
#     def get_balance(self):
#         return self._balance
#
# # Example usage:
# account = BankAccount(100)  # Create an account with an initial balance of $100
# account.deposit(50)          # Deposit $50
# account.withdraw(30)         # Withdraw $30
# print(f"Current balance: ${account.get_balance():.2f}")  # Output: Current balance: $120.00
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#         """Deposits a positive amount to the account."""
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         """Withdraws a positive amount from the account if sufficient funds are available."""
#         if amount > 0:
#             if amount <= self._balance:
#                 self._balance -= amount
#                 print(f"Withdrew: ${amount:.2f}")
#             else:
#                 print("Insufficient funds for this withdrawal.")
#         else:
#             print("Withdrawal amount must be positive.")
#
#     def get_balance(self):
#         """Returns the current balance."""
#         return self._balance
#
# # Example usage:
# account = BankAccount(100)  # Create an account with an initial balance of $100
# account.deposit(50)          # D
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         """Initializes the bank account with an optional initial balance."""
#         self._balance = initial_balance  # Private attribute
#
#     def deposit(self, amount):
#         """Deposits a positive amount into the account."""
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposited: ${amount:.2f}")
#         else:
#             print("Deposit amount must be positive.")
#
#     def withdraw(self, amount):
#         """Withdraws a positive amount from the account if sufficient funds are available."""
#         if amount > 0:
#             if amount <= self._balance:
#                 self._balance -= amount
#                 print(f"Withdrew: ${amount:.2f}")
#             else:
#                 print("Insufficient funds for this withdrawal.")
#         else:
#             print("Withdrawal amount must be positive.")
#
#     def get_balance(self):
#         """Returns the current balance."""
#         return self._balance
#
# # Example usage:
# if __name__ == "__main__":
#     account = BankAccount(100)  # Create an account with an initial balance of $100
#     account.deposit(50)          # Deposit $50
#     account.withdraw(30)         # Withdraw $30
# class Cat:
#     def speak(self):
#         print("Meow")
#
# class Dog:
#     def speak(self):
#         print("Woof")
#
# # Example usage:
# cat = Cat()
# dog = Dog()
#
# cat.speak()  # Output: Meow
# dog.speak()  # Output: Woof
# class Cat:
#     def speak(self):
#         print("Meow")
#
# class Dog:
#     def speak(self):
#         print("Woof")
#
# # Example usage:
# cat = Cat()
# dog = Dog()
#
# cat.speak()  # Output: Meow
# dog.speak()  # Output: Woof
# class Calculator:
#     def add(self, a, b, c=0):
#         """Returns the sum of two or three numbers."""
#         return a + b + c
#
# # Example usage:
# calculator = Calculator()
#
# # Adding two numbers
# sum_two = calculator.add(5, 10)
# print(f"Sum of 5 and 10: {sum_two}")  # Output: Sum of 5 and 10: 15
#
# # Adding three numbers
# sum_three = calculator.add(5, 10, 15)
# print(f"Sum of 5, 10, and 15: {sum_three}")  # Output: Sum of 5, 10, and 15: 30
# class Calculator:
#     def add(self, *args):
#         """Returns the sum of two or three numbers."""
#         if len(args) == 2:
#             return args[0] + args[1]
#         elif len(args) == 3:
#             return args[0] + args[1] + args[2]
#         else:
#             raise TypeError("add() takes either 2 or 3 arguments")
#
# # Example usage:
# calculator = Calculator()
#
# # Adding two numbers
# sum_two = calculator.add(5, 10)
# print(f"Sum of 5 and 10: {sum_two}")  # Output: Sum of 5 and 10: 15
#
# # Adding three numbers
# sum_three = calculator.add(5, 10, 15)
# print(f"Sum of 5, 10, and 15: {sum_three}")  # Output: Sum of 5, 10, and 15: 30
# class Calculator:
#     def add(self, a, b, c=None):
#         if c is not None:
#             return a + b + c
#         return a + b
#
# # Example usage:
# calculator = Calculator()
#
# print(calculator.add(5, 10))      # Output: 15
# print(calculator.add(5, 10, 15))  # Output: 30
# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
# class Animal(LivingBeing):
#     def move(self):
#         print("Moving")
#
# class Plant(LivingBeing):
#     def grow(self):
#         print("Growing")
#
# class Human(LivingBeing):
#     def think(self):
#         print("Thinking")
#
# # Example usage:
# if __name__ == "__main__":
#     living_being = LivingBeing()
#     living_being.breathe()  # Output: Breathing
#
#     animal = Animal()
#     animal.breathe()  # Output: Breathing
#     animal.move()     # Output: Moving
#
#     plant = Plant()
#     plant.breathe()  # Output: Breathing
#     plant.grow()     # Output: Growing
#
#     human = Human()
#     human.breathe()  # Output: Breathing
#     human.think()    # Output: Thinking
# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
#
# class Dog(Mammal):
#     def bark(self):
#         print("Woof")
#
# class Cat(Mammal):
#     def meow(self):
#         print("Meow")
#
# # Example usage:
# if __name__ == "__main__":
#     living_being = LivingBeing()
#     living_being.breathe()  # Output: Breathing
#
#     mammal = Mammal()
#     mammal.breathe()  # Output: Breathing
#     mammal.walk()     # Output: Walking
#
#     dog = Dog()
#     dog.breathe()     # Output: Breathing
#     dog.walk()        # Output: Walking
#     dog.bark()        # Output: Woof
#
#     cat = Cat()
#     cat.breathe()     # Output: Breathing
#     cat.walk()        # Output: Walking
#     cat.meow()        # Output: Meow
# class LivingBeing:
#     def breathe(self):
#         print("Breathing")
#
# class Mammal(LivingBeing):
#     def walk(self):
#         print("Walking")
#
# class Human(Mammal):
#     def think(self):
#         print("Thinking")
#
# class Dog(Mammal):
#     def bark(self):
#         print("Woof")
#
# class Cat(Mammal):
#     def meow(self):
#         print("Meow")
#
# # Example usage:
# if __name__ == "__main__":
#     living_being = LivingBeing()
#     living_being.breathe()  # Output: Breathing
#
#     mammal = Mammal()
#     mammal.breathe()  # Output: Breathing
#     mammal.walk()     # Output: Walking
#
#     human = Human()
#     human.breathe()   # Output: Breathing
#     human.walk()      # Output: Walking
#     human.think()     # Output: Thinking
#
#     dog = Dog()
#     dog.breathe()     # Output: Breathing
#     dog.walk()        # Output: Walking
#     dog.bark()        # Output: Woof
#
#     cat = Cat()
#     cat.breathe()     # Output: Breathing
#     cat.walk()        # Output: Walking
#     cat.meow()        # Output: Meow












