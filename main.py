"""Determine whether a one-to-one character mapping exists from one string, s1, to another string, s2.
"""
import sys


def main():
    # check if we have two string inputs
    if len(sys.argv) != 3:
        print("false")
        return False
    # read input s1 sand s2
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    # check if s1 and s2 have different length
    if len(s1) != len(s2):
        print("false")
        return False
    # store the mapping info into a dictionary
    mapping = {}
    for i in range(len(s1)):
        a = s1[i]
        b = s2[i]
        if a in mapping:
            # print "false" since the character a cannot map to two characters
            if mapping[a] != b:
                print("false")
                return False
        else:
            mapping[a] = b
    # print "true" since each character in s1 can be mapped to a character in s2
    print("true")
    return True


if __name__ == '__main__':
    main()
