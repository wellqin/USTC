import unittest

class Test(unittest.TestCase):
    @unittest.expectedFailure
    def test_never_passes(self):
        self.assertTrue(False)
    @unittest.expectedFailure
    def test_always_passes(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()