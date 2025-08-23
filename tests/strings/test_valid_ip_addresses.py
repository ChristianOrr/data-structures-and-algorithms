import pytest

from strings.valid_ip_addresses import (
    valid_ip_addresses_1,
)

implementations = [valid_ip_addresses_1]


@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    test = "1921680"
    out = fn(test)
    
    expected = [
        "1.9.216.80",
        "1.92.16.80",
        "1.92.168.0",
        "19.2.16.80",
        "19.2.168.0",
        "19.21.6.80",
        "19.21.68.0",
        "19.216.8.0",
        "192.1.6.80",
        "192.1.68.0",
        "192.16.8.0"
    ]
    assert set(out) == set(expected)