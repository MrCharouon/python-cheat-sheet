import random
import string

print('hello, Welcome to Password generator!')
length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)
password = "".join(temp)

if (len(password) < 8):
    print('password is weak\n')
elif (len(password) >= 8) and (len(password) <= 12):
    print('password is acceptable\n')
else:
    print('password is strong\n')
print(password)
