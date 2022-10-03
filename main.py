import string

def encrypt():
    passPlain = input("Please type your password you want to encrypt: ");
    cipherStep = input("Please enter your cipher step: ");

    while cipherStep.isnumeric() == False:
        cipherStep = input("Please enter a numeric value for cipher step: ");

    passList = list(passPlain);

    passCrypted = "";
    for i in range(len(passList)):
        iIndex = int(string.printable.index(passList[i])) + int(cipherStep);
        iIndex %= 100;
        passCrypted += string.printable[iIndex];

    print("Your encrypted password is {}".format(passCrypted));

def decrypt():
    passPlain = input("Please type your password you want to decrypt: ");
    cipherStep = input("Please enter your cipher step: ");

    while cipherStep.isnumeric() == False:
        cipherStep = input("Please enter a numeric value for cipher step: ");

    passList = list(passPlain);

    passDecrypted = "";
    for i in range(len(passList)):
        iIndex = int(string.printable.index(passList[i])) - int(cipherStep);
        iIndex %= 100;
        passDecrypted += string.printable[iIndex];

    print("Your decrypted password is {}".format(passDecrypted));

whatAction = input("What do you want to do? (type 'e' for encryption, 'd' for decryption: ").lower();
while (whatAction == "e" or whatAction == "d") == False:
    whatAction = input("Please enter a valid value!!! (type 'e' for encryption, 'd' for decryption: ").lower();

if whatAction == 'e':
    encrypt();
else:
    decrypt();
