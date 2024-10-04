import unittest
import sys

class SkippingTest(unittest.TestCase):
    @unittest.skip('always skipped')
    def test(self):
        self.assertTrue(False)
    
    @unittest.skipIf(sys.version_info[0] > 2, 'only runs on python2')
    def test_python2_only(self):
        self.assertTrue(False)
    
    @unittest.skipUnless(sys.platform == 'Darwin', 'only runs on macos')
    def test_macos_only(self):
        self.assertTrue(True)
    
    def test_raise_skiptest(self):
        raise unittest.SkipTest('skipping via exception')


if __name__ == "__main__":
    unittest.main()