#!/usr/bin/python
from PIL import Image

# Custom Image pixel enc
# created by : Fyzz

# help menu for cipheringing process
help_menu = """
+----------------------------------------------------------------+
|  [+] ARGUMENTS Pixel Enc                                       |
|  [+] ARG 1. Process                                            |
|          [-e] ---------- Encrypt                               |
|          [-d] ---------- Decrypt                               |
+----------------------------------------------------------------+
|  [+] ARG 2. Additional Aruments                                |
|          [-t <input text>] ------- Input Text                  |
|          [-i <copy file>] -------- Copy File                   |
|          [-ii <input image>] ----- Input image [.png]          |
|          [-o <output file>] ----+- Output File                 |
|                                 +---> [enc: .png, dec: any]    |
+----------------------------------------------------------------+ 
|  [+] Example:                                                  |
|          key pix -e -i copy.py -ii test.png -o encoded.png     |
|          key pix -d -ii decode.png                             |
+----------------------------------------------------------------+
"""

# encode pix
def encode(input):
    # Error Handling
    if (not input.inputFile or ".png" not in input.output):
        return ["Invalid Input file or PNG", False]

    # File Input / String Input
    input_content = ""
    if(input.inputFile):
         input_content = open(input.inputFile, 'r').read()
    if(input.text):
         input_content = input.text

    # Add Ending Flag
    file_with_ending = input_content + 'ÿ'
    input_image = Image.open(input.inputImage)
    pixel_map = input_image.load()
    height = input_image.size[1]

    # Map through text
    for i in range(0, len(file_with_ending)):
        # Get current image rbg and set new with encryption
        g, b = input_image.getpixel((i, height - 1))[1::]
        pixel_map[i, height -
                  1] = (int(ord(file_with_ending[i])), g, b)

    # Outputs
    input_image.save(f'{input.output}', format="png")
    return [f"Encoded: '{input.output}' Created", True, False]

# decode pix
def decode(input):
    # Error Handling
    if (".png" not in input.inputImage):
        return ["Invalid Input PNG", False]

    input_image = Image.open(input.inputImage)
    width, height = input_image.size

    # Starter Value
    output_text = ""

    # Map and decode
    for i in range(0, width - 1):
        r = input_image.getpixel((i, height - 1))[0]
        if r == 255:
            break
        output_text += chr(r)

    return [output_text, True]
