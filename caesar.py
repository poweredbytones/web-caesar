def alphabet_position_string(input):
    input = input.lower()
    output = []
    for character in input:
        number = ord(character) - 97
        output.append(number)
    print(output)

def alphabet_position(input):
    number = ord(input) - 97
    return number


def rotate_character(char,rot):
    if(char.isalpha()):
        number = alphabet_position(char.lower())
        number += rot
        number = number % 26
        char2 = chr(number+97)
        if char.isupper():
            char2 = char2.upper()
        return char2
    else:
        return char

def encrypt(text,rot):
    output = ''
    for letter in text:
        temp = rotate_character(letter,rot)
        output = output + temp
    return output

def main():

    from sys import argv, exit
    
    if (len(argv) > 1  and (argv[1].isdigit() == False)):
        print("\n- Attention the first argument must be an integer \n")

    if (len(argv) < 2):
        print("Remember that you can input a integer as a the first commandline argument")
        print("This integer will be used as the rotation.  ex. $python ceasar.py 5 \n")
    else:
        if (len(argv) < 3):
            print("Remember that you can input a string as a the second commandline argument")
            print("This strin will be used as the message.  ex. $python ceasar.py 5 'Hello World!' ")



    if (len(argv) > 2):
        I = argv[2]
    else:
        I = input("Type a message:")


    if (len(argv) > 1  and argv[1].isdigit()):
        R = int(argv[1])
    else:
        userInput = input("Rotate by:")
        if userInput.isdigit():
            R = int(userInput)
        else:
            print("rotation must be a integer")
            exit()
    print(encrypt(I,R))

if __name__ == "__main__":
    main()