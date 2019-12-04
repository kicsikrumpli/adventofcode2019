import sys

OP_ADD = 1
OP_MUL = 2
OP_HALT = 99
IP_STEP = 4
NOUN = 1
VERB = 2
SYMBOLS = {OP_ADD: "+", OP_MUL: "*", OP_HALT: "H"}


def run(prog, noun=12, verb=2):
    ip = 0
    done = False
    prog[NOUN] = noun
    prog[VERB] = verb
    while not done:
        op = prog[ip]
        arg1 = prog[prog[ip + 1]]
        arg2 = prog[prog[ip + 2]]
        target_address = prog[ip + 3]
        if op == OP_ADD:
            prog[target_address] = arg1 + arg2
        elif op == OP_MUL:
            prog[target_address] = arg1 * arg2
        elif op == OP_HALT:
            done = True
        else:
            raise Exception
        ip += IP_STEP
    return prog


def find(mem, target):
    params = {run(mem[:], noun, verb)[0]: (noun, verb)
              for noun in range(100)
              for verb in range(100)}
    return params.get(target)


def main(f):
    with open(f) as prog:
        mem = list(map(lambda s: int(s), prog.readline().split(sep=",")))
        noun, verb = find(mem, 19690720)
        print(100 * noun + verb)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("python3 01_cpu.py input.txt")
