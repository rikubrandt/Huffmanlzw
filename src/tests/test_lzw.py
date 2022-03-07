import unittest
from Utils.bit_converter import bytes_to_bits
import os

from LZW_compression.LZW import LZWCoding
from LZW_compression.LZW_encoding import LZW_Encoding
from LZW_compression.LZW_decoding import LZW_Decoding

class TestLZW(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.lzw = LZWCoding()
        self.test_text = "This is a test text."
        self.test_compressed = [84, 104, 105, 115, 32, 258, 32, 97, 32, 116, 101, 115, 116, 264, 101, 120, 116, 46]
        self.test_bits = "00001001001010100001101000001101001001110011000100000100000010000100000001100001000100000001110100001100101001110011001110100100001000001100101001111000001110100000101110"

    ### ENCODING

    def test_compress(self):
        compressed = self.lzw.compress(self.test_text)
        self.assertEqual(compressed, self.test_compressed)

    def test_create_bits(self):
        bits = self.lzw.create_bits(self.test_compressed)
        print("BITS: ", bits)
        self.assertEqual(bits, self.test_bits)

    def test_lzw_compression(self):
        lzw_encoder = LZW_Encoding()
        path = self.path + "/lzwtest.txt"
        filename = lzw_encoder.encode_file(path)
        with open(filename, "rb") as f:
            bytes = f.read()
        bites = bytes_to_bits(bytes)
        self.assertEqual(bites, self.test_bits)

    ### DECODING
    def test_bits_to_list(self):
        list = self.lzw.bits_to_list(self.test_bits)
        self.assertEqual(list, self.test_compressed)

    def test_generate_text(self):
        text = self.lzw.generate_text(self.test_compressed)
        self.assertEqual(text, self.test_text)
    

    def test_lzw_decompression(self):
        lzw_decoder = LZW_Decoding()
        path = self.path + "/lzwtest.bin"
        filename = lzw_decoder.decode_file(path)
        with open(filename, "r") as f:
            text = f.read()
        self.assertEqual(text, self.test_text)