fh=open("output3.txt",'w')
import random
length =int(input('Enter the length of the password : '))
password = ''
password_list='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_":'
i=1
while i<=length:
      password = password + random.choice(password_list)
      i =i+1
fh.write(password)