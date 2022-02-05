from heapq import heapify, heappush, heappop
from huffman_tree_node import HuffmanTreeNode
from collections import defaultdict
class HuffmanCoding:
    def __init__(self):
        pass

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

        print(heap)

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


if __name__ == "__main__":
    h = HuffmanEncoding("text.txt")

    freq = h.calculate_frequency()
    print(freq)
    root = h.generate_huffman_tree(freq)
    dict = {}
    h.generate_codes(root, '', dict)

    print(dict)


   # print(s.left.left.left.left.freq)
    #print(s.right.freq)