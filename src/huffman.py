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
                        freq=(left.freq+right.freq),
                        left=left,
                        right=right))

        return heappop(heap)

    # Generates the dictionary of the huffman tree, used for encoding.
    def generate_codes(self, root, s, dict):

        if root is None:
            return

        if root.char is not None:
            dict[root.char] = s
        self.generate_codes(root.left, s+"0", dict)
        self.generate_codes(root.right, s+"1", dict)

    
    def generate_encoded_text(self, dict, text):
        s = ""
        for char in text:
            s += dict.get(char)
        return s

    # Turns the tree structure to bits for encoding.
    def huffman_tree_to_bits(self, root):
        self.tree_bits = ""

        def rec(root):
            if root.isLeaf():
                self.tree_bits += "1" + format(ord(root.char), "08b")
            else:
                self.tree_bits += "0"
                rec(root.left)
                rec(root.right)
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
                if self.add_child_to_node(last, node):
                    stack.pop()
            else:
                # Get character from the bits.
                character = chr(int(bits[i+1: i+9], base=2))
                print(character)
                i += 8
                node = HuffmanTreeNode(char=character)

                if self.add_child_to_node(last, node):
                    stack.pop()
            stack.append(node)
            i +=1
        return root
    
    # Adds child to left first then right, returns true for deletion purposes.
    def add_child_to_node(self, parent, node):
                if parent.left is None:
                    parent.set_left_node(node)
                    return False
                else:
                    parent.set_right_node(node)
                    return True

    def build_bits_to_text(self, bits, root):
        node = root
        print(root)
        text = ""

        for bit in bits:
            if node.char is not None:
                print(node.char)
            if bit == "0":
                node = node.left
            else:
                node = node.right

        return text