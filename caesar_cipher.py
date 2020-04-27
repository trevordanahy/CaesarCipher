#to clear console and make it look good
import os
clear = lambda: os.system('clear') #on Linux System

#take input message and shift key from user and store it
#take input message and shift key from user and store it

print('What do you want to encrypt?')
msg = input()
shiftkey = int(input('What shiftkey do you want to use(enter a number)  '))


#convert string to list and iterate over list to convert letters to unicode

msg_orig = list(msg)

unicode_list = [ord(letter) for letter in msg_orig]

encrypt = []

#if the characters are a-z then shift them based on the key provided, the bounds below are a-z in upper and lower case. The second
for letter in unicode_list:
  shifted = letter + shiftkey
  if ((letter >=97) & (letter <=122)) or ((letter >=65) & (letter <= 90)):
    #second if cycles value back to a if the shift pushes past z. 
    if shifted > 122:
      letter = 96 + (shifted - 122)
      encrypt.append(chr(letter))
    elif shifted > 90 and shifted < 97:
      letter = 64 + (shifted - 90)
      encrypt.append(chr(letter))
    else:
      letter += shiftkey
      encrypt.append(chr(letter))
  else:
    encrypt.append(chr(letter))
#convert encrypted list to string
clear()
print ("".join(encrypt))