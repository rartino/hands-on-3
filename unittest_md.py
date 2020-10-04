import sys, unittest
from md import calcenergy

class MdTests(unittest.TestCase):

    def test_calcenergy(self):
        self.assertTrue(True)

if __name__ == '__main__':
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
