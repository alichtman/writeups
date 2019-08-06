# Quackme Solver -- picoCTF2018
# alichtman

import pwn
import json
import r2pipe
import codecs
import binascii

# Open file in r2 and perform auto-analysis
r2 = r2pipe.open("quackme-main")
r2.cmd('aaaa')

# Print obj.greetingMessage as string in json format,
# then extract only the first sentence from it.
greetingJSON = json.loads(r2.cmd("pfj S @ obj.greetingMessage")[1:-2])
greeting = greetingJSON["string"].split("\\u000")[0].strip()

# Extract sekrutBuffer
r2.cmd("s obj.sekrutBuffer")
buf = r2.cmd("pxj 25").strip()[1:-1].split(",")
hex_array = [int(hex_num) for hex_num in buf]
ascii_decoded = binascii.hexlify(bytearray(hex_array)).decode('ascii')
decode_hex = codecs.getdecoder("hex_codec")
sekrut_buffer = decode_hex(ascii_decoded)[0]

# XOR the greeting and the buffer to get the flag
res = str(pwn.xor(greeting, sekrut_buffer))
flag = res[2:len(sekrut_buffer) + 2]
print("FLAG:", flag)
