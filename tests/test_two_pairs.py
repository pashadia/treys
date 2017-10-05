from treys.hand import Hand
from utils import HandTestCase


class TwoPairTests(HandTestCase):
    _over_to_paired = {
        "cards": ["Qh", "Qs"],
        "board": ["Th", "Td", "3c"]
    }

    _top_two = {
        "cards": ["Ac", "Td"],
        "board": ["As", "3d", "Tc"]
    }

    _top_and_bot = {
        "cards": ["Ac", "5d"],
        "board": ["5c", "Td", "As"]
    }

    _bot_two = {
        "cards": ["4c", "5d"],
        "board": ["5c", "Td", "4s"]
    }

    _under_high = {
        "cards": ["7c", "7d"],
        "board": ["Td", "4s", "Ts"]
    }

    _over_low = {
        "cards": ["7c", "7d"],
        "board": ["4d", "4s", "Ts"]
    }

    _under_paired = {
        "cards": ["7c", "7d"],
        "board": ["Td", "Ts", "Ks"]
    }

    _all_two_pairs = [
        _over_to_paired, _top_two, _top_and_bot, _bot_two,
        _under_high, _over_low, _under_paired
    ]

    _all_non_two_pairs = []
    _all_hands = _all_two_pairs + _all_non_two_pairs

    def test_all_two_pairs(self):
        for hand_dict in self._all_two_pairs:
            hand = Hand(**hand_dict)
            self.assertTrue(hand.is_two_pair())

    def test_overpair_to_paired(self):
        self.standard_check(self._over_to_paired, Hand.has_overpair_to_paired_board)

    def test_top_two_pair(self):
        self.standard_check(self._top_two, Hand.has_top_two_pair)

    def test_top_and_bottom(self):
        self.standard_check(self._top_and_bot, Hand.has_top_and_bottom)

    def test_bottom_two_pair(self):
        self.standard_check(self._bot_two, Hand.has_bottom_two_pair)

    def test_under_high_pair(self):
        self.standard_check(self._under_high, Hand.has_under_high_pair)

    def test_over_low_pair(self):
        self.standard_check(self._over_low, Hand.has_over_low_pair)

    def test_under_pair_to_paired(self):
        self.standard_check(self._under_paired, Hand.has_under_pair_to_paired)
