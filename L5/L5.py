import unittest


def Factorial(num):
    res = 1
    while (num > 1):
        res = num * res
        num = num-1
    return res


class FactorialTestCase(unittest.TestCase):
    def test1(self):
        res = factorial(5)
        self.assertEqual(res, 120)

    def test2(self):
        res = factorial(6)
        self.assertEqual(res, 720)

    def test3(self):
        res = factorial(0)
        self.assertEqual(res, 1)


if __name__ == '__main__':
    print(factorial(5))
