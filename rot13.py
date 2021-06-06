import sys
from string import ascii_lowercase, ascii_uppercase


def rotate(message):
    """
    Returns the encoded or decoded message.
    """
    rot_message = ''
    lower = ascii_lowercase
    upper = ascii_uppercase
    for x in message:
        if x in lower:
            if lower.index(x) < 13:
                rot_message += lower[lower.index(x) + 13]
            else:
                rot_message += lower[lower.index(x) - 13]
        elif x in upper:
            if upper.index(x) < 13:
                rot_message += upper[upper.index(x) + 13]
            else:
                rot_message += upper[upper.index(x) - 13]
        else:
            rot_message += x

    return rot_message


def main(args):
    """Main program code."""
    if len(args) != 1:
        print('usage: python rot13.py message')
        sys.exit(1)

    message = sys.argv[1]

    rot = rotate(message)
    print(rot)


if __name__ == '__main__':
    main(sys.argv[1:])
