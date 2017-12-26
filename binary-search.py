import unittest

def binary_search(values, search, x = 0, y = 0):
    if len(values) == 0:
        raise Exception("Empty array")

    if (y == 0):
        y = len(values)-1

    mid = (x + y) / 2
    print "Mid {}".format(mid)

    if search == values[mid]:
        print "Equal"
        return mid

    if search < values[mid]:
        print "Lower, next: {}:{}".format(x, mid)
        return binary_search(values, search, x, mid)

    if search > values[mid]:
        print "Higher, next: {}:{}".format(mid, y)
        return binary_search(values, search, mid+1, y)

class TestbinarySearch(unittest.TestCase):
    def test_empty_array(self):
        self.assertRaises(Exception, binary_search, [[], 1])
    def test_one_element(self):
        self.assertEqual(binary_search([1], 1), 0)
    def test_two_elements(self):
        self.assertEqual(binary_search([1,5], 1), 0)
        self.assertEqual(binary_search([1,5], 5), 1)
    def test_multiple_elements(self):
        self.assertEqual(binary_search([0, 1, 12, 15, 18, 21, 25], 0), 0)
        self.assertEqual(binary_search([0, 1, 12, 15, 18, 21, 25], 15), 3)
        self.assertEqual(binary_search([0, 1, 12, 15, 18, 21, 25], 25), 6)

if __name__ == '__main__':
    unittest.main()
