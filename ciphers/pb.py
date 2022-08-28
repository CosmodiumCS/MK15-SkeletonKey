#!/usr/bin/python

# created by : Mart

# help menu for cipheringing process
help_menu = """
+--------------------------------------------------------------------------------------------------+
| [✓] ARGUMENTS Pin Buster                                                                         |
| [✓] ARG 1. Ciphering Process                                                                     |
|         [-b] .......... Brute Force                                                              |
| [✓] ARG 2. Additional Aruments                                                                   |
|         [-t <plaintext>] --------- Input Text                                                    |
|         [-i <input file>] -------- Input File [.txt]                                             |
|         [-o <output file>] ------- Output File                                                   |
|         [-r <number, number>] ---- Range                                                         |
|               [You can either enter one number as a range, or 2 numbers as a range of ranges]    |
+--------------------------------------------------------------------------------------------------+
| [✓] Example:                                                                                     |
|  cryptex pb -b -t "1234" -r 4                                                                    |
|  cryptex pb -b -t "1234" -r 3, 5                                                                 | 
+--------------------------------------------------------------------------------------------------+
"""

# brute function [!] Optional Per Cipher <----------------- [!]
def brute(args):
    text = args.text
    range_ = [i.strip() for i in args.range.split(",") if i.strip().isdigit()]
    increment = 1

    if not range_:
        return['Please enter a range \'-r\'', False]
    
    if len(range_) < 2:
        range_.append(range_[0] + 1)

    if range_[1] < range_[0]:
        increment = -1

    if text and length:
        output = f'Bruteforcing | {text}\n'

        import itertools
        aplhabet = [f"{i}" for i in range(10)]

        for length in range(range_[0], range_[1], increment):
            for item in itertools.product(alphabet, repeat=length):
                guess = "".join(item)
                if guess == text:
                    output += "Found pin | {guess}\n"
        
        output += f"Coundlit find pin\n"
        return [output,True]
    else:
        if not length:
            return ['Please enter a valid range \'-r\'', False]
        
        if not text:
            return ['Please enter a valid input/pin \'-t\'', False]

    return ['Unknown error', False]
