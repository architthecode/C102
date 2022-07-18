import os

def main():
    print("Hey Mate! I have designed two programs. Which one do you want to try?")
    print("1. Convert decimal number to BINARY, OCTAL and HEXADECIMAL")
    print("2. Count the vowels in word or sentence")
    choice = int(input("Enter your choice: "))

    if(choice == 1):
        print("Ok so going on with program number 1.")
        num = int(input("Enter the desired number which you want to convert: "))
        print("The decimal value of", num, "is:")
        print(bin(num), "in binary.")
        print(oct(num), "in octal.")
        print(hex(num), "in hexadecimal.")

    elif(choice == 2):
        vowels = 'aeiou'
        wordInput = input("Enter the sentence or word from which you want to know how many vowels are there.")
        wordInput = wordInput.casefold()
        count = {}.fromkeys(vowels,0)
        for char in wordInput:
           if char in count:
               count[char] += 1
        print(count)

    else:
        print("Enter a valid number")

main()