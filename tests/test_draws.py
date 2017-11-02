from treys.hand import Hand
from utils import HandTestCase


class DrawsTests(HandTestCase):
    _sf = {
        "cards": ["7s", "5s"],
        "board": ["Ac", "8s", "6s"]
    }

    _gsf = {
        "cards": ["7s", "5s"],
        "board": ["Ac", "8s", "4s"]
    }

    _flush = {
        "cards": ["7s", "5s"],
        "board": ["Ac", "As", "6s"]
    }

    _flush_high_card = {
        "cards": ["As", "9d"],
        "board": ["9s", "3s", "7s"]  # they didn't have to pair
    }

    _flush_low_card = {
        "cards": ["Ks", "Ad"],
        "board": ["9s", "3s", "7s"]
    }

    _flush_high_card_pair1 = {
        "cards": ["As", "Ad"],
        "board": ["9s", "3s", "7s"]
    }

    _flush_high_card_pair2 = {
        "cards": ["Ad", "As"],
        "board": ["9s", "3s", "7s"]
    }

    _straight = {
        "cards": ["7s", "5s"],
        "board": ["Ac", "8d", "6s"]
    }

    _gut_straight = {
        "cards": ["9c", "8d"],
        "board": ["7d", "5c", "2s"]
    }

    _made_flush = {
        "cards": ["Ac", "3c"],
        "board": ["Kc", "Tc", "2c"]
    }

    # _all_hands doesn't include _sf and _gsf because they also draw to flushes and straights.
    _all_hands = [_flush, _straight, _gut_straight]

    def test_straight_flush_draw(self):
        self.standard_check(self._sf, Hand.has_straight_flush_draw)

    def test_gutshot_straight_flush_draw(self):
        self.standard_check(self._gsf, Hand.has_gutshot_straight_flush_draw)

    def test_flush_draw_high_card(self):
        hand = Hand(**self._flush_high_card)
        high, low = hand.has_flush_draw()
        self.assertTrue(high)
        self.assertFalse(low)

    def test_flush_pair_in_hand(self):
        # Border case where there's a pair in hand.
        hand1 = Hand(**self._flush_high_card_pair1)
        hand2 = Hand(**self._flush_high_card_pair2)
        high1, low1 = hand1.has_flush_draw()
        high2, low2 = hand2.has_flush_draw()
        self.assertTrue(high1)
        self.assertFalse(low1)
        self.assertTrue(high2)
        self.assertFalse(low2)

    def test_flush_draw_low_card(self):
        hand = Hand(**self._flush_low_card)
        high, low = hand.has_flush_draw()
        self.assertTrue(low)
        self.assertFalse(high)

    def test_flush_draw_both_cards(self):
        hand = Hand(**self._flush)
        high, low = hand.has_flush_draw()
        self.assertTrue(high)
        self.assertTrue(low)

    def test_straight_draw(self):
        self.standard_check(self._straight, Hand.has_straight_draw)

    def test_gutshot_straight_draw(self):
        self.standard_check(self._gut_straight, Hand.has_gutshot_straight_draw)

    def test_made_flush_doesnt_draw(self):
        hand = Hand(**self._made_flush)
        high, low = hand.has_flush_draw()
        self.assertFalse(high)
        self.assertFalse(low)
