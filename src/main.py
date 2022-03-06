from LZW_compression.LZW_encoding import LZW_Encoding
from LZW_compression.LZW_decoding import LZW_Decoding

from Huffman_compression.huffman_encoding import Huffman_Encoding
from Huffman_compression.huffman_decoding import Huffman_Decoding

def main():
    print("Text file compression.")
    while True:
        print("1. Encode text file.")
        print("2. Decode text file.")
        print("3. Exit.")
        num = input()

        if num == "1":
            encode()
        elif num == "2":
            decode()
        elif num == "3":
            print("Exiting...")
            break
        else:
            print("Invalid number. ")
            


def encode():
    while True:
            print("1. Huffman Encoding.")
            print("2. LZW Encoding.")
            print("3. Exit.")
            num = input()

            if num == "1":
                try:
                    path = input("Give file path.")
                    huffman_encode = Huffman_Encoding()
                    new_file = huffman_encode.encode_file(path)
                    print("File encoded to: ", new_file)
                    break
                except FileNotFoundError:
                    print("File not found.")
            elif num == "2":
                try:
                    path = input("Give file path.")
                    lzw_encode = LZW_Encoding()
                    new_file = lzw_encode.encode_file(path)
                    print("File encoded to: ", new_file)
                    break
                except FileNotFoundError:
                    print("File not found.")

            elif num == "3":
                print("Exiting...")
                break
            else:
                print("Invalid number. ")

def decode():
     while True:
            print("1. Huffman Decoding.")
            print("2. LZW Decoding.")
            print("3. Exit.")
            num = input()

            if num == "1":
                try:
                    path = input("Give file path.")
                    huffman_decode = Huffman_Decoding()
                    new_file = huffman_decode.decode_file(path)
                    print("File encoded to: ", new_file)
                    break
                except FileNotFoundError:
                    print("File not found.")
            elif num == "2":
                try:
                    path = input("Give file path.")
                    lzw_decode = LZW_Decoding()
                    new_file = lzw_decode.decode_file(path)
                    print("File decoded to: ", new_file)
                    break
                except FileNotFoundError:
                    print("File not found.")

            elif num == "3":
                print("Exiting...")
                break
            else:
                print("Invalid number. ")


if __name__ == "__main__":
    main()
