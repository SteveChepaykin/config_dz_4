import struct
import xml.etree.ElementTree as ET

instructions = []

COMMANDS = {
    "CONST": 0,
    "GET_MEM": 14,
    "PUT_MEM": 10,
    "NEG": 4
}

registers = [0]*8
memory = [0]*256

def assemble(inputname):
    with open(inputname, 'r') as f:
        for line in f:
            process_line(line.strip())
    write_binary()
    write_log()

def process_line(line):
    # Обработка команд
    parts = line.split()
    comlen = COMMANDS[parts[0]]
    b, c = map(int, parts[1:])
    if parts[0] == 'CONST':
        instructions.append(const(comlen, b, c))
    elif parts[0] == 'GET_MEM':
        instructions.append(get_value(comlen, b, c))
    elif parts[0] == 'PUT_MEM':
        instructions.append(put_value(comlen, b, c))
    elif parts[0] == 'NEG':
        instructions.append(neg(comlen, b, c))

def const(a, b, c):
    return struct.pack('>B B B', (a << 4) | (b << 1), c & 0xFF, (c >> 8) & 0xFF)

def get_value(a, b, c):
    return struct.pack('>B B', (a << 4) | (b << 1), c)

def put_value(a, b, c):
    return struct.pack('>B B B', (a << 4) | (b << 1), c & 0xFF, (c >> 8) & 0xFF)

def neg(a, b, c):
    return struct.pack('>B B B', (a << 4) | (b << 1), c & 0xFF, (c >> 8) & 0xFF)

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

def load_instruction(instruction):
    opcode = instruction[0]
    if opcode == 0:
        B = instruction[1]
        C = (instruction[2]) | instruction[3]
        registers[B] = C
    if opcode == 14:
        B = instruction[1]
        C = (instruction[2]) | instruction[3]
        registers[B] = memory[C]
    if opcode == 10: 
        B = instruction[1]
        C = (instruction[2]) | instruction[3]
        memory[C] = registers[B]
    if opcode == 4:
        B = instruction[1]
        C = (instruction[2]) | instruction[3]
        memory[C] = -memory[registers[B]]

def execute():
    with open("binary.txt", 'rb') as f:
        while byte := f.read(4):
            load_instruction(byte)

def execute_instr():
    for instr in instructions:
        load_instruction(instr)

if __name__ == "__main__":
    s = str(input("enter txt file name (with extension): "))
    assemble(s)
    execute_instr()
