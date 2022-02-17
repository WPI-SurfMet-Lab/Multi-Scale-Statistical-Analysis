import unittest
import multiscale_modules.utils.read_data as rd


class TestReadData(unittest.TestCase):
    def testAreaScaleTestData(self):
        data = rd.read_data("samples/area-scale-test-data.txt")

        # Validate that the first row and column have correct data
        self.assertAlmostEqual(data['scale of analysis'][0], 0.357075, 3)
        # Validate that the last row and column have correct data
        self.assertAlmostEqual(data['r2'][49], 0.432761, 3)


if __name__ == '__main__':
    unittest.main()
