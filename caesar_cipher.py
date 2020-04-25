print('What do you want to encrypt?')
msg = input()
key = int(input('What key do you want to use(enter a number)  '))

msg_orig = list(msg)
print(msg_orig)

cypher = [ord(letter)+key for letter in msg_orig]


print(cypher)
print(ord('t'))

msg_encrypt = [chr(x) for x in cypher]
print(msg_encrypt)