
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


def test_remove_empty_spaces(text: str) -> str:
    new_text = str()

    for char in text:
        if not char.isspace():
            new_text += char

    return new_text


def words_into_list(text: str) -> list:

    new_text = str()

    for word in text:
        if word:
            new_text.append(word)

    return text.split(' ')




def main():
    ...


if __name__ == "__main__":
    main()
