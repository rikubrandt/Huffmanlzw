from huffman import HuffmanCoding
from utils.bit_converter import bytes_to_bits
import os

class Huffman_Decoding():

    def decode_file(self, path):

        decode = HuffmanCoding()

        with open(path, "rb") as f:
            bytes = f.read()

        bites = bytes_to_bits(bytes)

        tree_bits, text_bits = decode.divide_bits(bites)

        #print("Treebits: ", tree_bits)
        #print("Text bits: ", text_bits)
        tree_root = decode.build_bits_to_tree(tree_bits)

        print("Tree bits: ", tree_bits)
        print("Text bits: ", text_bits)

        text = decode.build_bits_to_text(text_bits, tree_root)
        decoded_file_name = os.path.splitext(path)[0] + ".txt"
        with open(decoded_file_name, "w") as encoded_file:
            encoded_file.write(bytes)

        return decoded_file_name

h = Huffman_Decoding()
h.decode_file("text.bin")