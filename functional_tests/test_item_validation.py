import unittest
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    @skip
    def test_cannot_add_empty_list_items(self):
        self.fail('write me! >_<')


if __name__ == '__main__':
    unittest.main()