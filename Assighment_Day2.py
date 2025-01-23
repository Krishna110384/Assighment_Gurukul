#Q1 Write a Program to find Maximum of 3 Numbers
# a = int(input("Enter First Number:"))
# b = int(input("Enter Second Number:"))
# c = int(input("Enter Third Number:"))
# max = a if a > b and a > c else b if b > c else c
# print("Maximum Value:", max)

#Q2 Write a Program to find Biggest of given 2 Numbers from the Key Board
# n1=int(input("Enter first Number:"))
# n2=int(input("Enter Second Number:"))
# if n1>n2:
#     print("N1 is biggest no :",n1)
# else:
#     print("N2 is biggest number :", n2)

#Q3 Write a Program to Check whether the given Number is in between 1 and 10?
# n3=int(input("Enter first Number:"))
# if n3>0 and n3<10:
#     print("No is between 1 & 10 :", n3)
# else:
#     print("No is not between 1 & 10",n3)

#Q4 Write a Python program that takes two numbers as input from the user and performs the following operations
# a=10
# b=10
# addition = a+b
# substraction = a-b
# multiplication = a*b
# FloatDivision= a/b
# FloorDivision= a/b
# mod= a%b
# print("Result for mathematical operation is shown below")
# print(addition)
# print(substraction)
# print(multiplication)
# print(FloatDivision)
# print(FloorDivision)
# print(mod)

#Q5 Write a Python program that checks whether a given number is even or odd using the modulus operator
# a1=int(input("Enter the no :"))
# if a1%2 ==0:
#     print("No is Even",a1)
# else:
#     print("No is odd:",a1)

#Q6 Write a Python program that takes a number as input from the user and checks if it is positive, negative, or zero
# a2=int(input("Enter the number:"))
# if a2>0:
#     print("The number is",a2,": positive")
# elif a2<0:
#     print("The number is", a2 , ": negative")
# else:
#     print("The no is zero")

#Q7 Write a Python program that calculates the grade of a student based on the marks entered by the user
# marks = int(input("Enter the percent of student :"))
# if marks>=90:
#     print("The Grade of student is A:",marks)
# elif marks >=80 and marks<90:
#     print("The Grade of student is B:", marks)
# elif marks >=70 and marks<80:
#     print("The Grade of student is C:", marks)
# elif marks >= 60 and marks<70:
#     print("The Grade of student is D:", marks)
# else:
#     print("The Grade of student is F:", marks)

#Q8 Write a Python program to create a text file called sample.txt and write the sentence "Hello, this is a sample file." to the file. Then, read and display the content from the file.
# filename="Sample.txt"
# with open (filename,"w") as file:
#     file.write("Hello this is a sample file")
# with open (filename,"r") as file:
#     content=file.read()
#     print(content)
#Q9 Write a Python program that reads a text file called data.txt and counts the number of words in the file
# filename="data.txt"
#wordcount=0
# with open(filename,"w") as file :
#     file.write("Automation is fun")
# with open(filename,"r") as file:
#     cont=file.read()
#     word=cont.split()
#     print(word)
#     print(len(word))
# #Q10 Write a Python program to print the numbers from 1 to 10 using a for loop
# x=1
# while x<=10 :
#     print(x)
#     x=x+1
#Q11 Write a Python program to display the multiplication table of a number entered by the user using a for loop
# x1=int(input("Enter the number :"))
# for i in range(1,11):
#     y1=x1*i
#     print(y1)