from collections import Counter


def can_form_names(s1, s2, pile):
    c1 = Counter(s1 + s2)
    c2 = Counter(pile)
    return c1 == c2


if __name__ == '__main__':
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    pile = raw_input().strip()
    print "YES" if can_form_names(s1, s2, pile) else "NO"
