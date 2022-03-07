

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

        maxlength = len(format(max(compressed), "b"))

        needed_bits = format(maxlength, "08b")

        bits = ""
        for c in compressed:
            b = "{0:0" + str(maxlength) + "b}"
            bits += b.format(c)

        return needed_bits + bits

    def bits_to_list(self, bits):
        length = int(bits[:8], 2)
        bits = bits[8:]

        return [int(bits[i:i+length], 2) for i in range(0, len(bits), length)]

    def generate_text(self, compressed):
        codes = {}
        for n in compressed:
            if n < 256:
                codes[str(n)] = chr(n)

        dict_size = 256
        current = str(compressed[0])
        text = codes[current]

        for i in range(len(compressed)-1):
            next_char = str(compressed[i+1])
            char = codes[next_char][0] if next_char in codes else codes[current]

            chars = codes[current] + char
            codes[str(dict_size)] = chars

            dict_size += 1
            current = next_char
            text += codes[current]

        return text
