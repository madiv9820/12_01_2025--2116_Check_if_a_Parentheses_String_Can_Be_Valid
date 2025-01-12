from Solution import Solution
from timeout_decorator import timeout
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ('))()))', '010100', True), 
                            2: ('()()', '0000', True), 
                            3: (')', '0', False),
                            4: ("())(()(()(())()())(())((())(()())((())))))(((((((())(()))))(", 
                                "100011110110011011010111100111011101111110000101001101001111", 
                                False),
                            5: ("))))(())((()))))((()((((((())())((()))((((())()()))(()",
                                "101100101111110000000101000101001010110001110000000101",
                                False),
                            6: ("))(())()((()))))(()()()()())(((())(())))))()(())()())(((((()()()()())))))())()((((())())()))())((()((((())))))())())((()((()))()(())()()(()))((()()()()((()(())))())((()())()(()))(()()()()(()()))))()((()()))()()()))())((((()((()(())()()(()(((()())",
                                "100110010100110101000010010010000101101000111010010100110100100110101100111011100111110101011010010101001110001110110001110001001010000011011100001111110100101110001001110101110101110110010001000111011011100101011001111001110111111111110001111011",
                                False)
                            }
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

    @timeout(0.5)
    def test_case_4(self):
        s, locked, output = self.__testcases[4]
        result = self.__obj.canBeValid(s = s, locked = locked)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_5(self):
        s, locked, output = self.__testcases[5]
        result = self.__obj.canBeValid(s = s, locked = locked)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_6(self):
        s, locked, output = self.__testcases[6]
        result = self.__obj.canBeValid(s = s, locked = locked)
        self.assertIsInstance(result, bool)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()