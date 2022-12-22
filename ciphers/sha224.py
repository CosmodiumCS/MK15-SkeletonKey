#!/usr/bin/env python3

# added by : H4Z3
# edit of Mart | marvhus MD5 module

import hashlib

# help menu for cipheringing process
help_menu = """
USAGE:
    key sha224 [FLAGS] [OPTIONS]

OPTIONS:
    -t, --text       Input Text
    -i, --inputFile  Input File
    -o, --output     Output File
    -w, --wordlist   Wordlist
                         Required if brute forcing with wordlist '-b'
    -r, --range      Max guess length
                         Required if brute forcing dynamically '-b'

EXAMPLES:
    key sha224 -e -t hello
    key sha224 -b -t ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193 -w example.txt
    key sha224 -b -t ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193 -r 13
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
            rawresult = hashlib.sha224( salt.encode('ascii') +
                                 text.encode('ascii')  ).digest()
            output += f'Salt | {salt}'
        else:
            rawresult = hashlib.sha224( text.encode('ascii')  ).digest()

        result = rawresult.hex()

        output += f"\nSHA224 Raw Sum | {rawresult}\nSHA224 Sum | {result}"

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
            guess = hashlib.sha224( word.encode('ascii') ).hexdigest()
            if guess.lower() == text.lower():
                output += f'\nDecoded SHA224 | {word}'
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
            result = hashlib.sha224( guess.encode('ascii') ).hexdigest()

            if result.lower() == text.lower():
                return [f'Decoded SHA224 | {guess}', True]
        print()

        return [f'Did not decode SHA224 with max range of {range_}', False]


    # Pass False if Fail Message
    # Return Nothing to have no output

    if not text:
        return [f'"{text}" is not a valid input for -t', False]

    return ['Unknown error', False]
