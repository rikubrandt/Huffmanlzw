

class LZWCoding:

    def compress(self, text):
        codes = {}

        for char in text:
            if char not in codes:
                codes[char] = ord(char)

        dict_size = 256

        compressed = []
        current = text[0]

        for i in range(len(text)):
            if i != len(text)-1:
                next_char = text[i+1]
            else:
                next_char = ""
            new = current + next_char

            if new not in codes:
                compressed.append(codes[s])
                codes[new] = dict_size
                dict_size += 1
                current = next_char
            else:
                current = new

        compressed.append(codes[current])
        return compressed

    def create_bits(self, compressed):

        maxlength = len(format(max(compressed), "b"))

        needed_bits = format(maxlength, "08b")

        bits = ""
        for char in compressed:
            binary = "{0:0" + str(maxlength) + "b}"
            bits += binary.format(char)

        return needed_bits + bits

    def bits_to_list(self, bits):
        length = int(bits[:8], 2)
        bits = bits[8:]

        return [int(bits[i:i+length], 2) for i in range(0, len(bits), length)]

    def generate_text(self, compressed):
        codes = {}
        for item in compressed:
            if item < 256:
                codes[str(item)] = chr(item)

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
