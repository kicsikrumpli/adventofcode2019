from itertools import groupby
from operator import itemgetter


def is_non_decreasing(number, d=100000):
    a = number // d
    b = number % d // (d // 10)
    return ((a <= b) and (d == 10)) or \
           ((a <= b) and is_non_decreasing(number % d, d // 10))


def has_repeating_digit(number):
    return len(set(list(str(number)))) < 6


def has_repeating_group_of_exactly_two(number):
    digits = sorted(list(str(number)))
    exactly_two_length_group = [len(list(v)) == 2 for k, v in groupby(digits)]
    return any(exactly_two_length_group)


def main(start, end):
    passwords = (password for password in range(start, end) if (has_repeating_digit(password) and is_non_decreasing(password)))
    print("puzzle1 – non decreasing digits and at least one repeating: ", len(list(passwords)))


if __name__ == "__main__":
    main(168630,718098)
