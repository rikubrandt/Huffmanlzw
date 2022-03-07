from heapq import heapify, heappush, heappop
from huffman_compression.huffman_tree_node import HuffmanTreeNode
from collections import defaultdict

class HuffmanCoding:
    def __init__(self):
        self.tree_bits = ""

    def calculate_frequency(self, text):
        frequency = defaultdict(int)

        for char in text:
            frequency[char] += 1

        return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))


    def generate_huffman_tree(self, table):
        heap = []
        heapify(heap)

        for char, freq in table.items():
            heappush(heap, HuffmanTreeNode(char=char, freq=freq))

        while len(heap)!= 1:
            left = heappop(heap)
            right = heappop(heap)
            heappush(heap, HuffmanTreeNode(
                        char=None,
                        freq=(left.freq+right.freq),
                        left=left,
                        right=right))

        return heappop(heap)

    # Generates the dictionary of the huffman tree, used for encoding.
    def generate_codes(self, root, string, table):
        if root is None:
            return

        if root.char is not None:
            table[root.char] = string
        self.generate_codes(root.left, string+"0", table)
        self.generate_codes(root.right, string+"1", table)

    def generate_encoded_text(self, table, text):
        string = ""
        for char in text:
            string += table.get(char)
        return string

    # Turns the tree structure to bits for encoding.
    def huffman_tree_to_bits(self, root):
        self.tree_bits = ""

        def rec(node):
            if node.is_leaf():
                self.tree_bits += "1" + format(ord(node.char), "08b")
            else:
                self.tree_bits += "0"
                rec(node.left)
                rec(node.right)
            return self.tree_bits
        return rec(root)

    # Divide treebits and text bits from the encoded bits.
    def divide_bits(self, bits):

        tree_bit_count = int(bits[:16], 2)
        bits = bits[16:]

        return bits[:tree_bit_count], bits[tree_bit_count:]

    def build_bits_to_tree(self, bits):
        root = HuffmanTreeNode()
        stack = [root]
        i = 1

        while i < len(bits):
            last = stack[-1]
            if bits[i] == "0":
                node = HuffmanTreeNode()
                if last.left is None:
                    last.set_left_node(node)
                    stack.append(node)
                else:
                    last.set_right_node(node)
                    stack.pop()
                    stack.append(node)
            else:
                # Get character from the bits.
                character = chr(int(bits[i+1: i+9], base=2))
                #print(character)
                i += 8
                node = HuffmanTreeNode(char=character)
                if last.left is None:
                    last.set_left_node(node)
                else:
                    last.set_right_node(node)
                    stack.pop()
            i += 1
        return root

    def build_bits_to_text(self, bits, root):
        node = root
        text = ""
        if node.char is not None:
            return node.char * len(bits)

        for bit in bits:
            if bit == "0":
                node = node.left
            else:
                node = node.right
            if node.is_leaf():
                text = text + node.char
                node = root
        return text
