from huffman_compression.huffman import HuffmanCoding
from utils.bit_converter import bytes_to_bits
import os

class HuffmanDecoding():

    def decode_file(self, path):

        decode = HuffmanCoding()

        with open(path, "rb") as f:
            bytes = f.read()

        bites = bytes_to_bits(bytes)

        tree_bits, text_bits = decode.divide_bits(bites)
        tree_root = decode.build_bits_to_tree(tree_bits)

        text = decode.build_bits_to_text(text_bits, tree_root)
        decoded_file_name = os.path.splitext(path)[0] + ".txt"
        with open(decoded_file_name, "w", encoding="utf-8") as encoded_file:
            encoded_file.write(text)

        return decoded_file_name
