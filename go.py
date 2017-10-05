"""Test program for treys library."""
from treys import Hand
from deuces import Card, Evaluator


ev = Evaluator()

# create a poker hand
hand = Hand([Card.new('Ks'),
            Card.new('Jd')],
            [Card.new('Js'),
            Card.new('Qs'),
            Card.new('2h')], ev)

print(hand)

print("########")

print(hand.has_overpair())
print(hand.has_top_pair())
