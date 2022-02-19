import unittest

from Huffman_compression.huffman import HuffmanCoding

class TestHuffman(unittest.TestCase):

    def setUp(self):
        self.huffman = HuffmanCoding()
        self.test_text = "This a test text hello 123."


    def test_calculate_frequency(self):
        freq = self.huffman.calculate_frequency(self.test_text)
        self.assertEqual(freq, {' ': 5, 't': 4, 'e': 3, 'h': 2, 's': 2, 'l': 2, 'T': 1, 'i': 1, 'a': 1, 'x': 1, 'o': 1, '1': 1, '2': 1, '3': 1, '.': 1}
)

    