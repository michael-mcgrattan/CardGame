import unittest, ScabbyQueen

minimumQueen = 1

class ScabbyQueenTest(unittest.TestCase):
    def test_removeQueens(self):
        deck = ScabbyQueen.removeQueens()
        noOfQueen = sum('Q' in s for s in deck)
        self.assertEqual(noOfQueen, minimumQueen)

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
