import sys


def calculate_fuel_from(mass):
    return (mass // 3) - 2


def total_fuel(f):
    masses = (int(dist) for dist in f)
    fuel_amounts = map(calculate_fuel_from, masses)
    total = sum(fuel_amounts)
    return total


def main(filename):
    with open(filename) as f:
        print(total_fuel(f))
    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("pyton3 01_fuel.py input.txt")
