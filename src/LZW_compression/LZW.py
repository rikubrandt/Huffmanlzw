

from bz2 import compress


class LZWCoding:

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
            if i != len(text)-1:
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
        return compressed

    def create_bits(self, compressed):
        
        max_bit_len = len(format(max(compressed), "b"))

        needed_bits = format(max_bit_len, "08b")

        bits = ""
        b = "{0:0" + str(needed_bits) + "b}"
        for code in compressed:
            print(b.format(code))
            bits += b.format(code)

        return needed_bits + bits

    def bits_to_list(self, bits):
        extras = int(bits[:8], 2)
        bits = bits[8+extras:]

        length = int(bits[:8], 2)
        bits = bits[8:]

        compressed = []

        for i in range(0, len(bits), length):
            compressed.append(int(bits[i:i+length], 2))

        return compressed

    def generate_text(self, compressed):
        codes = {}

        for i in compressed:
            if i < 256:
                codes[str(i)] = chr(i)
        
        dict_size = 256

        current = str(compressed[0])

        text = codes[current]

        for i in range(len(compressed)-1):
            next = str(compressed[i+1])

            if next in codes:
                char = codes[next][0]
            else:
                char = codes[current]

            chars = codes[current] + char
            codes[str(dict_size)] = chars
            dict_size += 1
            current = next
            text += codes[current]
        return text
