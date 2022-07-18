import random

my_deck = [r + s for r in '23456789TJQKA' for s in 'SHDC']


def deal(num_hands, n=5, deck=None):
    """deal n hands with n cards each"""
    if deck is None:
        deck = my_deck
    random.shuffle(deck)
    hands = []
    for i in range(num_hands):
        hands.append(deck[i * n:(i + 1) * n])
    return hands


def poker(hands):
    """Return the best hand: poker([hand,...]) => hand"""
    return allmax(hands, key=hand_rank)


def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first"""
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight."""
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    """Return True if all the cards have the same suit."""
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """Return the first rank that this hand has param cards of"""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """If there are two pair, return the two ranks of the two pairs,
    else None. """
    pair = kind(2, ranks)
    low_pair = kind(2, list(reversed(ranks)))
    if pair and low_pair != pair:
        return pair, low_pair
    else:
        return None


def hand_rank(hand):
    """Return the rank of a hand"""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return 8, max(ranks)
    elif kind(4, ranks):
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):
        return 5, ranks
    elif straight(ranks):
        return 4, max(ranks)
    elif kind(3, ranks):
        return 3, kind(3, ranks), ranks
    elif two_pair(ranks):
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):
        return 1, kind(2, ranks), ranks
    else:
        return 0, ranks


def allmax(iterable, key=None):
    """Return a list of all items equal to the max of the iterable."""
    result = []
    max_val = None
    for x in iterable:
        if key is None:
            val = x
        else:
            val = key(x)
        if max_val is None or val > max_val:
            result = [x]
            max_val = val
        elif val == max_val:
            result.append(x)
    return result
