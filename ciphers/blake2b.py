#!/usr/bin/env python3

# added by : H4Z3
# edit of Mart | marvhus MD5 module

import hashlib

# help menu for cipheringing process
help_menu = """
+-------------------------------------------------------------+
| [✓] ARGUMENTS Blake2b                                       |
| [✓] ARG 1. Ciphering Process                                |
|         [-e] .......... Encrypt                             |
|         [-b] .......... Brute Force                         |
| [✓] ARG 2. Additional Aruments                              |
|         [-t <plaintext>] --------- Input Text               |
|         [-i <input file>] -------- Input File [.txt]        |
|         [-o <output file>] ------- Output File              |
|         [-w <input file>] -------- Wordlist                 |
|             [Required if brute forcing with wordlist '-b']  |
|         [-r <number>] ------------ Max guess length         |
|             [Required if brute forcing dynamically '-b']    |
+-------------------------------------------------------------+-----------+
| [✓] Example:                                                            |
|  cryptex blake2b -e -t hello                                            |
|  cryptex blake2b -b -t 5d41402abc4b2a76b9719d911017c592 -w example.tx   |
|  ceyptex blake2b -b -t 5d41402abc4b2a76b9719d911017c592 -r 13           |
+-------------------------------------------------------------------------+
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
            result = hashlib.blake2b( salt.encode('ascii') +
                                 text.encode('ascii')  ).hexdigest()
            output += f'Salt | {salt}'
        else:
            result = hashlib.blake2b( text.encode('ascii')  ).hexdigest()

        output += f"\nBlake2b Sum | {result}"

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
            guess = hashlib.blake2b( word.encode('ascii') ).hexdigest()
            if guess.lower() == text.lower():
                output += f'\nDecoded Blake2b | {word}'
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
            result = hashlib.blake2b( guess.encode('ascii') ).hexdigest()

            if result.lower() == text.lower():
                return [f'Decoded Blake2b | {guess}', True]
        print()

        return [f'Did not decode Blake2b with max range of {range_}', False]


    # Pass False if Fail Message
    # Return Nothing to have no output

    if not text:
        return [f'"{text}" is not a valid input for -t', False]

    return ['Unknown error', False]
