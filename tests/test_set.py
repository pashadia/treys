from treys.hand import Hand
from utils import HandTestCase


class SetTests(HandTestCase):
    _top_set = {
        "cards": ["Ts", "Td"],
        "board": ["Tc", "4d", "3h"]
    }

    _middle_set = {
        "cards": ["Ts", "Td"],
        "board": ["Tc", "4d", "Ah"]
    }

    _bottom_set = {
        "cards": ["Ts", "Td"],
        "board": ["Tc", "Ad", "Qh"]
    }

    _overfull = {
        "cards": ["Ts", "Td"],
        "board": ["Tc", "4d", "4h"]
    }

    _all_sets = [_top_set, _middle_set, _bottom_set]
    _all_non_sets = [_overfull]
    _all_hands = _all_sets + _all_non_sets

    def test_all_sets(self):
        for hand_dict in self._all_sets:
            hand = Hand(**hand_dict)
            self.assertTrue(hand.is_set())

    def test_top_set(self):
        self.standard_check(self._top_set, Hand.has_top_set)

    def test_middle_set(self):
        self.standard_check(self._middle_set, Hand.has_middle_set)

    def test_bottom_set(self):
        self.standard_check(self._bottom_set, Hand.has_bottom_set)
