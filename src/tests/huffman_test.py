import unittest

import os
from Huffman_compression.huffman import HuffmanCoding
from Huffman_compression.huffman_encoding import Huffman_Encoding
from Huffman_compression.bit_converter import bytes_to_bits

class TestHuffman(unittest.TestCase):

    def setUp(self):
        self.huffman = HuffmanCoding()
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.test_text = "This a test text hello 123."
        self.frequency = {' ': 5, 't': 4, 'e': 3, 'h': 2, 's': 2, 'l': 2, 'T': 1, 'i': 1, 'a': 1, 'x': 1, 'o': 1, '1': 1, '2': 1, '3': 1, '.': 1}
        self.tree = self.huffman.generate_huffman_tree(self.frequency)
        self.codes = {' ': '00', 'e': '010', 'a': '0110', 'l': '0111', 't': '100', '2': '10100', 'i': '10101', 's': '1011', 'T': '11000', '1': '11001', 'h': '1101', '3': '11100', '.': '11101', 'x': '11110', 'o': '11111'}
        self.encoded = "110001101101011011000110001000101011100001000101111010000110101001110111111110011001101001110011101"
        self.encoded_tree = "00100100000010110010101011000011011011000010111010000100110010101101001101110011000101010100100110001101101000001001100111001011100101111000101101111"
        self.tree_length = format(len(self.encoded_tree), "016b")
        self.combined_bits = self.tree_length + self.encoded_tree + self.encoded


    ### ENCODING
    def test_calculate_frequency(self):
        freq = self.huffman.calculate_frequency(self.test_text)
        self.assertEqual(freq, self.frequency)

    def test_generate_huffman_tree(self):
        tree = self.huffman.generate_huffman_tree(self.frequency)
        self.assertEqual(tree.char, None)

    def test_generate_codes(self):
        table = {}
        self.huffman.generate_codes(self.tree, "", table)
        self.assertEqual(table, self.codes)

    def test_generate_encoded_text(self):
        encoded_text = self.huffman.generate_encoded_text(self.codes, self.test_text)
        self.assertEqual(encoded_text, self.encoded)

    def test_tree_to_bits(self):
        bits = self.huffman.huffman_tree_to_bits(self.tree)
        self.assertEqual(bits, self.encoded_tree)
    
    def test_huffman_compression(self):
        huffman_encoder = Huffman_Encoding()
        path = self.path + "/text.txt"
        filename = huffman_encoder.encode_file(path)
        with open(filename, "rb") as f:
            bytes = f.read()
        bites = bytes_to_bits(bytes)
        self.assertEqual(bites, self.combined_bits)

    ### DECODING

    def test_divide_bits(self):
        tree_bits, text_bits = self.huffman.divide_bits(self.combined_bits)
        self.assertEqual(tree_bits, self.encoded_tree)
        self.assertEqual(text_bits, self.encoded)

    def test_bits_to_tree(self):
        tree_root = self.huffman.build_bits_to_tree(self.encoded_tree)
        self.assertEqual(tree_root.char, self.tree.char)
        self.assertEqual(tree_root.left.char, self.tree.left.char)
        self.assertEqual(tree_root.right.char, self.tree.right.char)