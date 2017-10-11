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

    _bd_flush_high_card_pair1 = {
        "cards": ["As", "Ad"],
        "board": ["9s", "3s", "7d"]
    }

    _bd_flush_high_card_pair2 = {
        "cards": ["Ad", "As"],
        "board": ["9s", "3s", "7d"]
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

    def test_backdoor_flush_pair_in_hand(self):
        # Border case where there's a pair in hand.
        hand1 = Hand(**self._bd_flush_high_card_pair1)
        hand2 = Hand(**self._bd_flush_high_card_pair2)
        high1, low1 = hand1.has_backdoor_flush()
        high2, low2 = hand2.has_backdoor_flush()
        self.assertTrue(high1)
        self.assertFalse(low1)
        self.assertTrue(high2)
        self.assertFalse(low2)


    def test_backdoor_straight_draw(self):
        pass
