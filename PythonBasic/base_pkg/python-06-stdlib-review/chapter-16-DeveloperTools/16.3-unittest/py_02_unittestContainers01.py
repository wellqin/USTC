import unittest, textwrap

class ContainerEqualityTest(unittest.TestCase):
    def testCount(self):
        self.assertCountEqual(
            [1, 2, 3, 2],
            [1, 3, 2, 3],
        )
    
    def testDict(self):
        self.assertDictEqual(
            {'a': 1, 'b': 2},
            {'a': 1, 'b': 3},
        )
    
    def testList(self):
        self.assertListEqual(
            [1, 2, 3, 4],
            [1, 2, 3, 5],
        )
    
    def testTuple(self):
        self.assertTupleEqual(
            (1,),
            (2,),
        )
    def testSet(self):
        self.assertSetEqual(
            {1, 3, 5},
            {1, 3, 7},
        )

    def testMultiLineString(self):
        self.assertMultiLineEqual(
            textwrap.dedent("""
            this string
            has more than one
            line.
            """),
            textwrap.dedent("""
            this string has 
            more than two
            lines.
            """),
        )
    
    def testSequence(self):
        self.assertSequenceEqual(
            [1, 2, 3],
            [1, 3, 2],
        )

if __name__ == "__main__":
    unittest.main()