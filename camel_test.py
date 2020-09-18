import unittest
from unittest import TestCase
# import the capitalize function in the camale_case module
from camel_case import Camel_case
import camel_case

#create a class that inherits functionality from TestCase Class in the unitTest module
class TestCamelCase(TestCase):
    def test__for_correctValue(self):
        #store the value to be tested in variable
        test_case = "This is my first sentence"
        #store the expected value in a variable
        expected = "thisIsMyFirstSentence"
        self.assertEqual(Camel_case(test_case), expected)
    #this 
    def test_empty_string(self):
        #store the value to be tested in variable
        test_case = ""
        self.assertIsNone(Camel_case(test_case))
    
    def test_with_random_spaces_upper_and_lower_cases(self):
        test_case = "  This  cOnTains MoRe sPaces   aNd miXed uPper loWer caSeS "
        #store the expected value in a variable
        expected = "thisContainsMoreSpacesAndMixedUpperLowerCases"
        self.assertEqual(Camel_case(test_case), expected)

    def test_none_string_values(self):
        test_case = "hel#l!o w?o2r*l/d"
        expected = "helloWorld"
        self.assertEqual(Camel_case(test_case), expected)

    def test_for_numbers_valaues(self):
        test_case = "123"
        expected = ""
        self.assertEqual(camel_case.Remove_noneString_values(test_case), expected)

    def test_when_input_start_with_integer(self):
        test_case = "1 this start with number"
        expected = "thisSartWithNumber"
        self.assertEqual(Camel_case(test_case), expected)

unittest.main()




