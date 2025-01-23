#Global variable
x=10
print(x)
print("x is a :",type(x))
print("Memory location is :",id(x))

def myfunction():
    y=5 #Local variable

    print("Y is a local Variable :", y)

    print("Y is a local variable :", id(y))

    print("X is a Global Variable inside function:", type(x))
myfunction()

print("X is a global variable outside function :", id(x))