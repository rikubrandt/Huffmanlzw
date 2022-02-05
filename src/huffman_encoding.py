
from huffman import HuffmanCoding

class Huffman_Encoding():

    def encode_file(path):

        encode = HuffmanCoding()

        with open(path, "r") as f:
            text = f.read()
        
        freq = encode.calculate_frequency(text)
        root = encode.generate_huffman_tree(freq)
        dict = {}
        encode.generate_codes(root, '', dict)

        encoded_text = encode.generate_encoded_text(dict, text)
        print(encoded_text)
h = Huffman_Encoding
h.encode_file(path='text.txt')