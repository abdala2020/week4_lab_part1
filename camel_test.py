import unittest
from unittest import TestCase
# import the capitalize function in the camale_case module
from camel_case import capitalize
import camel_case

#create a class that inherits functionality from TestCase Class in the unitTest module
class TestCapitalizeWords(TestCase):
    def test_correctValue(self):
        #store the value to be tested in variable
        test_case = "This is my first sentence"
        #store the expected value in a variable
        expected = "thisIsMyFirstSentence"
        self.assertEqual(capitalize(test_case), expected)
    #this 
    def test_empty_string(self):
        #store the value to be tested in variable
        test_case = ""
        self.assertIsNone(capitalize(test_case))
    
    def test_with_random_spaces_upper_lower_cases(self):
        test_case = "  This  cOnTains MoRe sPaces   aNd miXed uPper loWer caSeS "
        #store the expected value in a variable
        expected = "thisContainsMoreSpacesAndMixedUpperLowerCases"
        self.assertEqual(capitalize(test_case), expected)

    def test_none_string_values(self):
        test_case = "hel#l!o w?o2r*l/d"
        expected = "helloworld"
        self.assertEqual(camel_case.validator(test_case), expected)
        
    def test_for_numbers(self):
        test_case = "123"
        expected = ""
        self.assertEqual(camel_case.validator(test_case), expected)

unittest.main()




