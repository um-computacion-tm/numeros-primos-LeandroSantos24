import unittest

def is_primo(value):
    if value <= 1:
        return False
    elif value <= 3:
        return True
    elif value % 2 == 0 or value % 3 == 0:
        return False
    i = 5
    while i * i <= value:
        if value % i == 0 or value % (i + 2) == 0:
            return False
        i += 6
    return True


class TestPrimos(unittest.TestCase):
    def test_1(self):
        result = is_primo(1)
        self.assertEqual(result, False) 
        
    def test_2(self):
        result = is_primo(2)
        self.assertEqual(result, True)

    def test_3(self):
        result = is_primo(3)
        self.assertEqual(result, True)

    def test_4(self):
        result = is_primo(4)
        self.assertEqual(result, False)

    def test_5(self):
        result = is_primo(5)
        self.assertEqual(result, True)

    def test_6(self):
        result = is_primo(6)
        self.assertEqual(result, False)


unittest.main()