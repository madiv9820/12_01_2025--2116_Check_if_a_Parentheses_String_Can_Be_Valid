from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ('))()))', '010100', True), 
                            2: ('()()', '0000', True), 
                            3: (')', '0', False)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        s, locked, output = self.__testcases[1]
        result = self.__obj.canBeValid(s = s, locked = locked)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        s, locked, output = self.__testcases[2]
        result = self.__obj.canBeValid(s = s, locked = locked)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        s, locked, output = self.__testcases[3]
        result = self.__obj.canBeValid(s = s, locked = locked)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()