import pytest

from strings.caesar_cipher_encryptor import (
    caesar_cipher_encryptor_1,
)

implementations = [caesar_cipher_encryptor_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_basic(fn):
    assert fn("xyz", 2) == "zab"

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_wrap_around(fn):
    assert fn("xyz", 30) == "bcd"

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_no_shift(fn):
    assert fn("sdfghwe", 0) == "sdfghwe"