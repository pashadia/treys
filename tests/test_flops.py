from unittest import \
	TestCase, \
	main

from treys.flop import Flop
from deuces import Card


class FlopTests(TestCase):
    """Test the Flop class."""

    _base_hand = [Card.new("Qh"), Card.new("Qs"), Card.new("Kh")]

    _type_1_flop = [Card.new("Qh"), Card.new("Qs"), Card.new("Qd")]

    _xyz_r = ["Ks", "Ad", "5c"]

    _flush = ["2h", "3h", "4h"]


    def test_init(self):
        flop = Flop(self._base_hand)


    def test_type(self):
        t1 = Flop(self._type_1_flop)
        assert t1.type == 1

        t3 = Flop(self._base_hand)
        assert t3.type == 3

        t4 = Flop(self._xyz_r)
        assert t4.type == 4

        t6 = Flop(self._flush)
        assert t6.type == 6


    def test_ranks(self):
        t1 = Flop(self._type_1_flop)
        assert len(t1._ranks()) == 1
        t3 = Flop(self._base_hand)
        assert len(t3._ranks()) == 2


    def test_suits(self):
        t1 = Flop(self._type_1_flop)
        assert len(t1.unique_suits) == 3
        t3 = Flop(self._base_hand)
        assert len(t3.unique_suits) == 2
        assert t3.suits == ["s", "h", "h"]

        xyzr = Flop(self._xyz_r)
        assert xyzr.suits == ["c", "s", "d"]
