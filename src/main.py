


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
    pass

def decode():
    pass


if __name__ == "__main__":
    main()
