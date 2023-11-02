def numJewelsInStones(jewels, stones):
    """
    :type jewels: str
    :type stones: str
    :rtype: int
    """
    types = set()
    n = 0
    for ch in jewels:
        types.add(ch)
    for ch in stones:
        if ch in types:
            n += 1
    return n