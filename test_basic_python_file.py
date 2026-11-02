import io
import unittest
from contextlib import redirect_stdout

from BasicPythonFile import divide_numbers


class TestDivideNumbers(unittest.TestCase):
    def test_division_with_different_arrays(self):
        test_arrays = [
            [10, 2, 5],
            [9, 3, 3],
            [7, 2, 3.5],
        ]

        for num1, num2, expected in test_arrays:
            with self.subTest(num1=num1, num2=num2):
                self.assertEqual(divide_numbers(num1, num2), expected)

    def test_prints_babaooey_when_result_is_four(self):
        output = io.StringIO()

        with redirect_stdout(output):
            result = divide_numbers(12, 3)

        self.assertEqual(result, 4)
        self.assertEqual(output.getvalue(), "babaooey\n")
    

if __name__ == "__main__":
    unittest.main()

