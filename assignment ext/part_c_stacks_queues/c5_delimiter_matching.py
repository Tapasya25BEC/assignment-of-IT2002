# C5: Delimiter matching using a stack

def is_matched(expr):
    lefts, rights = "({[", ")}]"
    S = []
    for c in expr:
        if c in lefts:
            S.append(c)
        elif c in rights:
            if not S or rights.index(c) != lefts.index(S.pop()):
                return False
    return len(S) == 0

print(is_matched("[(5+x)-(y+z)]"))
print(is_matched("([)]"))
print(is_matched("(("), is_matched(")"), is_matched(""))
