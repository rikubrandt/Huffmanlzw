
from lzw_compression.LZW import LZWCoding

from utils.bit_converter import bytes_to_bits
import os




class LZWDecoding:
    def decode_file(self, path):
        decoder = LZWCoding()

        with open(path, "rb") as file:
            bytes = file.read()
            bits = bytes_to_bits(bytes)
            compressed_list = decoder.bits_to_list(bits)
            text = decoder.generate_text(compressed_list)

            decoded_filename = os.path.splitext(path)[0]
            decoded_filename += ".txt"
        with open(decoded_filename, "w", encoding="utf-8") as decoded:
            decoded.write(text)

        return decoded_filename
        