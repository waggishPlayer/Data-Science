import random, string

allowed_chars = list(' ' + string.ascii_letters + string.digits + string.punctuation)

def mes_receiver(ms, opn):
    random.seed(int(input("Enter key: ")))
    shuffled_chars = allowed_chars.copy()
    random.shuffle(shuffled_chars)

    if opn == 1:
        print("".join(shuffled_chars[allowed_chars.index(ele)] for ele in ms))
    else:
        print("".join(allowed_chars[shuffled_chars.index(ele)] for ele in ms))

ms = input("Enter the message: ")
opn = int(input("Enter (1) to encrypt and (2) to decrypt the message: "))

if opn == 1 or opn == 2:
    mes_receiver(ms, opn)
else:
    print("Invalid command")
