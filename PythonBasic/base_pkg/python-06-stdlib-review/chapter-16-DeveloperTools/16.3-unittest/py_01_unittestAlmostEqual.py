import unittest

class AlmostEqualTest(unittest.TestCase):
    def testEqual(self):
        self.assertEqual(1.1, 3.3-2.2)
    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3-2.2, places=1)
    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 3.3-2.0, places=1)

if __name__ == "__main__":
    unittest.main()