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

    def generate_bits(self, root):

        bits = ""


    def generate_file(self):
        pass



class HuffmanTreeNode():
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.direction = ""
    
    def __lt__(self, other):
        return self.freq < other.freq

    def set_right_node(self, right):
        self.right = right

    def set_left_node(self, left):
        self.left = left


    




if __name__ == "__main__":
    h = HuffmanEncoding("text.txt")

    freq = h.calculate_frequency()
    print(freq)
    tree = h.generate_huffman_tree(freq)

    x = h.tree_to_bits(tree)
    print(x)
   # print(s.left.left.left.left.freq)
    #print(s.right.freq)