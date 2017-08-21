#!/usr/local/bin/python3
import unittest
import io
import sys
import time
from countdown_timer import CountdownTimer


class TimerTestCase(unittest.TestCase):

    def setUp(self):
        self.aTimer = CountdownTimer()
        self.start = time.time()

    def tearDown(self):
        t = time.time() - self.start
        print("%s: %.3f" % (self.id(), t))

    def test_default_current_time(self):
        self.assertEqual(self.aTimer.get_timer_secs(), 0)

    def test_timer_setting_seconds_ver(self):
        self.aTimer.set_timer_secs(100)
        self.assertEqual(self.aTimer.get_timer_secs(), 100)

    def test_timer_setting_min_secs_ver(self):
        self.aTimer.set_timer_min_secs(1, 40)
        self.assertEqual(self.aTimer.get_timer_secs(), 100)

    def test_timer_print_format_01(self):
        self.aTimer.set_timer_secs(190)
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            print(self.aTimer)
            output = out.getvalue().strip()
            self.assertEqual(output, "03:10")
        finally:
            sys.stdout = saved_stdout

    def test_timer_print_format_02(self):
        self.aTimer.set_timer_min_secs(5, 30)
        saved_stdout = sys.stdout
        try:
            out = io.StringIO()
            sys.stdout = out
            print(self.aTimer)
            output = out.getvalue().strip()
            self.assertEqual(output, "05:30")
        finally:
            sys.stdout = saved_stdout

    def test_timer_countdown(self):
        self.aTimer.set_timer_secs(10)
        start = time.time()
        self.aTimer.countdown()
        end = time.time()
        time_elapsed = end - start
        self.assertEqual(self.aTimer.get_timer_secs(), int(time_elapsed))

    def test_check_max_time_01(self):
        return_value = self.aTimer.set_timer_min_secs(1, 30)
        self.assertTrue(return_value)

    def test_check_max_time_02(self):
        return_value = self.aTimer.set_timer_secs(6001)
        self.assertFalse(return_value)

    def test_check_timer_value(self):
        return_value = self.aTimer.countdown()
        self.assertFalse(return_value)


if __name__ == "__main__":
    unittest.main()
