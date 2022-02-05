

def bits_to_bytes(bits):
    
    bytes = bytearray()
    
    for b in range(0, len(bits), 8):
        byte = (bits[b:b+8])
        bytes.append(int(byte, 2))

    return bytes(bytes)