#!/usr/bin/python

# created by : Fyzz
# New Template

# help menu for cipheringing process
help_menu = """
USAGE:
  key template [FLAGS] [OPTIONS]

FLAGS:
  -e, --encrypt   Encrypt input text or file
  -d, --decrypt   Decrypt input text or file

OPTIONS:
  -i, --inputFile <input file>   Input file to encrypt or decrypt
  -o, --output <output file>     Output file for encrypted or decrypted text
  -t, --text <text>              Input text to encrypt or decrypt

EXAMPLES:
  key template -e -t "hello"
"""

# decode function [!] Each Cipher Must Have This <---------- [!]
def encode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    if text:
        # Run Decode
        output = f'Encoding | {text}'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['Custom Fail Message', False]

# decode function [!] Each Cipher Must Have This <---------- [!]
def decode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    if text:
        # Run Decode
        output = f'Decoding | {text}'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['Custom Fail Message', False]

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = args.text
    
    if text:
        # Run Decode
        output = f'Bruteforcing | {text}'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['Custom Fail Message', False]
