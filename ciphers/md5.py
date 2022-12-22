#!/usr/bin/env python3

# created by : Mart | marvhus

import hashlib

# help menu for cipheringing process
help_menu = """
Usage:
  key md5 [FLAGS] [OPTIONS]

FLAGS:
  -e, --encrypt     encrypt input text or file
  -b, --brute       brute force hash

OPTIONS:
  -t, --text <plaintext>         input text
  -i, --inputFile <input file>   input file
  -o, --output <output file>     output file
  -w, --wordlist <input file>    wordlist file
                                    required if brute forcing with wordlist '-b'
  -r, --range <number>           maximum guess length
                                    required if brute forcing dynamically '-b'

Examples:
  key md5 -e -t hello
  key md5 -b -t 5d41402abc4b2a76b9719d911017c592 -w example.txt
  key md5 -b -t 5d41402abc4b2a76b9719d911017c592 -r 13
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
            rawresult = hashlib.md5( salt.encode('ascii') +
                                 text.encode('ascii')  ).digest()
            output += f'Salt | {salt}'
        else:
            rawresult = hashlib.md5( text.encode('ascii')  ).digest()

        result = rawresult.hex()

        output += f"\nMD5 Raw Sum | {rawresult}\nMD5 Sum | {result}"

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
            guess = hashlib.md5( word.encode('ascii') ).hexdigest()
            if guess.lower() == text.lower():
                output += f'\nDecoded MD5 | {word}'
                return [output, True]
            continue
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
            result = hashlib.md5( guess.encode('ascii') ).hexdigest()

            if result.lower() == text.lower():
                return [f'Decoded MD5 | {guess}', True]
        print()

        return [f'Did not decode md5 with max range of {range_}', False]


    # Pass False if Fail Message
    # Return Nothing to have no output

    if not text:
        return [f'"{text}" is not a valid input for -t', False]

    return ['Unknown error', False]

