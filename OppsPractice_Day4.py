# 1. Write a Python program to create a class named Car. Define attributes like brand, model, and year. Create an object of the class and display the details of the car?
# class Car:
#     brand="Hyundai"
#     model="Excel"
#     year=2024
# S1= Car()
# print(S1)
# print(S1.brand)
# print(S1.model)
# print(S1.year)
from math import degrees


# 2. Create a class Student with attributes name, roll_number, and marks. Define a constructor to initialize these attributes and a method display_info() to print the student's details?
# class Student:
#     def __init__(self, name, rollnumber, marks):
#         self.name=name
#         self.rollnumber=rollnumber
#         self.marks=marks
# S1=Student("Karan",32,99)
# print(S1)
# print(S1.name,S1.rollnumber,S1.marks)
# S2=Student("Arjun",1,100)
# print(S2)
# print(S2.name,S2.rollnumber,S2.marks)

# 3. Create a class Rectangle with attributes length and breadth. Include methods to calculate the area and perimeter of the rectangle. Create multiple objects and display the area and perimeter for each?
# class Rectangle:
#     def __init__(self,hieght,width):
#         self.hieght=hieght
#         self.width=width
# A1=Rectangle(10,20)
# perimeter=((2*(A1.hieght+A1.width)),"cm")
# Area=(A1.hieght*A1.width,"sqcm")
# print(A1)
# print(perimeter)
# print(Area)

# 4. Write a class Circle with an attribute radius and methods get_area() and get_circumference(). These methods should return the area and circumference of the circle, respectively ?
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
# c1=Circle(5)
# pie=3.14
# Area=pie*c1.radius*c1.radius
# Circumference=2*pie*c1.radius
# print(c1)
# print(Area)
# print(Circumference)

# Create Account class with 2 attributes - balance & account no. Create methods for debit, credit & printing the balance
# class Cards:
#     def __init__(self, accountno,balance):
#         self.accountno=accountno
#         self.balance=balance
# debitc1=Cards(8432140512,500)
# creditc1=Cards(5434206182,27000)
# print(debitc1.accountno,debitc1.balance)
# print(creditc1.accountno,creditc1.balance)

# Create a class Employee with an attribute employee_count (class variable) and a class method increment_employee_count() to increase the count whenever a new employee object is created. Show the updated employee count after creating new objects.
# class Employee:
#     # Class variable to store the number of employees
#     employee_count = 0
#
#     def __init__(self, name):
#         self.name = name
#         # Increment employee count when a new object is created
#         Employee.increment_employee_count()
#
#     @classmethod
#     def increment_employee_count(cls):
#         # Increment the employee count by 1
#         cls.employee_count += 1
#         print(f"Employee count updated: {cls.employee_count}")
#
# # Creating employee objects
# emp1 = Employee("John")
# emp2 = Employee("Alice")
# emp3 = Employee("Bob")
# emp4 = Employee("Zooba")

# Create a class Book with attributes title, author, and price. Write a constructor that allows the user to either initialize all three attributes or just the title and author (in which case the price should be set to a default value). Display the details of the book using an instance method.
# class Book:
#     def __init__(self, author,tittle,price=2.0):
#         self.author=author
#         self.tittle=tittle
#         self.price=price
#     def display_details(self):
#         print(f"Author : {self.author}")
#         print(f"Tittle : {self.tittle}")
#         print(f"Price : {self.price}")
# Book1=Book("Tarun","Gita",1000)
# Book2=Book("Meghali","DurgaSaptasati")#for default price
#
# Book1.display_details()
# print(Book1)
# Book2.display_details()
# print(Book2)

# 8. Write a class TemperatureConverter with an instance method celsius_to_fahrenheit(celsius) that takes a temperature in Celsius and returns its Fahrenheit equivalent. Create an object of the class and use the method to convert various temperatures.
# class TemperatureConvertor:
#     def celsius_to_fahernite(self, celcius):
#         fahernite=(celcius*9/5) +32
#         return fahernite
# convertor= TemperatureConvertor()
# tempin_fahernite_1=convertor.celsius_to_fahernite(0)
# tempin_fahernite_2=convertor.celsius_to_fahernite((90))
# tempin_fahernite_3=convertor.celsius_to_fahernite(45)
# print(f"0 C in Fahernite is :{tempin_fahernite_1}")
# print(f"90 C in Fahernite is :{tempin_fahernite_2}")
# print(f"45 C in Fahernite is :{tempin_fahernite_3}")


# class Time:
#     def __init__(self, hours=0, minutes=0):
#         # Initialize hours and minutes
#         self.hours = hours
#         self.minutes = minutes
#
#     def add_time(self, other_time):
#         # Add the minutes and hours from both Time objects
#         total_minutes = self.minutes + other_time.minutes
#         total_hours = self.hours + other_time.hours + total_minutes // 60  # Carry over extra minutes to hours
#         total_minutes = total_minutes % 60  # Remainder becomes the new minutes
#
#         # Return a new Time object with the sum
#         return Time(total_hours, total_minutes)
#
#     def display_time(self):
#         # Display time in a formatted way
#         print(f"{self.hours} hours, {self.minutes} minutes")
#
# # Creating two Time objects
# time1 = Time(2, 45)
# time2 = Time(1, 30)
#
# # Adding time1 and time2
# total_time = time1.add_time(time2)
#
# # Displaying the results
# print("Time 1:")
# time1.display_time()
# print("Time 2:")
# time2.display_time()
# print("Total time after addition:")
# total_time.display_time()

class EmployeeSalary:
    # Class variables for basic salary and bonus percentage
    basic_salary = 50000  # Default basic salary
    bonus_percentage = 10  # Default bonus percentage

    @classmethod
    def set_bonus_percentage(cls, new_bonus_percentage):
        # Class method to set a new bonus percentage for all employees
        cls.bonus_percentage = new_bonus_percentage

    def calculate_total_salary(self):
        # Calculate the total salary: basic salary + bonus
        bonus_amount = (EmployeeSalary.bonus_percentage / 100) * EmployeeSalary.basic_salary
        total_salary = EmployeeSalary.basic_salary + bonus_amount
        return total_salary

# Changing the bonus percentage for all employees using the class method
EmployeeSalary.set_bonus_percentage(15)

# Creating an EmployeeSalary object
employee1 = EmployeeSalary()

# Calculating and displaying the total salary for employee1
total_salary = employee1.calculate_total_salary()
print(f"Total salary for Employee 1: ${total_salary:.2f}")

# Creating another EmployeeSalary object
employee2 = EmployeeSalary()

# Calculating and displaying the total salary for employee2
total_salary2 = employee2.calculate_total_salary()
print(f"Total salary for Employee 2: ${total_salary2:.2f}")
