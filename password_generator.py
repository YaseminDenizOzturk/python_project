import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the password generator!")

yd_letters = int(input("How many letters would you like in your password? \n"))
yd_numbers = int(input("How many numbers would you like?  \n"))
yd_symbols = int(input("How many symbols would you like? \n"))

password = ""
for char in range(1 , yd_letters + 1):
# kullanıcı 5 karakterli isterse range son sayıyı dahil etmediği için bir fazlasını aldım.
    #random_chr = random.choice(letters)
    #password += random_chr
    password += random.choice(letters)
    # bir değişkene atayıp değişkeni password a eklemek yerine bu işlemi doğrudan yaptım.
    

for char in range(1 , yd_numbers + 1):
    password += random.choice(numbers)

for char in range(1 , yd_symbols + 1):
    password += random.choice(symbols)

print(password)
