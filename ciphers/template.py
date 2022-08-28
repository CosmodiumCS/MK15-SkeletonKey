#!/usr/bin/python

# created by : Fyzz
# New Template

# help menu for cipheringing process
help_menu = """
+------------------------------------------------------+
| [✓] ARGUMENTS Template                               |
| [✓] ARG 2. Additional Aruments                       |
|         [-t <plaintext>] --------- Input Text        |
|         [-i <input file>] -------- Input File [.txt] |
|         [-o <output file>] ------- Output File       |
+------------------------------------------------------+
| [✓] Example:                                         |
|  cryptex template -e -t hello                        |
+------------------------------------------------------+
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
