from third_task import RandomList
import unittest


class RandomListUnit(unittest.TestCase):
    def SetUpRandomList(self):
        self.RandomList = RandomList()

    def test_LenCheck(self):
        self.assertEqual(RandomList().length_check(), True)

    def test_length(self):
        self.assertEqual(RandomList.length, 2)

    def test_A_not_B(self):
        self.assertIsNot(RandomList.final[0], RandomList.final[1])


if __name__ == "__main__":
    unittest.main()
    
