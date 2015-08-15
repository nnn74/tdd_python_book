
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently tries to submit
        # an empty list item. She hits Enter on the empty inout box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She trie again with som text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # She receives a similair warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')

if __name__=='__main__':
    unittest.main()#warnings='ignore')


