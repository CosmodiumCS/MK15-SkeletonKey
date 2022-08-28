#!/usr/bin/python

# created by : marvhus

# help menu for cipheringing process
help_menu = """
+------------------------------------------------------+
| [✓] ARGUMENTS Cleartext                              |
| [✓] ARG 2. Additional Aruments                       |
|         [-t <plaintext>] --------- Input Text        |
|         [-i <input file>] -------- Input File [.txt] |
+------------------------------------------------------+
| [✓] Example:                                         |
|  cryptex cleartext -e -t hello                        |
|  cryptex cleartext -d -t hello                        |
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
        output = f'Encoding | {text}\nEncoded  | {text}'

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
        output = f'Decoding | {text}\nDecoded  | {text}'

        # Output content as string for main.py to print
        # Pass True if Success Message
        return [output,True]
    else:
        # Pass False if Fail Message
        # Return Nothing to have no output
        return ['Custom Fail Message', False]

