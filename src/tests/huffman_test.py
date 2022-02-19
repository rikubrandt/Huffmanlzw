import unittest

from Huffman_compression.huffman import HuffmanCoding

class TestHuffman(unittest.TestCase):

    def setUp(self):
        self.huffman = HuffmanCoding()
        self.test_text = "This a test text hello 123."


    def test_calculate_frequency(self):
        freq = self.huffman.calculate_frequency(self.test_text)
        self.assertEqual(freq, )

    