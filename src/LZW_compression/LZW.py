

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
        s = text[0]

        for i in range(len(text)):
            if i != len(text):
                next_char = text[i+1]
            else:
                next_char = ""
            
            new = s + next_char

            if new not in codes:
                compressed.append(codes[s])
                codes[new] = dict_size
                dict_size += 1
                s = next_char
            else:
                s = new
        
        compressed.append(codes[s])
        return codes

        