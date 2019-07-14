# Quackme Solver -- picoCTF2018
# alichtman

import pwn
import json
import r2pipe
import codecs

# Open file in r2 and perform auto-analysis
r2 = r2pipe.open("../ctf-files/quackme-main")
r2.cmd('aaaa')

# Print obj.greetingMessage as string in json format,
# then extract only the first sentence from it.
greetingJSON = json.loads(r2.cmd("pfj S @ obj.greetingMessage")[1:-2])
greeting = greetingJSON["string"].split("\\u000")[0].strip()

# Extract sekrutBuffer
r2.cmd("s obj.sekrutBuffer")
buf = r2.cmd("px0")
decode_hex = codecs.getdecoder("hex_codec")
sekrut_buffer = decode_hex(buf.strip() + "00")[0]

# XOR to get our flag, and add the last bracket (because this
# buffer somehow extends past a NULL byte??? There's a hanging 0x5D
# afterwards that would produce a closing bracket. When I solved this
# manually, it was in my hex and the fully flag decrypted properly
# *shrugs*)
res = str(pwn.xor(greeting, sekrut_buffer))
flag = res[2:len(sekrut_buffer) + 2] + "}"
print("FLAG:", flag)
