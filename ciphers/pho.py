#!/usr/bin/python

# New Template for the the codex project
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
USAGE:
  key pho [FLAGS] [OPTIONS]

FLAGS:
  -e, --encrypt     Encrypt the input text
  -d, --decrypt     Decrypt the input text

OPTIONS:
  -t, --text <plaintext>         Input Text
  -i, --inputFile <input file>   Input File [.txt]
  -o, --output <output file>     Output File

EXAMPLE:
  key pho -e -t hello
"""

# phonetic alphabet
phonetic ={
        "A" : "Alfa",
        "B" : "Brava",
        "C" : "Charlie",
        "D" : "Delta",
        "E" : "Echo",
        "F" : "Foxtrot",
        "G" : "Golf",
        "H" : "Hotel",
        "I" : "India",
        "J" : "Juliett",
        "K" : "Kilo",
        "L" : "lima",
        "M" : "Mike",
        "N" : "November",
        "O" : "Oscar",
        "P" : "Papa",
        "Q" : "Quebec",
        "R" : "Romeo",
        "S" : "Sierra",
        "T" : "Tango",
        "U" : "Uniform",
        "V" : "Victor",
        "W" : "Whiskey",
        "X" : "X-Ray",
        "Y" : "Yankee",
        "Z" : "Zulu",
        " " : "(space)"
        }
        
# phonetic alphabet inverse
phoneticInverse = dict((v,k) for (k,v) in phonetic.items())

# encode phonetic
def encode(input):
    text = input.text.upper()
    output = []

    for character in text:
        if character in phonetic:
            output.append(phonetic[character])
        else:
            output.append(character)
    return [" ".join(output), True]

# decode phonetic
def decode(input):
    text = input.text.split(" ")
    output = ''

    for character in text:
        if character in phoneticInverse:
            output += phoneticInverse[character]
        else:
            output += character
    return [output.capitalize(), True]
