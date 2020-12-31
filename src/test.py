import unittest
from constants import Constants
from path_utils import *
from shutil import rmtree
from collections import Counter


class PathUtilsTest(unittest.TestCase):

    def test_parse_path(self):
        actual = parse_path("c: {0} program files {0} riot games".format(Constants.SEPARATOR_WORD))
        expected = "c:{0}program files{0}riot games".format(Constants.SEPARATOR_CHAR)
        self.assertEqual(actual, expected)

    def test_get_valid_path_variations(self):
        # Create test directories
        test_path_1 = Constants.PROJECT_DIRECTORY + "/testdirectory/test_dir/inner_test_dir"
        test_path_2 = Constants.PROJECT_DIRECTORY + "/testdirectory/testdir/innertestdir"
        os.makedirs(test_path_1)
        os.makedirs(test_path_2)

        actual = get_valid_path_variations(Constants.PROJECT_DIRECTORY + "/testdirectory/test dir/inner test dir")
        expected = [test_path_1, test_path_2]

        self.assertEqual(Counter(actual), Counter(expected))  # compares contents of two lists ignoring order

        # Remove test directories
        rmtree(Constants.PROJECT_DIRECTORY + "/testdirectory/")

    def test_get_valid_path_variations_non_str_input(self):
        self.assertRaises(ValueError, get_valid_path_variations, 5)

    def test_get_valid_path_variations_empty_str_input(self):
        self.assertRaises(ValueError, get_valid_path_variations, "")


if __name__ == "__main__":
    unittest.main()
