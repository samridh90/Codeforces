def canDivide():
    w = int(raw_input())
    if not w or w <= 2:
        return "NO"
    if w % 2 == 0:
        return "YES"
    return "NO"

if __name__ == "__main__":
    print canDivide()