# encoder_decoder_service

## to_use
* Write to **to_code.txt** to encode or decode.
* Read from **coded.txt** for coded message.

### Format
'''
command
message_to_code
key
'''

Notes:
* **command** must be "encode" or "decode", all lowercase with no quotation marks.
* Parameters must be separated by newline.

### Example of encoding in Python
'''
if __name__ == "__main__":
    with open("to_code.txt", "w") as file:
        file.write("encode\nhello world\ntest")
'''

### Example of decoding in Python
'''
if __name__ == "__main__":
    with open("to_code.txt", "w") as file:
        file.write("decode\nMjggMCAzMSAyNCAyNyA2OSA0IDI3IDYgOSAyMyAxMjYg\ntest")
'''
