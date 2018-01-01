import unittest
import time
import random

def quick_sort(arr):
  if len(arr) < 2:
    return arr

  pivot = arr[0]
  less = [i for i in arr[1:] if i <= pivot]
  greater = [i for i in arr[1:] if i > pivot]
      
  return quick_sort(less) + [pivot] + quick_sort(greater)

class TestQuickSort(unittest.TestCase):
  def setUp(self):
      self.startTime = time.time()

  def tearDown(self):
    t = time.time() - self.startTime
    print "%s: %.3f" % (self.id(), t)
        
  def test_two_elements(self):
    self.assertListEqual(quick_sort([1,2]), [1,2])
    self.assertListEqual(quick_sort([2,1]), [1,2])
  def test_some_elements(self):
    self.assertListEqual(quick_sort([10, 1, 9, 10000, 1]), [1, 1, 9, 10, 10000])
    self.assertListEqual(quick_sort([1, 1, 1, 10000, 1]), [1, 1, 1, 1, 10000])
  def test_random_elements(self):
    rand = [random.randint(0,10000) for r in xrange(1000)]
    s = sorted(rand)
    self.assertListEqual(quick_sort(rand), s)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuickSort)
    unittest.TextTestRunner(verbosity=0).run(suite)
