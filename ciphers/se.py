#!/usr/bin/python

from PIL import Image
import numpy as np

# created by : marvhus

# help menu for cipheringing process
help_menu = """
+------------------------------------------------------+
| [✓] ARGUMENTS Static Encryption                      |
| [✓] ARG 2. Additional Aruments                       |
|         [-iw <number>] ----------- Image Width       |
|         [-m ] -------------------- Use monocromatic  |
+------------------------------------------------------+
| [✓] Example:                                         |
|  cryptex se -e                                       |
|  cryptex se -e -iw 3                                 |
|  cryptex se -d                                       |
|  cryptex se -d -iw 3                                 |
+------------------------------------------------------+
"""

# Generate the image
def gen_image(output, pixels):
    # Convert the pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # Use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image.save(output)

# Read the image data
def read_image(input_file):
    pixels = []
    img = Image.open(input_file)
    pix = img.load()
    width, height = img.size
    for i in range(height): # Vertical
        row = []
        for j in range(width): # Horizontal
            row.append(pix[j, i])
        pixels.append(row)
    return pixels

# decode function [!] Each Cipher Must Have This <---------- [!]
def encode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    text = input("Please enter the string you want to encode \n(example: Hello)\n > ")
    image_path = input("Please enter what you want the output file to be \n(example: file.png)\n > ")
    image_width = 1

    if not image_path:
        return ['You must suply file path for cryptext to make an image (-f)', False]

    if not text:
        return ['You must suply an input text for this to work', False]

    if args.image_width:
        image_width = int(args.image_width)

    output = f"Encoding | {text}"

    pixels = []
    for i in range(0, len(text), image_width * 3):
        row = text[i:i+(3*image_width)]
        rowArr = []
        # Loop over the input text in groups of 3
        for i in range(0, len(row), 3):
            # The group of 3 chars
            chars = row[i:i+3]
            # If there are not enough chars to make only groups of 3, then ths will say how many extra we will need (2, or 3)
            extra = 3 - len(chars)
            # Empty pixel array
            pixel = []

            # Get the ASCII values of the chars and add them to the pixel array
            for _, char in enumerate(chars):
                pixel.append(ord(char))

            # Add the extra value
            for i in range(extra):
                pixel.append(0)

            # Convert the pixel array to an array with a tupel inside
            pixel = (pixel[0], pixel[1], pixel[2])
            rowArr.append(pixel)

        extra = image_width - len(rowArr)
        for i in range(extra):
            rowArr.append((0,0,0)) # add black pixel if there are to few
        pixels.append(rowArr)

    gen_image(image_path, pixels)

    output += f"\nImage saved at | {image_path}"

    return [output, True]

# decode function [!] Each Cipher Must Have This <---------- [!]
def decode(args):
    # Getting text from all passed in args
    # All other args can be grabbed the same way
    # Example key = input.key | range = input.range
    image_path = input("Please enter the path to the file you want to decode \n(example: test.png)\n > ")

    if not image_path:
        return ['You must suply an image path for this to work (-f)', False]

    output = f'Decoding image | {image_path}'

    # Get the pixel data
    pixels = read_image(image_path)

    # Make empty string for the decoded text to be in
    decrypted = ""
    for _, height in enumerate(pixels): # Vertical
        for _, width in enumerate(height): # Horizontal
            for _, val in enumerate(width): # Pixel
                # Convert the ASCII value to char and add it to the decrypted variable
                decrypted += chr(val)

    output += f'\nText | {decrypted}'

    return [output,True]

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
