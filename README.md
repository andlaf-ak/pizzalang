# PizzaLang VM 🍕🖥️

A minimalistic assembly-like virtual machine inspired by the letters of **"PIZZA"**.
Designed to run programs using a quirky set of opcodes derived from substrings of the word "PIZZA".

---

## 🚀 Features

- Simple memory tape VM with 4092 cells (byte-sized)
- Two general-purpose registers: `A` and `C` (counter)
- Loop constructs with `ZZA` (loop start) and `IZZA` (loop end + conditional jump)
- Output as integers or ASCIIZ strings
- Basic arithmetic and pointer manipulation
- Easy to learn opcode set based on `P`, `I`, `Z`, and `A`

---

## 📝 Opcodes

| Opcode  | Description                                                |
|---------|------------------------------------------------------------|
| `PIZZA` | No operation (NOP) - Place it wherever you want!           |
| `PIZZ`  | Move memory pointer right                                  |
| `PIZ`   | Move memory pointer left                                   |
| `PI`    | Print current memory cell as integer                       |
| `P`     | Print ASCIIZ string starting at pointer                    |
| `IZZ`   | Shift current cell right (divide by 2)                     |
| `IZ`    | Shift current cell left (multiply by 2 modulo 256)         |
| `I`     | Increment current memory cell (modulo 256)                 |
| `Z`     | Set current memory cell to zero                            |
| `ZA`    | Add register A to current memory cell (mod 256)            |
| `A`     | Load current memory cell into register A                   |
| `ZZ`    | Load current memory cell into register C (counter)         |
| `ZZA`   | Start loop (push instruction pointer)                      |
| `IZZA`  | End loop (decrement C and jump to matching `ZZA` if C ≠ 0) |

---

## 📦 Usage

1. Write your PizzaLang program in a text file (e.g. `program.pizza`).
2. Run the VM with the program provided via stdin:

```bash
python pizzalang_vm.py < program.pizza
