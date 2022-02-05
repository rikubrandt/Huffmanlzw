from heapq import heapify, heappush, heappop
from huffman_tree_node import HuffmanTreeNode
from collections import defaultdict

class HuffmanCoding:
    def __init__(self):
        self.tree_bits = ""

    def calculate_frequency(self, text):
        frequency = defaultdict(int)

        for char in text:
            frequency[char] += 1

        return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))


    def generate_huffman_tree(self, dict):
        heap = []
        heapify(heap)

        for char, freq in dict.items():
            heappush(heap, HuffmanTreeNode(char, freq))

        for _ in range(len(heap)-1):
            left = heappop(heap)
            right = heappop(heap)
            heappush(heap, HuffmanTreeNode(
                        char=None,
                        freq=left.freq+right.freq,
                        left=left,
                        right=right))

        return heappop(heap)

    def generate_codes(self, root, s, dict):

        if root is None:
            return

        if root.isLeaf():
            dict[root.char] = s if len(s) > 0 else '1'
        self.generate_codes(root.left, s+'0', dict)
        self.generate_codes(root.right, s+'1', dict)

    def generate_encoded_text(self, dict, text):
        s = ''
        for char in text:
            s += dict.get(char)
        return s


    def huffman_tree_to_bits(self, root):
        self.tree_bits = ""

        def rec(root):
            if root.isLeaf():
                self.tree_bits += "0" + format(ord(root.char), "b")
            else:
                rec(root.left)
                rec(root.right)
            return self.tree_bits
        return rec(root)
    
    def divide_bits(self, bits):
        tree_bit_count = int(bits[:16], 2)
        bits = bits[16:]

        return bits[:tree_bit_count], bits[tree_bit_count:]