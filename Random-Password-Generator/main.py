import random 


print("==============RANDOM PASSWORD GENERATOR==============")

numbers = [str(i) for i in range(1, 11)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
letters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

passwordlist = []
input_of_numbers = int(input("How many numbers do you want in your password? "))
input_of_symbols = int(input("How many symbols do you want in your password? "))    
input_of_letters = int(input("How many letters do you want in your password? "))

for char in range(1,input_of_numbers+1):
    passwordlist.append(random.choice(numbers))

for char in range(1,input_of_symbols+1):
    passwordlist.append(random.choice(symbols))

for char in range(1,input_of_letters+1):
    passwordlist.append(random.choice(letters))

random.shuffle(passwordlist)
print(passwordlist)
password =" "
for char in passwordlist:
    password += char

print(f"Your password is "+str(password))