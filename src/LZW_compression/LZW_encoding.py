
from LZW import LZWCoding


class LZW_Encoding:
    def encode():
        encoder = LZWCoding()

        compressed = encoder.compress("IIINI asdasdasddasdas")

        print(compressed)
