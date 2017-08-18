#!/usr/local/bin/python3
import unittest
import io
import sys
import time
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
        self.assertEqual(self.aTimer.getTimerSecs(), 0)

    def test_timer_setting_seconds_ver(self):
        self.aTimer.setTimerSecs(100)
        self.assertEqual(self.aTimer.getTimerSecs(), 100)

    def test_timer_setting_min_secs_ver(self):
        self.aTimer.setTimerMinSecs(1, 40)
        self.assertEqual(self.aTimer.getTimerSecs(), 100)

    def test_timer_print_format_01(self):
        self.aTimer.setTimerSecs(190)
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
        self.aTimer.setTimerMinSecs(5, 30)
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
        self.aTimer.setTimerSecs(20)
        start = time.time()
        self.aTimer.countdown()
        end = time.time()
        timeElapsed = end - start
        self.assertEqual(self.aTimer.getTimerSecs(), int(timeElapsed))



    
if __name__ == "__main__":
    unittest.main()
