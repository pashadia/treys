from unittest import TestCase
from treys import Hand


class HandTestCase(TestCase):
    def check_others(self, good_dict, fn):
        for hand_dict in [hand for hand in self._all_hands if hand is not good_dict]:
            hand = Hand(**hand_dict)
            self.assertFalse(fn(hand))

    def standard_check(self, good_dict, good_func):
        hand = Hand(**good_dict)
        self.assertTrue(good_func(hand))
        self.check_others(good_dict, good_func)
