import unittest
from timeit import default_timer as timer
from libs.caching_fibonacci import caching_fibonacci


class TestCachingFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        fibonacci = caching_fibonacci()
        values = range(0, 10)
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for n, result in zip(values, expected):
            self.assertEqual(result, fibonacci(n))
    
    def test_caching_fibonacci(self):
        fibonacci = caching_fibonacci()
        n = 25
        start_cold = timer()
        fibonacci(n)
        end_cold = timer()

        start_hot = timer()
        fibonacci(n)
        end_hot = timer()

        cold = end_cold - start_cold
        hot = end_hot - start_hot

        self.assertEqual(cold / 10 > hot, True)
        

if __name__ == '__main__':
    unittest.main()
