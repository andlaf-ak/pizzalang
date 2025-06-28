import sys

class PizzaVM:
    def __init__(self, memory_size=4092):
        self.memory = [0] * memory_size
        self.ptr = 0
        self.register_a = 0
        self.counter = 0
        self.ip = 0
        self.tokens = []
        self.loop_stack = []

    def sanitize_code(self, raw_code):
        sanitized_lines = []
        for line in raw_code.splitlines():
            line = line.split(';', 1)[0].strip()  # Remove comments and trailing whitespace
            if line:  # Skip empty lines
                sanitized_lines.append(line)
        return ' '.join(sanitized_lines)

    def run(self, code):
        sanitized_code = self.sanitize_code(code)
        self.tokens = sanitized_code.split()
        self.ip = 0

        while self.ip < len(self.tokens):
            instr = self.tokens[self.ip]

            if instr == "PIZZ":
                self.ptr = (self.ptr + 1) % len(self.memory)

            elif instr == "PIZ":
                self.ptr = (self.ptr - 1) % len(self.memory)

            elif instr == "PI":
                print(self.memory[self.ptr], end=' ')

            elif instr == "P":
                i = self.ptr
                while i < len(self.memory) and self.memory[i] != 0:
                    print(chr(self.memory[i]), end='')
                    i += 1

            elif instr == "IZZ":
                self.memory[self.ptr] //= 2

            elif instr == "IZ":
                self.memory[self.ptr] = (self.memory[self.ptr] * 2) % 256

            elif instr == "I":
                self.memory[self.ptr] = (self.memory[self.ptr] + 1) % 256

            elif instr == "Z":
                self.memory[self.ptr] = 0

            elif instr == "ZA":
                self.memory[self.ptr] = (self.memory[self.ptr] + self.register_a) % 256

            elif instr == "A":
                self.register_a = self.memory[self.ptr]

            elif instr == "ZZ":
                self.counter = self.memory[self.ptr]

            elif instr == "ZZA":
                # Push the IP of the loop start
                self.loop_stack.append(self.ip)

            elif instr == "IZZA":
                # Decrement the counter
                self.counter = (self.counter - 1) % 256
                if self.counter != 0 and self.loop_stack:
                    # Jump back to the last ZZA if counter not zero
                    self.ip = self.loop_stack[-1]
                    continue
                elif self.counter == 0 and self.loop_stack:
                    self.loop_stack.pop()

            elif instr == "PIZZA":
                pass  # nop

            self.ip += 1


vm = PizzaVM()
code = sys.stdin.read()
vm.run(code)
