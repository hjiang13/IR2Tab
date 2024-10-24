# scripts/ir2tab_instr.py

#In LLVM IR, each instruction consists of an opcode (e.g., add, br, ret, etc.) and operands (registers, constants, or memory locations). 
# We'll write a script to extract these elements from each instruction within the basic blocks.

#Plan for Instruction Extraction:
# Identify the opcode: Each instruction starts with an opcode, which defines the type of operation (e.g., add, sub, load, store).
# Extract operands: After the opcode, operands follow, which could be registers, constants, or memory references.
# Store instructions: We'll store the extracted opcode and operands for each instruction.


def extract_instructions_from_block(block):
    """
    Extracts instructions from a basic block. Each instruction is represented as a
    dictionary containing the opcode and its operands.
    """
    instructions = []
    
    for line in block["instructions"]:
        # Ignore labels and comments
        if line.endswith(":") or line.startswith(";"):
            continue

        # Split line into parts to get opcode and operands
        parts = line.split()

        # Check if it's a valid instruction (ignore metadata and alignments)
        if "=" in line:
            result_var = parts[0]  # E.g., %0 = add i32 %a, %b
            opcode = parts[2]
            operands = parts[3:]
        else:
            result_var = None
            opcode = parts[0]  # E.g., br label %bb1
            operands = parts[1:]

        # Store the instruction as a dictionary
        instruction = {
            "result_var": result_var,
            "opcode": opcode,
            "operands": operands
        }
        instructions.append(instruction)

    return instructions

def print_instructions(instructions):
    """
    Prints instructions in a readable format.
    """
    for instr in instructions:
        result = instr["result_var"] if instr["result_var"] else ""
        print(f"{result} {instr['opcode']} {' '.join(instr['operands'])}")

if __name__ == "__main__":
    # Example basic block
    sample_block = {
        "label": "entry",
        "instructions": [
            "%0 = alloca i32, align 4",
            "store i32 0, i32* %0, align 4",
            "br label %bb1"
        ]
    }

    # Extract instructions from the block
    instructions = extract_instructions_from_block(sample_block)

    # Print instructions in a readable format
    print("Extracted Instructions:")
    print_instructions(instructions)
