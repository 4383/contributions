import datetime
import unittest
import contributions.utils as utils


class NewDatetime(datetime.datetime):
    @classmethod
    def now(cls):
        return cls(2018, 7, 20, 16, 4)

    @classmethod
    def today(cls):
        return cls(2018, 7, 20, 16, 4)


class TestUtils(unittest.TestCase):
    def test_ok(self):
        datetime.datetime = NewDatetime
        self.assertEqual(str(utils.date(0, 50)),
                         str(datetime.datetime(2017, 7, 30, 16, 4)))

        self.assertEqual(str(utils.date(3, 50)),
                         str(datetime.datetime(2017, 8, 2, 16, 4)))
