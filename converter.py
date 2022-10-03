##a simple binary to decimal and decimal to binary converter

#welcome
print("WELCOME TO BINARY / DECIMAL CONVERTER!!!\n");

#function to convert decimal to binary
def bin2dec(num):
    numList = list(num);
    decimal = 0;
    for i in range(0,8):
        a = int(7 - i);
        b = int(numList[i]);
        decimal += 2**a * b;
    print("Your number in decimal is " + str(decimal));
    restart();

def dec2bin(num):
    binary = ["0","0","0","0","0","0","0","0"];
    n = int(num);
    while n > 0:
        if n > 127:
            n -= 128;
            binary[0] = '1';
        elif n > 63:
            n -= 64;
            binary[1] = '1';
        elif n > 31:
            n -= 32;
            binary[2] = '1';
        elif n > 15:
            n -= 16;
            binary[3] = '1';
        elif n > 7:
            n -= 8;
            binary[4] = '1';
        elif n > 3:
            n -= 4;
            binary[5] = '1';
        elif n > 1:
            n -= 2;
            binary[6] = '1';
        else:
            n -= 1;
            binary[7] = '1';
    print("Your number in binary is: " + ' '.join(binary));
    restart();

#input for system and number to convert
def askForType():

    conversionType = input("What is the number system? Type b for binary, d for decimal: ");

    # checks if the system's been chosen right
    while (conversionType.lower() == "b" or conversionType.lower() == "d") != True:
        conversionType = input("Please type a valid value (b for binary, d for decimal): ");

    number2Convert = input("Please type the number you want to convert: ");

    #check if the number is in rule
    if conversionType.lower() == "b":
        while ((len(number2Convert) != 8 or int(number2Convert) > 11111111)):
            number2Convert = input("Please type a valid value!!! (00000000 - 11111111): ");
    elif conversionType.lower() == "d":
        while (int(number2Convert) < 0 or int(number2Convert) > 255):
            number2Convert = input("Please type a valid value!!! (0-255): ");

    if conversionType.lower() == "b":
        bin2dec(number2Convert);
    elif conversionType.lower() == "d":
        dec2bin(number2Convert);

def restart():
    toContinue = input("Do you want to continue? (y/n) ");
    if toContinue.lower() == "y":
        askForType();
    elif toContinue.lower() == "n":
        print("Thanks for using the binary/decimal converter!");
        return;
    else:
        print("Please enter a valid value!!!");
        restart();

#start program
askForType();
