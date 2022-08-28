#!/usr/bin/python

# main file for the the codex project
# created by : C0SM0

# TODO: beautify
# TODO: clean up
# TODO: import new ciphers

# imports
import sys
import os
from colorama import Fore, Back, Style

# NOTE: '--' for long args

# help menu
help_menu = Fore.CYAN + """
_________            .___     ____  ___
\\_   ___ \\  ____   __| _/____ \\   \\/  /
/    \\  \\/ /  _ \\ / __ |/ __ \\ \\     / 
\\     \\___(  <_> ) /_/ \\  ___/ /     \\ 
 \\______  /\\____/\\____ |\\___  >___/\\  \\
        \\/            \\/    \\/      \\_/


        The Codex Project Syntax

        First argument: Ciphers
        -b = base64 encoding
        -c = caesar cipher
        -m = multiplicative cipher
        -r = reverse cipher
        -v = vigenere cipher

            Base64 Encoding Arguments:

            First Argument:
            -e = encode
            -d = decode

            Additional Arguments:
            -i <input file> = input file [.txt is best]
            -t <input text> = input text, one string only
            -o <output file> = output file [output will be printed to screen by default]
            
            Example:
            main.py -b -e -t hello

        Caesar Cipher:
            Second Argument: Ciphering Process
            -e = encrypt
            -d = decrypt
            -b = bruteforce [bruteforces using all possible keys by default]

            Additional Arguments:
            -k <integer key> = key [not required for bruteforcing '-b']
            -r <start,end>   = choose a range of keys to start and end the bruteforce
            -t <plaintext>   = input text, one string only
            -i <input file>  = input file [.txt is best]
            -o <output file> = output file [output will be printed to screen by default]

            Example:
            main.py -c -e -t hello -k 5

        Multiplicative-Cipher Arguments:

            Second Argument: Ciphering Process
            -e = encrypt
            -d = decrypt

            Additional Arguments:
            -k <integer key> = key 
            -t <plaintext>   = input text 
            -i <input file>  = input file [.txt]
            -o <output file> = output file [output will be printed to screen by default]

            Example:
            main.py -m -e -k 7 -t hello 

        Reverse-Cipher Arguments:
            Additional Arguments:
            -t <plaintext>   = input file [.txt]
            -i <input file>  = input text
            -o <output file> = output file [output will be printed to screen by default]

            Example:
            main.py -t hello 
            
        Vigenere Cipher:
            Second Argument: Ciphering Process
            -e = encrypt
            -d = decrypt [known key]
            -u = decrypt [unkown key]

            Additional Arguments:
            -k <string key> = key 
            -i <input file> = input file [.txt is best]
            -t <input text> = input text, one string only

            Example:
            main.py -v -e -t hello -k world
            main.py -v -u -i file.txt 
        """ + Fore.RESET

# command line interface
def cli(argument_check):

    # one liners
    if argument_check == True:

        # check ciphering option
        ciphering_option = sys.argv[1]
        remaining_arguments = sys.argv[2:]
        string_args = ' '.join(remaining_arguments)

        # attempts to run caesar
        try:
            # caesar cipher
            if ciphering_option == '-c':
                os.system(f'python3 ./ciphers/caesarCipher.py {string_args}')

            # vigenere cipher
            elif ciphering_option == '-v':
                os.system(f'python3 ./ciphers/vigenereCipher.py {string_args}')

            # reverse cipher
            elif ciphering_option == '-r':
                os.system(f'python3 ./ciphers/reverseCipher.py {string_args}')

            # multiplicative cipher
            elif ciphering_option == '-m':
                os.system(f'python3 ./ciphers/multiplicativeCipher.py {string_args}')

            # base64 cipher
            elif ciphering_option == '-b':
                os.system(f'python3 ./ciphers/base64Cipher.py {string_args}')

            # exception
            else:
                print('no ciphering option was added')

        # catches unspecified arguments
        except TypeError:
            print(f'[!!] No Key or Argument was specified\n{help_menu}')

    # help menu
    else:
        print(help_menu)

# main code
def codex_main():

    # checks for arguments
    try:
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

# run main code
if __name__ == '__main__':
    codex_main()