#!/usr/bin/env python3

# added by : H4Z3
# edit of Mart | marvhus MD5 module

import hashlib

# help menu for cipheringing process
help_menu = """
USAGE:
  key sha512 [FLAGS] [OPTIONS]

FLAGS:
  -b, --brute       Brute force
  -e, --encrypt     Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -r, --range <number>           Max guess length (required if brute forcing dynamically)
  -t, --text <text>              Input text to encrypt or decrypt
  -w, --wordlist <input file>    Wordlist (required if brute forcing with wordlist)

EXAMPLES:
  key sha512 -e -t hello
  key sha512 -b -t 59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f -w example.txt
  key sha512 -b -t 59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f -r 13
"""

# decode function [!] Each Cipher Must Have This <---------- [!]
def encode(args):
    if not (text := args.text):
        # Pass False if Fail Message
        # Return Nothing to have no output
        return [f'"{text}" is not a valid input for -t', False]
    # Run Decode
    output = f'Encoding | {text}'

    if salt := args.salt:
        rawresult = hashlib.sha512( salt.encode('ascii') +
                             text.encode('ascii')  ).digest()
        output += f'Salt | {salt}'
    else:
        rawresult = hashlib.sha512( text.encode('ascii')  ).digest()

    result = rawresult.hex()

    output += f"\nSHA512 Raw Sum | {rawresult}\nSHA512 Sum | {result}"

    # Output content as string for main.py to print
    # Pass True if Success Message
    return [output,True]

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text

    if args.wordlist and args.range:
        return ["Please only pick one '-r' or '-w\'", False]

    if text and args.wordlist:
        return bruteforcing(args, text)
    if text and args.range:
        return decoding_SHA512(args, text)
    # Pass False if Fail Message
    # Return Nothing to have no output

    return (
        ['Unknown error', False]
        if text
        else [f'"{text}" is not a valid input for -t', False]
    )

def decoding_SHA512(args, text):
    import string
    import itertools

    alphabet = string.ascii_letters + string.punctuation + string.digits
    range_ = int(args.range)

    if range_ <= 0:
        return ["Can't use a range that is 0 or lower", False]

    print()
    for i, item in enumerate(itertools.product(alphabet, repeat=range_), start=1):
        guess = "".join(item)
        print(f'Attempt {i} -- {guess}', end='\r')
        result = hashlib.sha512( guess.encode('ascii') ).hexdigest()

        if result.lower() == text.lower():
            return [f'Decoded SHA512 | {guess}', True]
    print()

    return [f'Did not decode SHA512 with max range of {range_}', False]


def bruteforcing(args, text):
    wordlist = args.wordlist

    # Run Decode
    output = f'Bruteforcing | {text}'

    length = len(wordlist)

    print()
    for i, word in enumerate(wordlist):
        print(f'Checking {i + 1}/{length}', end='\r')
        guess = hashlib.sha512( word.encode('ascii') ).hexdigest()
        if guess.lower() == text.lower():
            output += f'\nDecoded SHA512 | {word}'
            return [output, True]
    print()

    output = "Not found in wordlist"
    # Output content as string for main.py to print
    # Pass True if Success Message
    return [output, False]
