import struct
import xml.etree.ElementTree as ET

instructions = []

COMMANDS = {
    "CONST": 0,
    "GET_MEM": 14,
    "PUT_MEM": 10,
    "NEG": 4
}

registers = [0]*1024
memory = [0]*1024

def assemble(inputname):
    with open(inputname, 'r') as f:
        for line in f:
            process_line(line.strip())
    write_binary()
    write_log()

def process_line(line):
    parts = line.split()
    comlen = COMMANDS[parts[0]]
    b, c = map(int, parts[1:])
    byt = 0
    if parts[0] == 'CONST':
        byt = 3
    elif parts[0] == 'GET_MEM':
        byt = 2
    elif parts[0] == 'PUT_MEM':
        byt = 4
    elif parts[0] == 'NEG':
        byt = 4
    else:
        return
    instructions.append(process_command(comlen, b, c, byt))
    return 

def process_command(a, b, c, byt):
    ii = 0
    ii += c
    ii = ii << 3
    ii += b
    ii = ii << 4
    ii += a
    return ii.to_bytes(byt, byteorder='little')

def write_binary():
    with open("binary.txt", 'wb') as out:
        for instruction in instructions:
            out.write(instruction)

def write_log():
    root = ET.Element("Log")
    for idx, instruction in enumerate(instructions):
        cmd = ET.SubElement(root, "Instruction")
        cmd.set("index", str(idx))
        cmd.set("instr", str(instruction))
        cmd.text = instruction.hex()
    tree = ET.ElementTree(root)
    tree.write("log.xml")
    

def execute_instructions():
    root = ET.Element("Out")
    for idx, instr in enumerate(instructions):
        ii = int.from_bytes(instr, byteorder='little')
        a = ii & 15
        ii = ii >> 4
        b = ii & 7
        ii = ii >> 3
        c = ii
        innertext = ""
        if a == 0:
            registers[b] = c
            innertext = f"loaded {c} in register by adress {b}"
        if a == 14:
            registers[c] = memory[registers[b]]
            innertext = f"loaded info from memory by adress described in register {b} into register by adress {c}"
        if a == 10:
            memory[registers[c]] = registers[b]
            innertext = f"loaded info from register {b} into memory cell described in register {c}"
        if a == 4:
            memory[registers[c]] = -memory[registers[b]]
            innertext = f"loaded unary minus result: {-memory[registers[b]]} into memory cell described in register {c}"
        
        cmd = ET.SubElement(root, str(a))
        cmd.set("index", str(idx))
        cmd.set("adress", str(b))
        cmd.set("operand", str(c))
        cmd.text = innertext
    tree = ET.ElementTree(root)
    tree.write("out.xml")


if __name__ == "__main__":
    s = str(input("enter txt file name (with extension): "))
    assemble(s)
    execute_instructions()
