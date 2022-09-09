import unittest

from src.vector import Vector

class TestVector(unittest.TestCase):

    def setUp(self) -> None:
        self.max_capacity = 5
        self.vector = Vector(self.max_capacity);


    def test_is_empty_is_true_when_size_is_zero(self):
        self.assertTrue(self.vector.is_empty())

    def test_is_empty_is_false_when_size_is_not_zero(self):
        self.vector.push(0)
        self.assertFalse(self.vector.is_empty())


    def test_at_returns_value_when_in_range(self):
        self.vector.push(5)
        self.assertEqual(self.vector.at(0), 5)

    def test_at_return_value_with_negative_index_in_range(self):
        self.vector.push(5)
        self.assertEqual(self.vector.at(-1), 5)

    def test_at_raises_exception_when_i_exceeds_upper_range(self):
        self.vector.push(5)
        with self.assertRaises(IndexError):
            self.vector.at(100)

    def test_at_raises_exception_when_i_exceeds_lower_range(self):
        self.vector.push(5)
        with self.assertRaises(IndexError):
            self.vector.at(-100)


    def test_push_appends_value_to_vector(self):
        self.vector.push('value')
        self.assertEqual(self.vector.at(self.vector.size()-1), 'value')

    def test_push_resizes_vector_if_array_is_full(self):
        for i in range(0, 6):
            self.vector.push(i)

        self.assertEqual(self.vector.capacity(), self.max_capacity*2)

if __name__ == '__main__':
    unittest.main()
