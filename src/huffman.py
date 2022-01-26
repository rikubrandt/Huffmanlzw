
class HuffmanEncoding:
    def __init__(self, file):
        self.file = file

    
    def file_reader(self):
        with open(self.file) as r:
            while True:
                character = r.read(1)
                if character:
                    yield character
                else:
                    return

    def calculate_frequency(self):
        frequency = {}

        iterator = self.file_reader()
        while True:
            try:
                c = next(iterator)
                #Adds a new key with value 1 or increments it.
                frequency[c] = frequency.get(c, 0) +1
            except StopIteration:
                break

        return dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))

if __name__ == "__main__":
    h = HuffmanEncoding("text.txt")

    dic = h.calculate_frequency()

    print(dic)
    print(dic)