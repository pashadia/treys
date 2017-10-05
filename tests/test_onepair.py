from treys.hand import Hand
from utils import HandTestCase


class OnePairTests(HandTestCase):
    _over = {
        "cards": ["Qh", "Qs"],
        "board": ["2s", "3c", "8d"]
    }

    _tptk = {
        "cards": ["As", "Kh"],
        "board": ["Kd", "Tc", "2c"]
    }

    _tptk_paired = {
        "cards": ["As", "Kh"],
        "board": ["Kd", "Tc", "Ts"]
    }

    _top = {
        "cards": ["3s", "Kh"],
        "board": ["Kd", "Tc", "2c"]
    }

    _under_top = {
        "cards": ["Js", "Jh"],
        "board": ["Kd", "Tc", "2c"]
    }

    _mptk = {
        "cards": ["As", "Th"],
        "board": ["Kd", "Tc", "2c"]
    }

    _under_middle = {
        "cards": ["8s", "8h"],
        "board": ["Kd", "Tc", "2c"]
    }

    _bot = {
        "cards": ["3s", "2h"],
        "board": ["Kd", "Tc", "2c"]
    }

    _under = {
        "cards": ["2s", "2h"],
        "board": ["Kd", "Tc", "3c"]
    }

    _all_pairs = [_over, _tptk, _top, _under_top, _mptk, _under_middle, _bot, _under]

    _all_non_pairs = [_tptk_paired]

    _all_hands = _all_pairs + _all_non_pairs

    def test_all_pairs(self):
        for hand_dict in self._all_pairs:
            hand = Hand(**hand_dict)
            self.assertTrue(hand.is_one_pair())

    def test_over_pair(self):
        self.standard_check(self._over, Hand.has_overpair)

    def test_top_pair(self):
        for hand_dict in (self._tptk, self._top):
            hand = Hand(**hand_dict)
            self.assertTrue(hand.has_top_pair())

    def test_under_top(self):
        self.standard_check(self._under_top, Hand.has_under_top_pair)

    def test_middle_pair(self):
        self.standard_check(self._mptk, Hand.has_middle_pair)

    def test_under_middle_pair(self):
        self.standard_check(self._under_middle, Hand.has_under_middle_pair)

    def test_bottom_pair(self):
        self.standard_check(self._bot, Hand.has_bottom_pair)

    def test_under_pair(self):
        self.standard_check(self._under, Hand.has_under_pair)
