import unittest
import path_utils

""" 
def test_(self):
    input = 
    expected =
    self.assertEqual(func(input), expected) 
"""

class path_utils_test(unittest.TestCase):

    def test_parse_path(self):
        input = "c slash program files slash riot games"
        expected = "c/program files/riot games"
        self.assertEqual(path_utils.parse_path(input), expected) 

    # def test_get_possible_directory_variations(self):
    #     testcases = ["c: slash test dir slash inner test dir", "c: idk", "c: slash idk"]
        
    #     for case in testcases:
    #         print("Input: " + str(case))
    #         try:
    #             print("Output: " + str(get_valid_path_variations(parse_path(case))))
    #         except ValueError as error:
    #             print("Error raised: " + str(error))


if __name__ == '__main__':
    unittest.main()