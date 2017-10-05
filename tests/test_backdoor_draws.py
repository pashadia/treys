from treys.hand import Hand
from utils import HandTestCase


class BackdoorDrawsTests(HandTestCase):
    _bd_flush_high = {
        "cards": ["Ks", "7d"],
        "board": ["Qs", "Ts", "2c"]
    }

    _bd_flush_low = {
        "cards": ["Kd", "7s"],
        "board": ["Qs", "Ts", "2c"]
    }

    _bd_flush_both = {
        "cards": ["Ks", "7s"],
        "board": ["Qs", "Td", "2c"]
    }

    def test_backdoor_flush_high_card(self):
        hand = Hand(**self._bd_flush_high)
        high, low = hand.has_backdoor_flush()
        self.assertTrue(high)
        self.assertFalse(low)

    def test_backdoor_flush_low_card(self):
        hand = Hand(**self._bd_flush_low)
        high, low = hand.has_backdoor_flush()
        self.assertTrue(low)
        self.assertFalse(high)

    def test_backdoor_flush_both_cards(self):
        hand = Hand(**self._bd_flush_both)
        high, low = hand.has_backdoor_flush()
        self.assertTrue(high)
        self.assertTrue(low)

    def test_backdoor_straight_draw(self):
        pass
