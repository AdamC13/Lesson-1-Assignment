#1
weather  = 'sunny'

if weather == "sunny":
    print("Wear sunglasses!")
else:
    print("Take an umbrella!")

feeling = input('How do you feel today? ')
if feeling == 'happy':
    print("That's great to hear")
elif feeling == 'sad':
    print("I hope your day gets better")

#2
PI_VALUE = 3.14
user_Age = 25
user_Location = "New York"
MAXLIMIT =  1000

#3
variable_a = "Hello, World!"
variable_b = 23
variable_c = 3.14
variable_d = True
print(type(variable_a))
print(type(variable_b))
print(type(variable_c))
print(type(variable_d))

#4
bread_Price = 4.99
jelly_Price = 6.99
peanut_Butter_Price = 65.99
total_Price = bread_Price + jelly_Price + peanut_Butter_Price

bank_Balance = 10000
interest_Rate = .07
new_Balance = bank_Balance * interest_Rate

#5
num1 = 57
num2 = 36
num3 = num1
num1 = num2
num2 = num3
print(num1 == num2)