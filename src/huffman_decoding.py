

from huffman import HuffmanCoding
from huffman import HuffmanCoding
import os

class Huffman_Decoding():

    def decode_file(self, path):

        decode = HuffmanCoding()

        with open(path, "rb") as f:
            bytes = f.read()

        