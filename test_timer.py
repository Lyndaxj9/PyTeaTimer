#!/usr/local/bin/python3
import unittest
import io
import sys
from countdown_timer import CountdownTimer

class TimerTestCase(unittest.TestCase):
    def setUp(self):
        self.aTimer = CountdownTimer()

    def test_print_correct_name(self):
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            self.aTimer.printClassName()
            output = out.getvalue().strip()
            self.assertEqual(output, "CountdownTimer")
        finally:
            sys.stdout = saved_stdout

    def test_default_current_time(self):
        self.assertEqual(self.aTimer.getCurrentTime(), 0)

if __name__ == "__main__":
    unittest.main()
