alpha = list(("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ").lower())


def encrypt():
    text = ""
    msg2 = input("enter the text to encrypt: ")
    shift = int(input("enter the shift number: "))
    shift = shift % 25
    for msg in msg2:
        if msg not in alpha:
            text = text+"*"
        else:
            position = alpha.index(msg)
            new_position = position+shift
            new_char = alpha[new_position]
            text += new_char
    print(text)
    start()


def decrypt():
    text = ""
    msg2 = input("enter the text to encrypt: ")
    shift = int(input("enter the shift number: "))
    shift = shift % 25
    for msg in msg2:
        position = alpha.index(msg)
        new_position = position-shift
        new_char = alpha[new_position]
        text += new_char
    print(text)
    start()


def cho():
    ask = input("press 1 for Encrpyt and 2 for Decrypt: ")
    if(ask == "1"):
        encrypt()
    elif(ask == "2"):
        decrypt()
    else:
        print("enter the correct choice")


def choo():
    choice = input("Enter yes to continue and no to exit:\n")
    if(choice == "yes"):
        cho()
    else:
        exit


def start():
    choice = input("Enter 1 to continue and 2 to exit:\n")
    if(choice == "1"):
        cho()
    else:
        exit


choo()
