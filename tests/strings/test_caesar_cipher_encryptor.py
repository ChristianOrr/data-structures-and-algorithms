import pytest

from strings.caesar_cipher_encryptor import (
    caesar_cipher_encryptor_1,
)

implementations = [caesar_cipher_encryptor_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    assert fn("xyz", 2) == "zab"