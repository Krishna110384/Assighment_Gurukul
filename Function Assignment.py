# from enum import unique
#
#
# def maximum(a,b,c,d):
#     return maximum
# if __name__ == "__main__":
#     numbers=(20,30,40,50)
#     print(max(numbers))
#
# def multiply(a,b,c,d,e):
#     return a*b*c*d*e
# if __name__ == "__main__":
#     seq=multiply(8,2,3,-1,7)
#     print(seq)
#
# def reverse_string(s):
#     return s[::-1]
# if __name__ == "__main__":
#     original_string=("1234abcd")
#     reversed_string=reverse_string(original_string)
#     print(reversed_string)
#
# def factorial(x):
#     if x<0:
#         return "No factorial defined for -ve values"
#     elif x==0 & x==1:
#         return 1
#     else:
#         result =1
#         for i in range(2, x+1):
#            result *= +i
#         return result
# if __name__ == "__main__":
#     delta=factorial(5)
#     print(delta)
#
#
# def unique(input_list):
#     return list(set(input_list))
# if __name__ == "__main__":
#     original_list=[1,22,2,2,3,3,5,8,5,7,10]
#     distinct_values=unique(original_list)
#     print(distinct_values)

# def prime_check(x,y):
#
#     return x%y
# if __name__ == "__main__":
#     x=int(input("Enter the no:"))
#     y=int(input("Enter the no:"))
#     if x%y==0 and x%1==0:
#         print("No is prime:",x)
#     else:
#         print("No is not a prime number :",x)


# def even_one(input_list):
#     for num in input_list:
#         if num%2 ==0:
#             print(num)
#     return list(set(input_list))
# if __name__ == "__main__":
#             input_list = [2, 3, 5, 8, 6, 9, 21, 16, 18]
#             print("Even no in the list are :")
#             even_one(input_list)
# def letter(x):
#     count=0
#     for char in x:
#         if char.isupper():
#             count +=1
#     return count
# if __name__ == "__main__":
#     x="This is India, Democracy is maintained"
#     uppercase_count=letter(x)
#     print("Number of uppercase letters:",uppercase_count)
# def alphabets(z):
#     count=0
#     for char in z:
#         if char.islower():
#             count +=1
#     return count
# if __name__ == "__main__":
#     z = "This is India, Democracy is maintained"
#     lowercase_count = alphabets(z)
#     print("Number of lowercase letters:", lowercase_count)
# def sum_of_list(input_list):
#     return sum(input_list)
# if __name__ == "__main__":
#     input_list=(8,2,3,0,7)
#     sum_list=sum_of_list(input_list)
#     print(sum_list)
def is_palindrome(string):
    cleaned_string=string.replace("","")
    return cleaned_string==cleaned_string[::-1]
if __name__ == "__main__":
    word="star"
    if is_palindrome(word):
        print(f'"{word}" is a palindrome')
    else:
        print(f'"{word}" is not a palindrome')







