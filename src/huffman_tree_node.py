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
        return self.left is None and self.right is None

    def set_right_node(self, right):
        self.right = right

    def set_left_node(self, left):
        self.left = left
