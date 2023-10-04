#1
# n1 = n//1000
# n2 = (n//100)%10
# n3 = (n%100)//10
# n4 = n%10
# r1 = n1+n4
# r2 = abs(n2-n3)
# if r1==r2:
#     print("YES!")
# else:
#     print("NO!")

#2
# age=int(input("Please enter your age!:"))
# if age>=18:
#     print("Access allowed")
# else:
#     print("Access denied")

#3
# a=int(input())
# b=int(input())
# c=int(input())
# if a+1==b and a+2==c:
#     print("YES!")
# else:
#     print("NO!")

#4
# c1=int(input())
# r1=int(input())
# c2=int(input())
# r2=int(input())
# if 1<=c1<=8 and 1<=r1<=8 and 1<=c2<=8 and 1<=r2<=8:
#     if c1==c2 or r1==r2:
#         print("YES!")
#     else:
#         print("NO!")
# else:
#  print("Error!Your number must be between 1 and 8!")

#5
# c1=int(input())
# r1=int(input())
# c2=int(input())
# r2=int(input())
# if 1<=c1<=8 and 1<=r1<=8 and 1<=c2<=8 and 1<=r2<=8:
#     if abs(c1-c2)<=1 and abs(r1-r2)<=1:
#         print("YES!")
#     else:
#         print("NO!")
# else:
#  print("Error!Your number must be between 1 and 8!")

#6
# a=int(input())
# b=int(input())
# c=int(input())
# if a>=b and a<=c:
#     print(a)
# elif b>=a and b<=c:
#     print(b)
# else:
#     print(c)

#7
# month = int(input("Enter the month number (1-12): "))
# if 1 <= month <= 12:
#     if month == 2:
#         print("This month has 28 days.")
#     elif month in [4, 6, 9, 11]:
#         print("This month has 30 days.")
#     else:
#         print("This month has 31 days.")
# else:
#     print("Error! Please enter a month number between 1 and 12.")

#8
# w = int(input("Enter the weight of the boxer!: "))
# if 15 <= w <= 60:
#     print("Light weight")
# elif 60 < w <= 64:
#     print("First welterweight")
# else:
#     print("Welterweight")

#9
# a1 = str(input("Enter the password!: "))
# a2 = str(input("Repeat the password!: "))
# if a1 == a2:
#     print("Password accepted!")
# else:
#     print("Password not accepted!")

#10
# n = int(input("Enter any number!: "))
# if n%2==0:
#     print("Even value")
# else :
#     print("Odd number")

#11
# a = float(input())
# b = float(input())
# if a < b:
#     print(a)
# else:
#     print(b)

#12
# age = int(input("Please enter your age: "))
# if age <= 13:
#     print("childhood")
# elif 14 <= age <= 24:
#     print("youth")
# elif 25 <= age <= 59:
#     print("maturity")
# else:
#     print("old")

#13
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b > c and b+c > a and a+c > b:
#     if a == b and b == c:
#         print("Equilateral")
#     elif a == b or b == c or a == c:
#         print("Isosceles")
#     else:
#         print("Versatile")
# else:
#     print("Triangle is not defined!")
