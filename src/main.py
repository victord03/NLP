from input_output.io_ops import open_file


def main():
    """Main Func"""

    file_path = r'C:\Users\3tr0001\Desktop\nlp.txt'

    text = open_file(file_path)
    print(text)

    # text_as_lists = text.split("\n")
    # print(text_as_lists)


if __name__ == "__main__":
    main()
