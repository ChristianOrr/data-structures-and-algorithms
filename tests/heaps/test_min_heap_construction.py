import pytest

from heaps.min_heap_construction import (
    is_min_heap_property_satisfied,
    MinHeap
)

implementations = [MinHeap]

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_1(fn):
    minHeap = fn([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
    minHeap.insert(76)
    assert is_min_heap_property_satisfied(minHeap.heap)
    assert minHeap.peek() == -5
    assert minHeap.remove() == -5
    assert is_min_heap_property_satisfied(minHeap.heap)
    assert minHeap.peek() == 2
    assert minHeap.remove() == 2
    assert is_min_heap_property_satisfied(minHeap.heap)
    assert minHeap.peek() == 6
    minHeap.insert(87)
    assert is_min_heap_property_satisfied(minHeap.heap)

@pytest.mark.parametrize("fn", implementations, ids=[f.__name__ for f in implementations])
def test_2(fn):
    minHeap = fn([2, 3, 1])
    assert is_min_heap_property_satisfied(minHeap.heap)
    assert minHeap.peek() == 1
    assert is_min_heap_property_satisfied(minHeap.heap)
    assert minHeap.peek() == 1