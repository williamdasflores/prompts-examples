import unittest
from longest_str import find_longest_string

class TestFindLongestString(unittest.TestCase):
     # Test standard case with clear longest string
    def test_standard_case_with_clear_longest(self):
        result = find_longest_string(["cat", "dog", "elephant"])
        self.assertEqual(result, "elephant")
    
    # Test empty list returns None
    def test_empty_list_returns_none(self):
        result = find_longest_string([])
        self.assertIsNone(result)
    
    # Test tie-breaking behavior - returns first longest string when there's a tie
    def test_tie_breaking_returns_first_longest(self):
        result = find_longest_string(["hello", "world", "python"])
        self.assertEqual(result, "hello")
    
    # Test TypeError is raised when non-string element is in list
    def test_raises_type_error_for_non_string(self):
        with self.assertRaises(TypeError):
            find_longest_string(["hello", 123, "world"])


if __name__ == "__main__":
    unittest.main()