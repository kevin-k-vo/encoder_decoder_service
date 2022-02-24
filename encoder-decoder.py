import binascii
from itertools import cycle
import base64
import os
import time

def encode(input, key):
    zipped = zip(input, cycle(key))

    output = ""

    for z in zipped:
        output += str(ord(z[0]) ^ ord(z[1]))
        output += " "

    output_bytes = output.encode('ascii')
    base64_bytes = base64.b64encode(output_bytes)
    base64_message = base64_bytes.decode('ascii')

    return base64_message

def decode(input, key):
    input_bytes = input.encode('ascii')
    decoded_bytes = base64.b64decode(input_bytes)


    input_message = decoded_bytes.decode('ascii')

    input = input_message.split()

    zipped = zip(input, cycle(key))

    output = ""
    for z in zipped:
        output += (chr(int(z[0]) ^ ord(z[1])))

    return output

if __name__ == "__main__":
    while True:
        if os.stat("to_code.txt").st_size != 0:
            with open("to_code.txt", "r+") as file:
                l = file.readline()
                
                if l.find("encode") != -1:
                    msg = file.readline()
                    key = file.readline()
                    coded = encode(msg, key)
                    file.truncate(0)

                elif l.find("decode") != -1:
                    msg = file.readline()
                    key = file.readline()
                    coded = decode(msg, key)
                    file.truncate(0)

                with open("coded.txt", "w") as file2:
                    file2.write(coded)








    