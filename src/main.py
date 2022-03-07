from lzw_compression.LZW_encoding import LZWEncoding
from lzw_compression.LZW_decoding import LZWDecoding

from huffman_compression.huffman_encoding import HuffmanEncoding
from huffman_compression.huffman_decoding import HuffmanDecoding
import os
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
                huffman_encode = HuffmanEncoding()
                new_file = huffman_encode.encode_file(path)
                print("File encoded to: ", new_file)
                print(f"Compressed file is {count_compression(path, new_file)}%  smaller.")
                break
            except FileNotFoundError:
                print("File not found.")
        elif num == "2":
            try:
                path = input("Give file path.")
                lzw_encode = LZWEncoding()
                new_file = lzw_encode.encode_file(path)
                print("File encoded to: ", new_file)
                print(f"Compressed file is {count_compression(path, new_file)}%  smaller.")
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
                huffman_decode = HuffmanDecoding()
                new_file = huffman_decode.decode_file(path)
                print("File encoded to: ", new_file)
                break
            except FileNotFoundError:
                print("File not found.")
        elif num == "2":
            try:
                path = input("Give file path.")
                lzw_decode = LZWDecoding()
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

def count_compression(path, encoded_path):
    original_size = os.path.getsize(path)
    compressed_size = os.path.getsize(encoded_path)
    return round((1-compressed_size/original_size)*100, 2)

if __name__ == "__main__":
    main()
