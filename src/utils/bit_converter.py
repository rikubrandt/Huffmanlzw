
# Needed to get the length divided by 8
def add_additional_bits(bits):
    over = 8 - (len(bits) % 8)
    count = format(over, "08b")
    return count + over * "0"

def bits_to_bytes(bits):

    byte_array = bytearray()
    bits = add_additional_bits(bits) + bits
    for bit in range(0, len(bits), 8):
        byte = (bits[bit:bit+8])
        byte_array.append(int(byte, 2))
    return bytes(byte_array)

def bytes_to_bits(bytes):
    bits = ""
    for byte in bytes:
        bits += bin(byte)[2:].zfill(8)

    #Removes the extra bits
    extras = int(bits[:8], 2)
    return bits[8+extras:]
