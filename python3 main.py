# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append((i,next))
            pass

        if next in ")]}":
            if len(opening_brackets_stack)==0:
                return i+1
            for j in range(len(opening_brackets_stack)-1,-1,-1):
                if opening_brackets_stack[j][1] in "([{":
                    if are_matching(opening_brackets_stack[j][1],next):
                        opening_brackets_stack.pop(j)
                        break
                    else:
                        return i+1
            pass

    if len(opening_brackets_stack)==1:
        return opening_brackets_stack[0][0]+1
    return 0
pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch !=0:
        print(mismatch)
        return 0
    print("Success")
    return 0
pass


if __name__ == "__main__":
    main()
