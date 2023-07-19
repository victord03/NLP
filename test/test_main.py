from src import main


def test_remove_punctuation():

    text = 'While punctuation is great, it is important - imperative - to remove it for sentiment analysis!'
    expected = 'While punctuation is great it is important  imperative  to remove it for sentiment analysis'

    assert main.remove_punctuation(text) == expected


def test_remove_semantics():

    text = 'While punctuation is great it is important  imperative  to remove it for sentiment analysis'
    expected = 'punctuation is great is important  imperative  remove sentiment analysis'

    assert main.remove_semantics(text) == expected


def test_words_into_list():

    text = 'punctuation is great is important  imperative  remove sentiment analysis'
    expected = text.split(' ')

    assert main.words_into_list(text) == expected


def test_remove_empty_spaces():

    text = 'While punctuation is  great is important  imperative remove    sentiment analysis'
    expected = ['While', 'punctuation', 'is', 'great','is', 'important','imperative','remove','sentiment','analysis']

    assert main.test_remove_empty_spaces(text) == expected


def test_find_verbs():

    words = ['While', 'punctuation', 'is', 'great','is', 'important','imperative','remove','sentiment','analysis']
    expected = ['am', 'remove']

    assert main.find_verbs(words) == expected