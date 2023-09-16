import unittest
import re
from ast_loader import AstLoader
from app.interpreter import Interpreter
from tests.stdout_capture import StdoutCapture


class EvaluatorTests(unittest.TestCase):
    def test_something(self):
        with StdoutCapture() as capture:
            # Your code that generates output to stdout
            print("Hello, this is captured stdout")

        captured_output = capture.get_output()
        self.assertEqual("Hello, this is captured stdout\n", captured_output)  # add assertion here

    def test_print(self):
        ast = AstLoader.load_json_file("testdata/static_string_print.json")
        interpreter = Interpreter()

        with StdoutCapture() as capture:
            interpreter.eval_print(ast['expression'])
        captured_output = capture.get_output()

        self.assertEqual("hello world\n", captured_output)

    def test_print_with_print_inside(self):
        ast = AstLoader.load_json_file("testdata/print_in_print.json")
        interpreter = Interpreter()

        with StdoutCapture() as capture:
            interpreter.eval_print(ast['expression'])
        captured_output = capture.get_output()

        self.assertEqual("hello world\nhello world\n", captured_output)

    def test_print_concatenated_strings(self):
        ast = AstLoader.load_json_file("testdata/print_concatenated_string.json")
        interpreter = Interpreter()

        with StdoutCapture() as capture:
            interpreter.eval_print(ast['expression'])
        captured_output = capture.get_output()

        self.assertEqual("hello world\n", captured_output)

    def test_print_sum_numbers(self):
        ast = AstLoader.load_json_file("testdata/print_sum_numbers.json")
        interpreter = Interpreter()

        with StdoutCapture() as capture:
            interpreter.eval_print(ast['expression'])
        captured_output = capture.get_output()

        self.assertEqual(str(1332), re.sub(r'\n', '', captured_output))

    def test_print_number_and_string_concatenated(self):
        ast = AstLoader.load_json_file("testdata/print_number_and_string_concatenated.json")
        interpreter = Interpreter()

        with StdoutCapture() as capture:
            interpreter.eval_print(ast['expression'])
        captured_output = capture.get_output()

        self.assertEqual("666666\n", captured_output)

    def test_print_function_in_function(self):
        ast = AstLoader.load_json_file("testdata/print_function_in_function.json")
        interpreter = Interpreter()

        with StdoutCapture() as capture:
            interpreter.interpret(ast)
        captured_output = capture.get_output()

        self.assertEqual("is lesser\nis lesser\n", captured_output)


if __name__ == '__main__':
    unittest.main()
