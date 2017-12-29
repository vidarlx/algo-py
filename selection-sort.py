import unittest

def find_min(lst):
  min = 0
  for index in range(len(lst)):
    if lst[index] < lst[min]:
      min = index
  return min

def selection_sort(lst):
  if (len(lst) == 0):
    raise Exception("Array can not be empty")

  if (len(lst) == 1):
    return lst
  
  result = []
  for i in range(len(lst)):
    min = find_min(lst)
    result.append(lst[min])
    lst.pop(min)
  return result

class TestbinarySearch(unittest.TestCase):
  def test_empty_list(self):
    self.assertRaises(Exception, selection_sort, None)
    self.assertRaises(Exception, selection_sort, [])
  def test_two_elements(self):
    self.assertListEqual(selection_sort([1,2]), [1,2])
    self.assertListEqual(selection_sort([2,1]), [1,2])
  def test_some_elements(self):
    self.assertListEqual(selection_sort([10, 1, 9, 10000, 1]), [1, 1, 9, 10, 10000])
    self.assertListEqual(selection_sort([1, 1, 1, 10000, 1]), [1, 1, 1, 1, 10000])
    
if __name__ == '__main__':
    unittest.main()