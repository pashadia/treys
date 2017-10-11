"""Contains the Hand class definition."""

from deuces import Card, Deck, Evaluator


class Hand:
    """
    Represent a Texas Hold'em hand.

    Two cards in the hand, and 3, 4 or 5 cards on the board are expected.

    Checks for validity and allows for various hand strength checks.

    """

    cards = []
    rank = 0

    def __init__(self, cards, board, evaluator=None):
        """Initialize new poker hand from a card array and an evaluator."""
        assert len(cards) == 2
        assert len(board) in [3, 4, 5]

        # checking there are 5, 6 or 7 unique cards
        cardset = set(cards + board)
        assert len(cardset) == len(cards) + len(board)

        if isinstance(cards[0], str):
            self.cards = [Card.new(card_str) for card_str in cards]
        else:
            self.cards = cards

        if isinstance(board[0], str):
            self.board = [Card.new(card_str) for card_str in board]
        else:
            self.board = board

        if evaluator:
            self.ev = evaluator
        else:
            ev = Evaluator()
            self.ev = ev

        self.rank = self.ev.evaluate(self.cards, self.board)
        self.rank_class = self.ev.get_rank_class(self.rank)

        self._hand_ranks = sorted([Card.get_rank_int(card) for card in self.cards])
        self._board_ranks = sorted([Card.get_rank_int(card) for card in self.board])

    def __str__(self):
        """Provide a pretty looking string representation."""
        s = "%s on %s" % \
            (str(list(map(Card.int_to_pretty_str, self.cards))),
             str(list(map(Card.int_to_pretty_str, self.board))))
        return s

    def pair_in_hand(self):
        """Verify if the hand has a pair."""
        ranks = list(map(Card.get_rank_int, self.cards))
        return ranks[0] == ranks[1]

    def paired_board(self):
        """Verify if the board has paired."""
        ranks = list(map(Card.get_rank_int, self.board))
        return len(set(ranks)) < len(ranks)

    def rest_of_the_deck(self):
        """Return a list with the rest of the cards in the deck."""
        full_deck = Deck.GetFullDeck()
        return [elem
                for elem in full_deck
                if elem not in (self.cards + self.board)]

    # Hand strength checks
    # These are gross hand rank checks.
    # Should be very fast.
    def is_straight_flush(self):
        """Verify if a hand is a straight flush."""
        return self.rank_class is 1

    def is_quads(self):
        """Verify if a hand is a four-of-a-kind."""
        return self.rank_class is 2

    def is_full_house(self):
        """Verify if a hand is a full house."""
        return self.rank_class is 3
    is_fullhouse = is_full_house
    is_boat = is_full_house

    def is_flush(self):
        """Verify if a hand is a flush."""
        return self.rank_class is 4

    def is_straight(self):
        """Verify if a hand is a straight."""
        return self.rank_class is 5

    def is_trips(self):
        """Verify if a hand is a three-of-a-kind."""
        return self.rank_class is 6 and not self.pair_in_hand()

    def is_set(self):
        """Verify is a hand has a set."""
        return self.rank_class is 6 and self.pair_in_hand()

    def is_two_pair(self):
        """Verify if a hand is a two-pair."""
        return self.rank_class is 7

    def is_one_pair(self):
        """Verify if a hand is a one-pair."""
        return self.rank_class is 8

    def is_high_card(self):
        """Verify if a hand is a high-card."""
        return self.rank_class is 9

    # Hand strength checks continue, with finer detail
    def has_overpair(self):
        """Verify if the hand is an overpair to the board."""
        if not self.pair_in_hand():
            return False
        rank = Card.get_rank_int(self.cards[0])
        return all(map(lambda x: rank > x, self._board_ranks))

    def has_overpair_to_paired_board(self):
        """Verify if the hand is overpair to a paired board."""
        return self.has_overpair() and self.paired_board()

    def has_top_pair(self):
        """Verify if the hand has paired the top card on the board."""
        return max(self._board_ranks) in self._hand_ranks and \
            self.is_one_pair()

    def has_under_top_pair(self):
        """Verify if the hand is an underpair to the board's top card."""
        if not self.pair_in_hand() or self.paired_board():
            return False
        rank = self._hand_ranks[0]
        higher_ranks = [x for x in self._board_ranks if x > rank]
        return len(higher_ranks) is 1

    def has_bottom_pair(self):
        """Verify whether I've hit bottom pair."""
        return min(self._board_ranks) in self._hand_ranks and \
            self.is_one_pair()

    def has_middle_pair(self):
        """Verify whether i've hit middle pair.

        Assumes we're on the flop.
        """
        if (len(self.board) != 3) or self.pair_in_hand():
            return False
        return self.is_one_pair() and \
            not self.has_top_pair() and \
            not self.has_bottom_pair()

    def has_under_middle_pair(self):
        """Verify if the hand is an underpair to the board's middle card."""
        if not self.pair_in_hand() or self.paired_board():
            return False
        rank = self._hand_ranks[0]
        higher_ranks = [x for x in self._board_ranks if x > rank]
        return len(higher_ranks) is 2

    def has_under_pair(self):
        """Verify if the hand is an underpair to the board."""
        if not self.pair_in_hand():
            return False
        rank = Card.get_rank_int(self.cards[0])
        return all(map(lambda x: rank < x, self._board_ranks))

    # Two pair tests start here.
    # has_overpair_to_paired_board defined earlier.

    def has_top_two_pair(self):
        """Verify if the hand has two top pairs."""
        if self.pair_in_hand() or self.paired_board():
            return False
        return self._hand_ranks == self._board_ranks[-2:]

    def has_top_and_bottom(self):
        """Verify if the hand has top and bottom pairs."""
        if self.pair_in_hand() or self.paired_board():
            return False
        return self._hand_ranks[0] == self._board_ranks[0] and \
            self._hand_ranks[1] == self._board_ranks[-1]

    def has_bottom_two_pair(self):
        """Verify if the hand has hit bottom two pairs."""
        if self.pair_in_hand() or self.paired_board():
            return False
        return self._hand_ranks == self._board_ranks[:2]

    def has_under_high_pair(self):
        """Verify the hand is of the form BB on AAC."""
        if not self.pair_in_hand() or not self.paired_board():
            return False
        return self._hand_ranks[0] > self._board_ranks[0] and \
            self._hand_ranks[0] < self._board_ranks[1]

    def has_over_low_pair(self):
        """Verify the hand is of the form BB on ACC."""
        if not self.pair_in_hand() or not self.paired_board():
            return False
        return self._hand_ranks[0] > self._board_ranks[1] and \
            self._hand_ranks[0] < self._board_ranks[2]

    def has_under_pair_to_paired(self):
        """Verify if we have an underpair to a paired board."""
        return self.paired_board() and self.has_under_pair()

    # Sets start here

    def has_top_set(self):
        """Verify we've hit top set."""
        return self.is_set() and self._hand_ranks[0] == self._board_ranks[2]

    def has_middle_set(self):
        """Verify we've hit top set."""
        return self.is_set() and self._hand_ranks[0] == self._board_ranks[1]

    def has_bottom_set(self):
        """Verify we've hit top set."""
        return self.is_set() and self._hand_ranks[0] == self._board_ranks[0]

    # Draws start here
    # All drawing hands should be included below,
    # plus supporting code.
    #
    # Needed method for the draws
    def outs_to(self, flag):
        """Count the number of outs to making a hand.

        Should be used as:
        hand.outs_to(is_flush)

        `flag` is any bool function, actually.
        """
        count = 0
        for c in self.rest_of_the_deck():
            new_board = self.board + [c]
            new_hand = Hand(self.cards, new_board, self.ev)
            if flag(new_hand):
                count += 1
        return count

    # Flags for the direct draws
    def has_straight_flush_draw(self):
        """Has a straight flush draw."""
        return self.outs_to(Hand.is_straight_flush) >= 2

    def has_gutshot_straight_flush_draw(self):
        """Has a gutshot to a straight flush."""
        return self.outs_to(Hand.is_straight_flush) is 1

    def has_flush_draw(self):
        """Verifies if there is a flush draw.

        Returns a tuple of booleans, (high, low)
        (True, False) means there's a flush draw to the high card.
        (False, True) means the same, to the low card.
        (True, True) means the hand is suited, and there's a flush draw.
        (False, False) means no flush draw.

        Should return (True, False) if there's a flush draw with a pair in hand.

        Can be used with any() or all()
        """
        high_card = max(self.cards)
        hc_suit = Card.get_suit_int(high_card)

        low_card = min(self.cards)
        lc_suit = Card.get_suit_int(low_card)

        suits = list(map(Card.get_suit_int, self.cards + self.board))

        high_f_d = len([suit for suit in suits if suit == hc_suit]) == 4
        low_f_d = len([suit for suit in suits if suit == lc_suit]) == 4

        if any([high_f_d, low_f_d]) and self.pair_in_hand():
            return (True, False)

        return (high_f_d, low_f_d)

    def has_straight_draw(self):
        """Has an up-and-down straight draw."""
        outs = self.outs_to(Hand.is_straight)
        if any(self.has_flush_draw()):
            return outs == 6
        else:
            return outs == 8

    def has_gutshot_straight_draw(self):
        """Has a gutshot straight draw."""
        outs = self.outs_to(Hand.is_straight)
        if any(self.has_flush_draw()):
            return outs == 3
        else:
            return outs == 4

    # Backdoor draws come here

    def has_backdoor_flush(self):
        """Verifies if there is a backdoor flush.

        Returns a tuple of booleans, (high, low)
        (True, False) means there's a backdoor flush to the high card.
        (False, True) means the same, to the low card.
        (True, True) means the hand is suited, and there's a backdoor flush
            with a card on the flop.
        (False, False) means no backdoor flush draw.

        Can be used with any() or all()
        """

        high_card = max(self.cards)
        hc_suit = Card.get_suit_int(high_card)

        low_card = min(self.cards)
        lc_suit = Card.get_suit_int(low_card)

        suits = list(map(Card.get_suit_int, self.cards + self.board))

        high_bd_f_d = len([suit for suit in suits if suit == hc_suit]) == 3
        low_bd_f_d = len([suit for suit in suits if suit == lc_suit]) == 3

        return (high_bd_f_d, low_bd_f_d)

    # Overcards tests

    def _number_of_overcards(self):
        overs = [rank for rank in self._hand_ranks if rank > max(self._board_ranks)]
        return len(overs)

    def has_two_overcards(self):
        """Verify we have two overcards to the flop."""
        return self._number_of_overcards() == 2

    def has_one_over(self):
        """Verify we have one overcard to the flop."""
        return self._number_of_overcards() == 1

    FLAGS = [
        is_straight_flush,
        is_quads,
        is_full_house,
        is_flush,
        is_straight,
        is_trips,
        is_set,
        is_two_pair,
        is_one_pair,
        is_high_card,
        has_overpair,
        has_overpair_to_paired_board,
        has_top_pair,
        has_under_top_pair,
        has_bottom_pair,
        has_middle_pair,
        has_under_middle_pair,
        has_under_pair,
        has_top_two_pair,
        has_top_and_bottom,
        has_bottom_two_pair,
        has_under_high_pair,
        has_over_low_pair,
        has_under_pair_to_paired,
        has_top_set,
        has_middle_set,
        has_bottom_set,
        has_straight_flush_draw,
        has_gutshot_straight_flush_draw,
        has_flush_draw,
        has_straight_draw,
        has_gutshot_straight_draw,
        has_backdoor_flush,
        has_two_overcards,
        has_one_over,
    ]
