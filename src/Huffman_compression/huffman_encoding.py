
from Huffman_compression.huffman import HuffmanCoding

import os
from utils.bit_converter import bits_to_bytes

class Huffman_Encoding():

    def encode_file(self, path):

        encode = HuffmanCoding()

        with open(path, "r") as f:
            text = f.read()
   
        freq = encode.calculate_frequency(text)
        print(freq)
        root = encode.generate_huffman_tree(freq)
        dict = {}
        encode.generate_codes(root, '', dict)

        encoded_text = encode.generate_encoded_text(dict, text)

        treebits = encode.huffman_tree_to_bits(root)
        
        #Treebits length converted to binary (max 65k)
        tree_bits_length = format(len(treebits), "016b")

        combined_bits = tree_bits_length + treebits + encoded_text

        combined_bytes = bits_to_bytes(combined_bits)
        
        encoded_file_name = os.path.splitext(path)[0] + ".bin"
        with open(encoded_file_name, "wb") as encoded_file:
            encoded_file.write(combined_bytes)
        return encoded_file_name
