import unittest

from python.collections import priority_queue


class PriorityQueueTests(unittest.TestCase):
    implements = [
        'list',
        'ordered_list',
        'heap',
    ]

    def test_pop(self):
        data = [2, 7, 5, 4, 2, 1]
        expected = [1, 2, 2, 4, 5, 7]

        for impl in self.implements:
            with self.subTest(impl=impl):
                queue = priority_queue(impl)
                for d in data:
                    queue.push(d)
                actual = []
                while len(queue) > 0:
                    actual.append(queue.pop())

                self.assertListEqual(expected, actual)

    def test_pop_with_desc(self):
        data = [2, 7, 5, 4, 2, 1]
        expected = [7, 5, 4, 2, 2, 1]

        for impl in self.implements:
            with self.subTest(impl=impl):
                queue = priority_queue(impl=impl, asc=False)
                for d in data:
                    queue.push(d)
                actual = []
                while len(queue) > 0:
                    actual.append(queue.pop())

                self.assertListEqual(expected, actual)

    def test_top(self):
        data = [2, 7, 5, 4, 2, 1]
        expected = 1

        for impl in self.implements:
            with self.subTest(impl=impl):
                queue = priority_queue(impl)
                for d in data:
                    queue.push(d)

                self.assertEqual(expected, queue.top())
                self.assertEqual(expected, queue.top())
                self.assertEqual(expected, queue.top())

    def test_top_with_desc(self):
        data = [2, 7, 5, 4, 2, 1]
        expected = 7

        for impl in self.implements:
            with self.subTest(impl=impl):
                queue = priority_queue(impl=impl, asc=False)
                for d in data:
                    queue.push(d)

                self.assertEqual(expected, queue.top())
                self.assertEqual(expected, queue.top())
                self.assertEqual(expected, queue.top())
