import unittest
from random import randint
from maximum_pairwise_product import max_pairwise_product_naive, max_pairwise_product

class TestMaxPairwiseProduct(unittest.TestCase):
    def test_small(self):
        print("test_small start")
        self.assertEqual(max_pairwise_product([1, 2, 3]), 6)
        self.assertEqual(max_pairwise_product([9, 3, 2]), 27)
        self.assertEqual(max_pairwise_product([7, 3, 7, 2]), 49)
        self.assertEqual(max_pairwise_product([3, 3, 3, 3]), 9)
        self.assertEqual(max_pairwise_product([1, 31, 30, 3]), 930)
        print("test_small complete")

    def test_stress(self):
        print("test_stress start")
        number_of_iterations = 10
        array_size = 100
        max_number = 2 * 10**5

        for _ in range(number_of_iterations):
            numbers = [randint(0, max_number) for _ in range(array_size)]
            self.assertEqual(max_pairwise_product(list(numbers)), max_pairwise_product_naive(numbers))
        print("test_stress end")

    def test_large(self):
        print("test_large start")
        self.assertEqual(max_pairwise_product([4] * (2 * 10**5)), 16)
        self.assertEqual(max_pairwise_product([x for x in range(10**5)]), (10**5 - 1) * (10**5 - 2))
        self.assertEqual(max_pairwise_product([1] * (2 * 10**5)), 1)
        self.assertEqual(max_pairwise_product([1] * (2 * 10**5)), 1)
        self.assertEqual(max_pairwise_product([1] * (2 * 10**5)), 1)

if __name__ == '__main__':
    unittest.main()
