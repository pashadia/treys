from unittest import \
    TestCase, \
    main

from treys.hand import Hand
from deuces import Card, Evaluator

class TransformCase(TestCase):
    """Test the hand transformations to HDSC suits."""

    _royal = {
        "cards": [Card.new("Ts"), Card.new("Js")],
        "board": [Card.new("Qs"), Card.new("Ks"), Card.new("As")]
    }


    _royal_transformed = {
        "cards": ["Th", "Jh"],
    }

    _line2 = {
        "cards": ["Qc", "Qs"],
        "board": ["2c", "3c", "8c"]
    }

    _line2_transform = {
        "cards": ["Qh", "Qc"],
        "board": ["2c", "3c", "8c"]
    }

    _line6 = {
        "cards": ["2d", "Qd"],
        "board": ["2c", "3d", "8h"]
    }

    _line6_transform = {
        "cards": ["2s", "Qs"],
        "board": ["2c", "3d", "8h"]
    }


    _line10 = {
        "cards": ["Qs", "Qd"],
        "board": ["2c", "2d", "8d"]
    }

    _line10_transform = {
        "cards": ["Qh", "Qc"],
        "board": ["2c", "2d", "8d"]
    }

    _line9 = {
        "cards": ["Qs", "8s"],
        "board": ["2c", "2s", "8d"]
    }

    _line9_transform = {
        "cards": ["8h", "Qh"],
    }


    _line16 = {
        "cards": ["2s", "2d"],
        "board": ["2c", "4d", "8d"]
    }

    _line16_transform = {
        "cards": ["2h", "2c"],
    }

    _line24 = {
        "cards": ["As", "Qd"],
        "board": ["2c", "2h", "8d"]
    }

    _line24_transform = {
        "cards": ["Qc", "As"],
        "board": ["2c", "2h", "8d"]
    }

    _default= {
        "cards": ["As", "Qd"],
        "board": ["Ac", "Qh", "8d"]
    }

    _default_transform = {
        "cards": ["Qc", "As"],
    }

    _hands = [_line2, _line6, _line10, _line9, _line16, _line24, _default]
    _hands_transformed = [_line2_transform, _line6_transform, _line10_transform, _line9_transform, _line16_transform, _line24_transform, _default_transform]


    def setUp(self):
        self.ev = Evaluator()

    def test_basic(self):
        hand = Hand(**self._royal)
        transformed = hand.to_hdsc()

        self.assertEqual(transformed, self._royal_transformed["cards"])

    def test_line_2(self):
        hand = Hand(**self._line2)
        self.assertEqual(hand.to_hdsc(), self._line2_transform["cards"])


    def test_transforms(self):
        for (hand_dict, transf_dict) in zip(self._hands, self._hands_transformed):
            hand = Hand(**hand_dict)
            should_be = transf_dict["cards"]

            print(hand)
            print(should_be)

            self.assertEqual(hand.to_hdsc(), should_be)
