from treys.hand import Hand
from utils import HandTestCase


class HighcardsTests(HandTestCase):
    _overcards = {
        "cards": ["As", "Kd"],
        "board": ["Td", "3s", "2c"]
    }

    _one_over = {
        "cards": ["As", "9d"],
        "board": ["Td", "3s", "2c"]
    }

    _all_hands = [_overcards, _one_over]

    def test_two_overcards(self):
        self.standard_check(self._overcards, Hand.has_two_overcards)

    def test_one_overcard(self):
        self.standard_check(self._one_over, Hand.has_one_over)
