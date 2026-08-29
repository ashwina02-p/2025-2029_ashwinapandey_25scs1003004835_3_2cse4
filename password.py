import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['!','#','$','%','^','&','*','(', ')', '+']

print("welcome to the pypassword generator")

nr_letter = int(input("enter the number of letters: "))
nr_symbol = int(input("enter the number of symbols: "))
nr_number = int(input("enter the number of numbers: "))

password_list = []

for char in range(0,nr_letter):
    password_list.append(random.choice(letters))
for char in range(0,nr_symbol):
    password_list.append(random.choice(symbols))
for char in range(0,nr_number):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char
print(f"your password is: {password} ")