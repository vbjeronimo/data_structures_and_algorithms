
from typing import Any


class Vector:

    _arr: list[Any]
    _capacity: int
    _size: int

    def __init__(self, capacity) -> None:
        self._arr = list()
        self._capacity = capacity
        self._size = 0

    def size(self) -> int:
        return self._size

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        return self._size == 0

    def at(self, index:int) -> Any:
        """
        O(1): Constant time to write to/read from any element.
        """
        if index < -self._size or index >= self._size:
            raise IndexError

        return self._arr[index]

    def push(self, value) -> None:
        """
        O(1): Constant time to push element if vector is not full
        O(n): Linear time if vector is full (all elements from the internal
                array need to be copied to a larger array)
        """
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        self._arr.insert(self._size, value)
        self._size += 1

    def _resize(self, new_capacity) -> None:
        new_arr = [i for i in self._arr]
        self._arr = new_arr
        self._capacity = new_capacity
    
