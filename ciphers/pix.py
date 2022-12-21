#!/usr/bin/python

from PIL import Image
import math

# made by : Haze

# help menu for pixel encoding process
help_menu = """
┌────────────────────────────────────────────────────────────────────┐
│  [■] ARGUMENTS Pixel Encoding                                      │
│  [■] ARG 1. Process                                                │
│          [-e] ──────────────────── Encode                          │
│          [-d] ──────────────────── Decode                          │ 
├────────────────────────────────────────────────────────────────────┤
│  [■] ARG 2. Additional Aruments                                    │
│          [-t <input text>] ─────── Input Text                      │
│          [-f <file>] ───────────── Input File                      │
│          [-ii <input image>] ───── Input image                     │
│          [-o <output file>] ────── Output File                     │
│          [-c <channel> ] ───────── Channel                         │
├────────────────────────────────────────────────────────────────────┤
│  [■] ARG 3. Channel                                                │
│          [-c red] ──────────────── Encode image on red channel     │
│          [-c green] ────────────── Encode image on green channel   │
│          [-c blue] ─────────────── Encode image on blue channel    │
├────────────────────────────────────────────────────────────────────┤
│  [■] Example:                                                      │
│          key pix -e -t 'Hello World!' -c red -o encoded.png        │
│          key pix -e -f textfile.txt -c red -o encoded.png          │
│                                                                    │
│          key pix -d -ii encoded.png -c red                         │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
"""

def encode(args):
    text = args.text
    file = args.file
    output = args.output
    channel = args.channel

    # Read the input text or file
    if text:
        pass
    
    elif file:
        try:
            with open(file, "r") as f:
                text = f.read() 

        except FileNotFoundError:
            return ['Error: The file count not be found', False]

        except:
            return ['Error: An unknown error occurred while reading the file', False]

    else:
        return ['Error: No input text or file provided', False]

    # Calculate the size of the image
    size = int(math.ceil(math.sqrt(len(text))))

    # Create an empty image with the calculated size
    img = Image.new("RGB", (size, size))
    pixels = img.load()

    # Encode the text into the specified channel of the pixel values of the image
    if channel.lower() == "red":
        for i in range(len(text)):
            x = i % size
            y = i // size
            r, g, b = pixels[x, y]
            pixels[x, y] = (ord(text[i]), g, b)

    elif channel.lower() == "green":
        for i in range(len(text)):
            x = i % size
            y = i // size
            r, g, b = pixels[x, y]
            pixels[x, y] = (r, ord(text[i]), b)
            
    elif channel.lower() == "blue":
        for i in range(len(text)):
            x = i % size
            y = i // size
            r, g, b = pixels[x, y]
            pixels[x, y] = (r, g, ord(text[i]))

    else:
        return ['Error: Invalid channel specified', False]

    # Save the image
    try:
        img.save(output)

    except:
        return ['Error: An error occurred while saving the image', False]

    if len(text) <= 100:
        output = 'Encoding | {}\nChannel | {}\nOutput | {}'.format(
                text, channel, output)
        return [output, True]
    
    elif len(text) < 100:
        output = 'Encoding | Text is to large to show\nChannel | {}\nOutput | {}'.format(
                channel, output)
        return [output, True]

    else:
        return ['Error: Output status failed but program ran successfully', True]

def decode(args):
    inputImage = args.inputImage
    channel = args.channel

    # Open the input image
    img = Image.open(inputImage)
    pixels = img.load()

    # Decode the text from the specified channel of the pixel values of the image
    decoded_text = ""
    if channel.lower() == "red":
        for i in range(img.size[0] * img.size[1]):
            x = i % img.size[0]
            y = i // img.size[0]
            r, g, b = pixels[x, y]
            decoded_text += chr(r)

    elif channel.lower() == "green":
        for i in range(img.size[0] * img.size[1]):
            x = i % img.size[0]
            y = i // img.size[0]
            r, g, b = pixels[x, y]
            decoded_text += chr(g)

    elif channel.lower() == "blue":
        for i in range(img.size[0] * img.size[1]):
            x = i % img.size[0]
            y = i // img.size[0]
            r, g, b = pixels[x, y]
            decoded_text += chr(b)
    else:
        return ['Error: Invalid channel specified', False]

    output = "Decoding | {}\nChannel | {}\nDecoded | {}".format(
            inputImage, channel, decoded_text)

    return [output, True]
