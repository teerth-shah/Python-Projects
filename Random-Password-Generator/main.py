import random 
#random library 

print("==============RANDOM PASSWORD GENERATOR==============")
#loops in list
numbers = [str(i) for i in range(1, 11)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
#created new list to take input 
passwordlist = []
input_of_numbers = int(input("How many numbers do you want in your password? "))
input_of_symbols = int(input("How many symbols do you want in your password? "))    
input_of_letters = int(input("How many letters do you want in your password? "))
#loops to append all random numbers , symbols, letters in list
for char in range(1,input_of_numbers+1):
    passwordlist.append(random.choice(numbers))

for char in range(1,input_of_symbols+1):
    passwordlist.append(random.choice(symbols))

for char in range(1,input_of_letters+1):
    passwordlist.append(random.choice(letters))

random.shuffle(passwordlist)
print(passwordlist)
#another password variable so add every char in it  
password =" "
for char in passwordlist:
    password += char

print(f"Your password is "+str(password))
