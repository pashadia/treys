from deuces import Card

class Flop:
    """Represents a Texas/Omaha Hold'em flop.

    Does not verify uniqueness of the cards or validity.
    """

    _cards = []
    _flop_type = 0


    def __init__(self, cards):
        """Initialize a flop.

        Sorts the internal vector, but does not calculate type.
        """
        assert len(cards) == 3

        if isinstance(cards[0], str):
            self._cards = [Card.new(card_str) for card_str in cards]
        else:
            self._cards = list(cards)

        self._cards.sort()


    def cards():
        doc = "The cards property."

        def fget(self):
            return [Card.int_to_str(card) for card in self._cards]

        def fset(self, value):
            self._cards = [Card.new(card_str) for card_str in value]

        def fdel(self):
            del self._cards
        return locals()
    cards = property(**cards())


    def type():
        doc = """The flop's type.

        Possible flop types:
        1: Trips (XXX)
        2: XXY rainbow,
        3: XXY suited,
        4: XYZ rainbow,
        5: XYZ suited,
        6: XYZ flush
        """

        def fget(self):
            if self._flop_type == 0:
                self._flop_type = self._calculate_flop_type()

            return self._flop_type

        return locals()
    type = property(**type())

    def _ranks(self):
        """Return a list of unique card ranks."""
        return list(set([Card.get_rank_int(card) for card in self._cards]))

    @property
    def suits(self):
        """Return a list of the cards' suits, in order."""
        return [Card.INT_SUIT_TO_CHAR_SUIT[Card.get_suit_int(card)] for card in self._cards]

    @property
    def unique_suits(self):
        """Return the list of unique suits."""
        return list(set(self.suits))

    def _calculate_flop_type(self):
        r = len(self._ranks())
        s = len(self.unique_suits)
        if r == 1:
            return 1
        elif r == 2:
            if s == 3:
                return 2
            elif s == 2:
                return 3
        elif r == 3:
            if s == 3:
                return 4
            elif s == 2:
                return 5
            elif s == 1:
                return 6

        return 0  # This should never happen.
