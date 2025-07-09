import unittest
import bankaccount as bc


class TestHello(unittest.TestCase):
    def test_deposit(self):
        bac = bc.Bankaccount(0, "Viktor", 100)
        self.assertEqual(bac.deposit(100), 100)
        # bac2 = bc.Bankaccount(0, "Viktor", 100)
        # self.assertEqual(bac2.deposit(0), 100)

    def test_withdraw(self):
        bac = bc.Bankaccount(100, "Viktor", 100)
        self.assertEqual(bac.withdraw(100), 0)
        # bac2 = bc.Bankaccount(100, "Viktor", 100)
        # self.assertEqual(bac2.withdraw(0), 0)


if __name__ == "__main__":
    unittest.main()
