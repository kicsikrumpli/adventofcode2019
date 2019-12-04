import sys


def calculate_fuel_from(mass):
    return (mass // 3) - 2


def fuel_generator(mass):
    m = calculate_fuel_from(mass)
    while m > 0:
        yield m
        m = calculate_fuel_from(m)


def total_fuel(f):
    masses = (fuel_weight
              for module_weight in f
              for fuel_weight in fuel_generator(int(module_weight)))
    return sum(masses)


def main(filename):
    with open(filename) as f:
        print(total_fuel(f))
    return


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("pyton3 02_fuel.py input.txt")
