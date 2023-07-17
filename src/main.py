
def remove_punctuation(text: str) -> str:
    """Removed all provided punctuation from the text."""

    punctuation_to_be_removed = ['!', ',', '-', '\'', '\"', '[', ']', '?', '.', '(', ')']

    new_text = str()

    for char in text:
        if char not in punctuation_to_be_removed:
            new_text += char

    return new_text


def remove_semantics(text: str) -> str:
    """Removed all provided punctuation from the text."""

    words_to_be_removed = ['while', 'and', 'the', 'to', 'it', 'for', 'by', 'on', 'in', 'as']

    new_text = list()

    for word in text.split(' '):
        if word.lower() not in words_to_be_removed:
            new_text.append(word)

    return ' '.join(new_text)


def words_into_list(text: str) -> list:
    return text.split(' ')


def test_remove_empty_spaces(text: str) -> list:

    words = words_into_list(text)
    words_copy = words.copy()

    count = 0

    for index, element in enumerate(words):
        if not element:
            del words_copy[index - count]
            count += 1

    return words_copy


def main():
    ...


if __name__ == "__main__":
    main()
