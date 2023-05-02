#!/usr/bin/env python3

# added by : H4Z3
# edit of Mart | marvhus MD5 module

import hashlib

# help menu for cipheringing process
help_menu = """
USAGE:
  key sha256 [FLAGS] [OPTIONS]

FLAGS:
  -b, --brute   Brute force the sha256 hash
  -e, --encode  Encrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt
  -o, --output <output file>     Output file for encrypted text
  -r, --range <range>            Max guess length for brute forcing (required for dynamic brute forcing)
  -t, --text <text>              Input text to encrypt or decrypt
  -w, --wordlist <wordlist>      Wordlist for brute forcing (required for brute forcing with wordlist)

EXAMPLES:
  key sha256 -e -t hello
  key sha256 -b -t 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 -w example.txt
  key sha256 -b -t 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 -r 13
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
        rawresult = hashlib.sha256( salt.encode('ascii') +
                             text.encode('ascii')  ).digest()
        output += f'Salt | {salt}'
    else:
        rawresult = hashlib.sha256( text.encode('ascii')  ).digest()

    result = rawresult.hex()

    output += f"\nSHA256 Raw Sum | {rawresult}\nSHA256 Sum | {result}"

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
        return SHA256_decode(args, text)
    if text and args.range:
        return bruteforce(args, text)
    # Pass False if Fail Message
    # Return Nothing to have no output

    return (
        ['Unknown error', False]
        if text
        else [f'"{text}" is not a valid input for -t', False]
    )


# TODO Rename this here and in `brute`
def bruteforce(args, text):
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
        result = hashlib.sha256( guess.encode('ascii') ).hexdigest()

        if result.lower() == text.lower():
            return [f'Decoded SHA256 | {guess}', True]
    print()

    return [f'Did not decode SHA256 with max range of {range_}', False]


# TODO Rename this here and in `brute`
def SHA256_decode(args, text):
    wordlist = args.wordlist

    # Run Decode
    output = f'Bruteforcing | {text}'

    length = len(wordlist)

    print()
    for i, word in enumerate(wordlist):
        print(f'Checking {i + 1}/{length}', end='\r')
        guess = hashlib.sha256( word.encode('ascii') ).hexdigest()
        if guess.lower() == text.lower():
            output += f'\nDecoded SHA256 | {word}'
            return [output, True]
    print()

    output = "Not found in wordlist"
    # Output content as string for main.py to print
    # Pass True if Success Message
    return [output, False]
