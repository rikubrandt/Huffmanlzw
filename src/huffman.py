from heapq import heapify, heappush, heappop

from collections import defaultdict
class HuffmanEncoding:
    def __init__(self, file):
        self.file = file

    
    def file_reader(self):
        with open(self.file) as r:
            while True:
                character = r.read(1)
                if character:
                    yield character
                else:
                    return

    def calculate_frequency(self):
        frequency = defaultdict(int)

        iterator = self.file_reader()
        while True:
            try:
                c = next(iterator)
                frequency[c] += 1
            except StopIteration:
                break

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

    def encode(self, root, s, dict):

        if root is None:
            return

        if root.isLeaf():
            dict[root.char] = s if len(s) > 0 else '1'
        self.encode(root.left, s+'0', dict)
        self.encode(root.right, s+'1', dict)





class HuffmanTreeNode():
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    # Override comparison function
    def __lt__(self, other):
        return self.freq < other.freq

    def isLeaf(self):
        if self.left is None and self.right is None:
            return True
        return False

    def set_right_node(self, right):
        self.right = right

    def set_left_node(self, left):
        self.left = left


    




if __name__ == "__main__":
    h = HuffmanEncoding("text.txt")

    freq = h.calculate_frequency()
    print(freq)
    root = h.generate_huffman_tree(freq)
    dict = {}
    h.encode(root, '', dict)

    print(dict)
   # print(s.left.left.left.left.freq)
    #print(s.right.freq)