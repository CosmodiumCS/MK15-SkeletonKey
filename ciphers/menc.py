#!/usr/bin/python
# created by : Mart | marvhus

# imports
import getopt
import sys

#---------------------------------------------------------------------------------| Help Menu |
# Make sure to edit this for your specific cipher
help_menu = """
      +------------------------------------------------------+
      |  [+] ARGUMENTS MENC                                  |
      |  [+] ARG 1. Process                                  |
      |          [-e] ---------- Encrypt                     |
      |          [-d] ---------- Decrypt                     |
      +------------------------------------------------------+
      |  [+] ARG 2. Additional Aruments                      |
      |          [-t <plaintext>] --------- Input Text       |
      |          [-k <plaintext>] --------- Input Key        |
      +------------------------------------------------------+ 
      |  [+] Example:                                        |
      |          cryptex -menc -e -t "hello" -k "test"       |
      |          cryptex -menc -d -t "test" -k "0C00070805"  |
      +------------------------------------------------------+
        """

#-----------------------------------------------------------------------------------| Encoding |
def encode(_Input, alphabet, _Output):

    # Calculate the indexes of the characters in the input based of the alphabet variable
    inputArr = []
    for char in _Input:
        index = alphabet.index(char)
        if index == -1:
            print(f"Error: illegal character: '{char}'")
            return
        inputArr.append(index)

    # Calculate the indexes of the character in the output based of the alphabet variable
    outputArr = []
    for char in _Output:
        index = alphabet.index(char)
        if index == -1:
            print(f"Error: illegal character: '{char}'")
            return
        outputArr.append(index)

    # Calculate the encryption/decryption key
    key = ""
    for i, val in enumerate(inputArr):
        inputCharIndex = val
        outputCharIndex = outputArr[i % len(outputArr)]

        difference = None
        if inputCharIndex == outputCharIndex:
            difference = 0
        elif inputCharIndex < outputCharIndex:
            difference = outputCharIndex - inputCharIndex
        elif inputCharIndex > outputCharIndex:
            difference = len(alphabet) - (inputCharIndex - outputCharIndex)
        else:
            print("This shouldn't happen")
            return

        # Check if the difference is correct
        if outputCharIndex == (inputCharIndex + difference) % len(alphabet):
            hexValue = "%0.2X" % difference
            key += hexValue
        else:
            print("error, could not find the charIndex difference")

    print(f'\nEncrypted Content:\n{_Output}\nGenerated Key: \n{key}\n')

#-----------------------------------------------------------------------------------| Decoding |
def decode(plain_content, alphabet, key):

    # key
    n = 2
    key = [key[i:i+n] for i in range(0, len(key), n)]
    for i, val in enumerate(key):
        key[i] = int(val, 16)

    # Calculate the indexes of the characters in the encrypted text, based of the alphabet variable
    encryptedTextCharIndex = []
    for char in plain_content:
        index = alphabet.index(char)
        if index == -1:
            print(f"error, illegal character: \"{char}\"")
            return
        encryptedTextCharIndex.append(index)

    # Decrypt the text
    decrypted = ""
    for i in range(len(key)):
        charIndex = (encryptedTextCharIndex[i % len(encryptedTextCharIndex)] - key[i]) % len(alphabet)
        char = alphabet[charIndex]
        decrypted += char


    print(f'Decrypted Content:\n{decrypted}\n')

# -------------------------------------------------------------------------------| Arg Parsing |
# Add more args here if there are more than the default -t -i -o [ Example: -k ]
def parser():
    opts, _ = getopt.getopt(sys.argv[2:], 't:k:', ['inputText', 'inputKey'])
    arg_dict = {}

    # loop through arguments, assign them to dict [arg_dict]
    for opt, arg in opts:
        # input options
        if opt == '-t':
            arg_dict['-t'] = arg # input text
        if opt == '-k':
            arg_dict['-k'] = arg # input key

    return arg_dict


# ---------------------------------------------------------------------------------| CLI Args |
# command line interface
def cli(argument_check):

    # one liners
    if argument_check == True:

        # tries to get all arguments
        try:
            arguments = parser()

        # catches arguments with no value
        except getopt.GetoptError:
            print(f'[!!] No value was given to your argument\n{help_menu}')

        # continues with recieved arguments
        else:
            inputted_content = arguments.get('-t') # getting variables for ciphering process
            alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
            # TODO: add functionality to set custom alphabet
            key = arguments.get('-k')

            ciphering_process = sys.argv[1]

            # attempts to run cipher
            try:
                # encodes octal
                if ciphering_process == '-e':
                    encode(inputted_content, alphabet, key)

                # decodes octal
                elif ciphering_process == '-d':
                    decode(inputted_content, alphabet, key)

                # exeption
                else:
                    print(f'[!!] No Key or Argument was specified - Ciphering process\n{help_menu}')

            # catches unspecified arguments
            except TypeError:
                print(f'[!!] No Key or Argument was specified - TypeError\n{help_menu}\n')
                import traceback
                traceback.print_exc()

    else:
        print(help_menu)

# ---------------------------------------------------------------------------------| Main Code |
# [!!] Shouldnt have to edit this
def main_code():
    try:# checks for arguments
        sys.argv[1]
    except IndexError:
        arguments_exist = False
    else:
        arguments_exist = True

    cli(arguments_exist)

# runs main function if file is not being imported
if __name__ == '__main__':
    main_code()