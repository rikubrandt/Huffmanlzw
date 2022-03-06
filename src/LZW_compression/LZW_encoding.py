
from LZW_compression.LZW import LZWCoding

from utils.bit_converter import bits_to_bytes
import os

class LZW_Encoding:
    def encode_file(self, path):
        encoder = LZWCoding()

        with open(path, "r") as f:
            text = f.read()
        compressed = encoder.compress(text)


        bits = encoder.create_bits(compressed)
        
        bytes = bits_to_bytes(bits)
        encoded_file_name = os.path.splitext(path)[0] + ".bin"
        with open(encoded_file_name, "wb") as encoded_file:
            encoded_file.write(bytes)
            
        return encoded_file_name
