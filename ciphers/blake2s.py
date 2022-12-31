#!/usr/bin/env python4

# added by : H4Z3
# edit of Mart | marvhus MD5 module

import hashlib

# help menu for cipheringing process
help_menu = """
USAGE:
key blake2s [FLAGS] [OPTIONS]

FLAGS:
    -b, --brute      Brute Force
    -e, --encrypt    Encrypt input text or file

OPTIONS:
    -i, --inputFile <input file>    Input file to encrypt or decrypt
    -o, --output <output file>      Output file for encrypted or decrypted text
    -r, --range <number>            Max guess length
    -t, --text <text>               Input text to encrypt or decrypt
    -w, --wordlist <input file>     Wordlist

EXAMPLES:
    key blake2s -e -t "hello"
"""

# decode function [!] Each Cipher Must Have This <---------- [!]
def encode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    salt = args.salt

    if text:
        # Run Decode
        output = f'Encoding | {text}'

        # Detect Salt
        if salt:
            rawresult = hashlib.blake2s( salt.encode('ascii') +
                                 text.encode('ascii')  ).digest()
            output += f'Salt | {salt}'
        else:
            rawresult = hashlib.blake2s( text.encode('ascii')  ).digest()

        result = rawresult.hex()

        output += f"\nBlake2s Raw Sum | {rawresult}\nBlake2s Sum | {result}"

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return [f'"{text}" is not a valid input for -t', False]

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text

    if args.wordlist and args.range:
        return ["Please only pick one '-r' or '-w\'", False]

    if text and args.wordlist:
        wordlist = args.wordlist

        # Run Decode
        output = f'Bruteforcing | {text}'

        length = len(wordlist)

        print()
        for i, word in enumerate(wordlist):
            print(f'Checking {i + 1}/{length}', end='\r')
            guess = hashlib.blake2s( word.encode('ascii') ).hexdigest()
            if guess.lower() == text.lower():
                output += f'\nDecoded Blake2s | {word}'
                return [output, True]
            continuear
        print()

        output = "Not found in wordlist"
        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output, False]

    if text and args.range:
        import string
        import itertools

        alphabet = string.ascii_letters + string.punctuation + string.digits
        range_ = int(args.range)

        if range_ <= 0:
            return ["Can't use a range that is 0 or lower", False]

        i = 0
        print()
        for item in itertools.product(alphabet, repeat=range_):
            i += 1
            guess = "".join(item)
            print(f'Attempt {i} -- {guess}', end='\r')
            result = hashlib.blake2s( guess.encode('ascii') ).hexdigest()

            if result.lower() == text.lower():
                return [f'Decoded Blake2s | {guess}', True]
        print()

        return [f'Did not decode Blake2s with max range of {range_}', False]


    # Pass False if Fail Message
    # Return Nothing to have no output

    if not text:
        return [f'"{text}" is not a valid input for -t', False]

    return ['Unknown error', False]




