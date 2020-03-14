"""Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
"""
import sys


def main():
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if s1 is None or s2 is None:
        print("false")
        return False
    if len(s1) != len(s2):
        print("false")
        return False
    mapping = {}
    for i in range(len(s1)):
        a = s1[i]
        b = s2[i]
        if a in mapping:
            if mapping[a] != b:
                print("false")
                return False
        else:
            mapping[a] = b
    print("true")
    return True


if __name__ == '__main__':
    main()
