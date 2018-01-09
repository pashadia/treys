from unittest import \
    TestCase, \
    main
from treys.hand import Hand
from deuces import Card, Evaluator


class HandTests(TestCase):
    """Test the Hand class."""

    _invalid_hands = [
        {"cards": [], "board": []},
        {"cards": [Card.new("Qh"), Card.new("Qs")], "board": []},  # no board
        {
            "cards": [],
            "board": [Card.new("Qh"), Card.new("Qs"), Card.new("Kh")]
        },  # no hand
        {
            "cards": [Card.new("Qh"), Card.new("Qs")],
            "board": [Card.new("Qh"), Card.new("2s"), Card.new("3s")]
        },  # duplicate card
        {
            "cards": [Card.new("Qh"), Card.new("Qs"), Card.new("Kh")],
            "board": [Card.new("Qd"), Card.new("2s"), Card.new("3s")]
        },  # too many cards in the hand
        {
            "cards": [Card.new("Qh"), Card.new("Qs")],
            "board": [
                Card.new("Qd"), Card.new("2s"),
                Card.new("3s"), Card.new("Kh"),
                Card.new("5s"), Card.new("As")
            ]
        },  # too many cards on the board
        {
            "cards": [Card.new("Qh"), Card.new("Qs"), Card.new("Kh")],
            "board": [Card.new("Qd"), Card.new("2s")]
        },  # too many cards in the hand and too few on the board
        {
            "cards": [Card.new("Qh"), Card.new("Qs")],
            "board": [Card.new("4c"), Card.new("2s")]
        },  # too few cards on the board
    ]

    _royal = {
        "cards": [Card.new("Ts"), Card.new("Js")],
        "board": [Card.new("Qs"), Card.new("Ks"), Card.new("As")]
    }

    def setUp(self):
        self.ev = Evaluator()

    def test_init_invalid_values(self):
        for hand_dict in self._invalid_hands:
            hand_dict["evaluator"] = self.ev
            self.assertRaises(
                AssertionError,
                Hand.__init__, None, **hand_dict)

    def test_init_without_evaluator(self):
        hand = Hand(**self._royal)
        self.assertEqual(hand.rank_class, 1)

    def test_init_valid_hands(self):
        self._royal["evaluator"] = self.ev
        hand = Hand(**self._royal)
        self.assertEqual(hand.rank_class, 1)

    def test_pocket_pair(self):
        pair = Hand(["Ts", "Td"], ["2d", "3c", "5h"], self.ev)
        self.assertTrue(pair.pair_in_hand())
        no_pair = Hand(["5d", "6d"], ["2d", "3c", "5h"], self.ev)
        self.assertFalse(no_pair.pair_in_hand())

    def test_paired_board(self):
        paired = Hand(["Ts", "Td"], ["As", "Ad", "3c"])
        self.assertTrue(paired.paired_board())
        not_paired = Hand(["Ts", "Td"], ["As", "Kd", "3c"])
        self.assertFalse(not_paired.paired_board())

    def test_suited_hands(self):
        suited = Hand(["As", "Ks"], ["2d", "3c", "5h"], self.ev)
        self.assertTrue(suited.hand_is_suited())
        not_suited = Hand(["As", "Kd"], ["2d", "3c", "5h"], self.ev)
        self.assertFalse(not_suited.hand_is_suited())

if __name__ == "__main__":
    main()
