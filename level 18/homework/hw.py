#if ბლოკი ამოწმებს პირველ პირობას
#თუ if პირობა მცდარია მაშინ elif ვხმარობთ
#თუ არცერთი არ შესრულდა, მაშინ else ბლოკი

num = int(input('enter your number'))
num1 = int(input('Enter your number'))

if num > num1:
    print(num)
else:
    print(num1)


if num % 2 == 0:
    print("even")
else: 
    print("odd")


num = float(input("enter a number: "))
if num > 0:
   print("positive")
elif num < 0:
    print("negative")
else: 
    print("zero")


num= int(input("enter a number: "))
if num % 5 == 0:
    print("divisible by 5")
else:
    print("not divisible by 5")


for i in range(5):
    if num % 2 == 0:
       print("evan")
else:
    print("odd")

password = input("enter your password")
while password != "goa best":
    password = input("try again")
print("passsword is correct")

