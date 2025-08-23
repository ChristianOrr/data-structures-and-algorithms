import pytest

from strings.generate_document import (
    generate_document_1,
)

implementations = [generate_document_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    characters = "atGent!ne reumeDoc"
    document = "Generate Document!"
    expected = True
    actual = fn(characters, document)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    characters = "L"
    document = "l"
    expected = False
    actual = fn(characters, document)
    assert actual == expected

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_3(fn):
    characters = "l"
    document = "l"
    expected = True
    actual = fn(characters, document)
    assert actual == expected