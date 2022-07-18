import poker as p

sf = "6C 7C 8C 9C TC".split()  # Straight Flush
tp = "5S 5D 9H 9C 6S".split()  # Two pairs
fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
fh = "TD TC TH 7C 7D".split()  # Full House
sf2 = "6D 7D 8D 9D TD".split()  # Straight Flush


def test1_card_ranks():
    assert p.card_ranks(sf) == [10, 9, 8, 7, 6]
    assert p.card_ranks(fk) == [9, 9, 9, 9, 7]
    assert p.card_ranks(fh) == [10, 10, 10, 7, 7]


def test1_hand_rank():
    assert p.hand_rank(sf) == (8, 10)
    assert p.hand_rank(fk) == (7, 9, 7)
    assert p.hand_rank(fh) == (6, 10, 7)


def test_kinds():
    fkranks = p.card_ranks(fk)
    tpranks = p.card_ranks(tp)
    assert p.kind(4, fkranks) == 9
    assert p.kind(3, fkranks) is None
    assert p.kind(2, fkranks) is None
    assert p.kind(1, fkranks) == 7


def test_poker():
    assert p.poker([sf, fk, fh]) == [sf]
    assert p.poker([fk, fh]) == [fk]
    assert p.poker([fh, fh]) == [fh, fh]
    assert p.poker([sf]) == [sf]


def test_straight():
    assert p.straight([9, 8, 7, 6, 5]) == True
    assert p.straight([9, 8, 8, 6, 5]) == False


def test_flush():
    assert p.flush(sf) == True
    assert p.flush(fk) == False


def test_tie_breaker():
    assert p.poker([sf, sf2, fk, fh]) == [sf, sf2]
