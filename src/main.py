

def split_text_in_sentences(text: str) -> list[str]:

    sentences = text.split('\n')
    stripped_sentences = list()

    for element in sentences:
        stripped_sentences.append(element.strip())

    return test_remove_empty_spaces(stripped_sentences)


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

    # todo: to become a separate file
    words_to_be_removed = ['while', 'and', 'the', 'to', 'it', 'for', 'by', 'on', 'in', 'as']

    new_text = list()

    for word in text.split(' '):
        if word.lower() not in words_to_be_removed:
            new_text.append(word)

    return ' '.join(new_text)


def words_into_list(text: str) -> list[str]:
    """Splits a text into a list of words (splits on white spaces)."""
    return text.split(' ')


def test_remove_empty_spaces(sentences: list[str]) -> list[str]:
    """Removes empty elements from a list of text split into words (more than one white space)."""

    sentences_copy = sentences.copy()

    count = 0

    for index, element in enumerate(sentences):
        if not element:
            del sentences_copy[index - count]
            count += 1

    return sentences_copy


def find_verbs(words: list[str]) -> list[str]:
    """Finds verbs within the text, in any tense and returns a list of unique verbs used, in the present tense."""

    # todo: to become a separate file
    verbs = {
        'am': ['am', 'are', 'is', 'was', 'be', 'were'],
        'do': ['do', 'does', 'did', 'done'],
        'remove': ['remove', 'removed'],
        'add': ['add', 'adds', 'added'],
    }

    found = list()

    for word in words:

        for verb, tense in verbs.items():
            if word in tense:
                if verb not in found:
                    found.append(verb)

    return found


def main():
    ...


if __name__ == "__main__":
    main()
