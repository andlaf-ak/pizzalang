import sys
import math

def generate_pizza_instructions(target_ascii):
    if target_ascii < 1:
        return ["Z"]  # Just clear the memory for 0
    instructions = ["Z", "I"]  # Start from 1
    doubles = int(math.log2(target_ascii))
    base = 2 ** doubles
    increments = target_ascii - base
    instructions += ["IZ"] * doubles
    instructions += ["I"] * increments
    return instructions

def encode_line_to_pizzavm(line):
    instrs = []
    for char in line:
        ascii_val = ord(char)
        instrs += generate_pizza_instructions(ascii_val)
        instrs.append("PIZZ")  # Move to next memory cell

    # Add null terminator (0) at end
    instrs.append("Z")       # Zero out this memory cell

    # Move pointer back to start of string
    instrs += ["PIZ"] * len(line)

    # Print ASCIIZ string
    instrs.append("P")

    return instrs

def new_line_instructions():
    return 'Z I IZ IZ IZ I I PIZZ Z PIZ P '

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        instrs = encode_line_to_pizzavm(line)
        print(new_line_instructions())
        print(' '.join(instrs))

if __name__ == "__main__":
    main()
