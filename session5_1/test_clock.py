import unittest
from clock import ClockIterator

class TestClockIterator(unittest.TestCase):
    """
    Test the ClockIterator class
    """

    def _test_print(self, order):
        clock = ClockIterator()
        iter(clock)
        a = None
        for i in range(order):
            a = clock.__next__()

        return a

    def test_print(self):
        # test The first thing returned from a ClockIterator should be the string "00:00".
        self.assertEqual(self._test_print(1), "00:00")
        # The 60th thing returned from a ClockIterator should be the string "00:59".
        self.assertEqual(self._test_print(60), "00:59")
        # The 61st thing returned from a ClockIterator should be the string "01:00".
        self.assertEqual(self._test_print(61), "01:00")
        # The 1440th thing returned from a ClockIterator should be the string "23:59".
        self.assertEqual(self._test_print(1440), "23:59")
        # The 1441st thing returned from a ClockIterator should be the string "00:00".
        self.assertEqual(self._test_print(1441), "00:00")

if __name__ == '__main__':
    unittest.main()
