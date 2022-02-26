

class LZWCoding:
    def __init__(self):
        pass


    def create_list(self, text):
        codes = {}

        for c in text:
            if c not in codes:
                codes[c] = ord(c)

        ###TODO