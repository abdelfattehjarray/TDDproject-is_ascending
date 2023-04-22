def is_ascending(lst):
    """
    Returns True if the input list is sorted in ascending order, and False otherwise.
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

import unittest
from unittest.mock import patch, Mock

class TestIsAscending(unittest.TestCase):
    
    def test_is_ascending_with_patch(self):
        with patch('__main__.is_ascending', return_value=True) as mock_is_ascending:
            result = is_ascending([1, 2, 3, 4])
            self.assertTrue(result)
            mock_is_ascending.assert_called_once_with([1, 2, 3, 4])
    
    def test_is_ascending_with_return_value(self):
        with patch('__main__.is_ascending', Mock(return_value=False)) as mock_is_ascending:
            result1 = is_ascending([4, 3, 2, 1])
            result2 = is_ascending([1, 2, 3, 4])
            self.assertFalse(result1)
            self.assertFalse(result2)
            mock_is_ascending.assert_any_call([4, 3, 2, 1])
            mock_is_ascending.assert_any_call([1, 2, 3, 4])
    
    def test_is_ascending_with_side_effect(self):
        def mock_side_effect(lst):
            if 3 in lst:
                raise ValueError('List contains 3')
            return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
        
        with patch('__main__.is_ascending', Mock(side_effect=mock_side_effect)) as mock_is_ascending:
            with self.assertRaises(ValueError):
                is_ascending([1, 2, 3])
            result = is_ascending([1, 2, 4])
            self.assertTrue(result)
            mock_is_ascending.assert_any_call([1, 2, 3])
            mock_is_ascending.assert_any_call([1, 2, 4])
            
if __name__ == '__main__':
    unittest.main()
