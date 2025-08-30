import pytest

from strings.generate_document import (
    generate_document_1,
    generate_document_2
)

implementations = [generate_document_1, generate_document_2]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_basic(fn):
    characters = "atGent!ne reumeDoc"
    document = "Generate Document!"
    expected = True
    actual = fn(characters, document)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_capital_letter(fn):
    characters = "L"
    document = "l"
    expected = False
    actual = fn(characters, document)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_lower_letter(fn):
    characters = "l"
    document = "l"
    expected = True
    actual = fn(characters, document)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_empty_string(fn):
    characters = ""
    document = ""
    expected = True
    actual = fn(characters, document)
    assert actual == expected