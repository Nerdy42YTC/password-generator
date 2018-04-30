import string, random

chars = string.ascii_letters + string.digits + string.punctuation
length = 8

def define_length(length):
    length = int(input("Enter the length of the password (min. 8 chars.) :   "))

    while length < 8:
        print("\nERROR!")
        print("For your security, the password must be at least of 8 chars.")
        length = int(input("Enter the length of the password (min. 8 chars.) :   "))
    #end while
    return length
    #end function

def generate(length):
    passwd =  ''
    for i in range(length):
        passwd += random.choice(chars)
        #end for
    print(passwd)
    #end function

length = define_length(length)
generate(length)