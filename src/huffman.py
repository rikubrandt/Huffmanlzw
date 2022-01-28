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
        pass

    def generate_file(self):
        pass




class HuffmanTreeNode():
    def __init__(self, char, freq=None, left=None, right=None):
        char = self.char
        freq = self.freq
        left = self.left
        right = self.right

    def set_right_node(self, right):
        self.right = right

    def set_left_node(self, left):
        self.left = left


if __name__ == "__main__":
    h = HuffmanEncoding("text.txt")

    dic = h.calculate_frequency()

    print(dic)
    print(dic)