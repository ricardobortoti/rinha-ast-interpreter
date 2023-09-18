from unittest import TestCase

from app.callstack.stack import Stack


class TestStack(TestCase):
    def test_is_empty(self):
        stack = Stack()
        self.assertEqual(stack.is_empty(), True)

    def test_push(self):
        stack = Stack()
        item = {'a': 1, 'b': 2}
        stack.push(item)
        self.assertDictEqual(stack.peek(), item)

    def test_pop(self):
        stack = Stack()
        first_item = {'a': 1, 'b': 2}
        second_item = {'a': 2, 'b': 1}
        stack.push(first_item)
        stack.push(second_item)
        self.assertDictEqual(stack.pop(), second_item)
        self.assertDictEqual(stack.peek(), first_item)

    def test_peek(self):
        stack = Stack()
        first_item = {'a': 1, 'b': 2}
        stack.push(first_item)
        self.assertDictEqual(stack.peek(), first_item)

    def test_size(self):
        stack = Stack()
        first_item = {'a': 1, 'b': 2}
        second_item = {'a': 2, 'b': 1}
        stack.push(first_item)
        stack.push(second_item)
        self.assertEqual(stack.size(), 2)

    def test_set_and_get(self):
        stack = Stack()
        expected_a = 2
        stack['variable'] = expected_a
        self.assertEqual(stack['variable'], expected_a)

