"""
Includes tests for fishnchips module.
"""


# python setup.py test

from unittest import TestCase

import fishnchips


class TestFishNChips(TestCase):
    """
    Tests the class.
    """
    def test_say_the_word(self):
        """
        Tests the say_the_word() method.
        """
        expected = " Chips"
        actual = fishnchips.say_the_word()
        self.assertEqual(expected, actual)
