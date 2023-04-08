#Password Generator Project


#EASY PASSWORD GENERATOR

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password= ""
for i in range(1,nr_letters+1):
  random_letters  = random.choice(letters)
  password += random_letters
for j in range(1,nr_numbers+1):
  random_numbers = random.choice(numbers)
  password += random_numbers
for k in range(1,nr_symbols+1):
  random_symbol = random.choice(symbols)
  password += random_symbol
print(password)




# Hard Password GENERATOR

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Making a list so that password can be randomized as strings cant be

# password_list = []

# for i in range(1,nr_letters+1):
#   password_list.append(random.choice(letters))
# for j in range(1,nr_numbers+1):
#   password_list.append(random.choice(numbers))
# for k in range(1,nr_symbols+1):
#   password_list.append(random.choice(symbols))

# #Shuffling or randomizing the password

# random.shuffle(password_list)
# print(password_list)


# #Converting list into string


# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")
