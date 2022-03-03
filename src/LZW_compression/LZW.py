

class LZWCoding:
    def __init__(self):
        pass


    def compress(self, text):
        codes = {}

        for c in text:
            if c not in codes:
                codes[c] = ord(c)

        s = ""

        dict_size = 256

        compressed = []

        for c in text:
            string_c = s + c
            if string_c in codes:
                s = string_c
            else:
                compressed.append(codes[s])
                s = c
        
        if s in codes:
            compressed.append(codes[s])
        
        print(compressed)