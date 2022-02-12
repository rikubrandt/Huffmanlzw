from huffman import HuffmanCoding
from bit_converter import bytes_to_bits

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

        print(tree_root.char)
        print(tree_root.right)
        #print(tree_root.left.right)



        #text = decode.build_bits_to_text(text_bits, tree_root)
        

        #print(text)


h = Huffman_Decoding()
h.decode_file("text.bin")