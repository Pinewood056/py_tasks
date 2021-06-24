import unittest
from fifth_task import DateTask


class TestDate(unittest.TestCase):

    def setUpDateTask(self):
        self.DateTask = DateTask()

    def test_date_exist(self):
        self.assertEqual(DateTask(28, 2, 1994).check(), True)
        self.assertEqual(DateTask(29, 2, 2020).check(), True)
        self.assertEqual(DateTask(1, 12, 2032).check(), True)

    def test_date_not_exist(self):
        self.assertEqual(DateTask(32, 12, 2000).check(), False)
        self.assertEqual(DateTask(11, 13, 2001).check(), False)
        self.assertEqual(DateTask(29, 2, 2021).check(), False)


if __name__ == "__main__":
    unittest.main()
