import re
import argparse
from ir2tab_block import extract_basic_blocks_from_function  # Import the basic block extraction
from ir2tab_function import extract_functions_from_ir  # Import the function extraction


import re

import re

def extract_instructions_from_block(block):
    """
    Extracts instructions from a basic block. Each instruction is represented as a
    dictionary containing the destination, opcode, operands, and additional fields.
    """
    instructions = []

    for line in block["instructions"]:
        # Ignore labels and comments
        if line.endswith(":") or line.startswith(";") or not line.strip():
            continue

        # Initialize variables
        destination = None
        opcode = None
        operands = []
        additional = "NA"  # For fields like align or condition

        # Handle lines with an assignment (e.g., %1 = ...)
        if "=" in line:
            # Match memory operations like `alloca`
            if "alloca" in line:
                match = re.match(r'(%\S+)\s*=\s*alloca\s+(\S+)(?:,\s*align\s*(\d+))?', line)
                if match:
                    destination = match.group(1)  # e.g., %1
                    opcode = "alloca"
                    operands = [match.group(2)]  # e.g., i32
                    additional = match.group(3) if match.group(3) else "NA"  # e.g., align 4

            # Match arithmetic and logical operations
            # e.g. %28 = add nsw i32 %27, %26
            elif any(op in line for op in ["add", "sub", "mul", "and", "or"]):
                match = re.match(r'(%\S+)\s*=\s*(\S+)\s*(\S+)?\s+\S+\s+(%\S+),\s+(%\S+)', line)
                if match:
                    destination = match.group(1)  # %28
                    opcode = match.group(2)       # add
                    flags = match.group(3) if match.group(3) else "NA"  # nsw
                    operands= [match.group(4), match.group(5)]  #27%, 26%  

            #Parses an `icmp` instruction.
            # Pattern: %result = icmp <predicate> <type> <operand1>, <operand2>
            elif ("icmp" or "cmp" in line):
                match = re.match(r'(%\S+)\s*=\s*icmp\s+(\S+)\s+(\S+)\s+(%\S+),\s+(%\S+)', line)
                if match:
                    destination = match.group(1)  # e.g., %11
                    opcode = "icmp"    # e.g., sle
                    value_type = match.group(3)   # e.g., i32
                    operands = [match.group(4), match.group(5)]     # e.g., %9, %10


            # Match function calls
            elif "call" in line:
                match = re.match(r'(%\S+)?\s*=\s*call\s+\S+\s+\@(\S+)\((.*)\)', line)
                if match:
                    destination = match.group(1) if match.group(1) else "NA"
                    opcode = "call"
                    operands = match.group(3).split(", ") if match.group(3) else []

        else:
            # Handle lines without an assignment (e.g., br, ret)
            if line.startswith("br"):
                match = re.match(r'br\s+\S+\s+(\S+),\s+label\s+(\S+),\s+label\s+(\S+)', line)
                if match:
                    opcode = "br"
                    operands = [match.group(1), match.group(2), match.group(3)]

            elif line.startswith("ret"):
                match = re.match(r'ret\s+\S+\s+(\S+)', line)
                if match:
                    opcode = "ret"
                    operands = [match.group(1)]

        # Ensure opcode is recognized
        if not opcode:
            opcode = "unknown"

        # Store the instruction as a dictionary
        instruction = {
            "destination": destination,  # The result variable
            "opcode": opcode,            # The opcode
            "operands": operands,        # Operands (variables/constants)
            "additional": additional     # Additional fields like align
        }
        instructions.append(instruction)

    return instructions


def print_instructions(instructions):
    """
    Prints instructions in a readable format.
    """
    for instr in instructions:
        destination = instr["destination"] if instr["destination"] else "NA"
        opcode = instr["opcode"]
        operands = ", ".join(instr["operands"]) if instr["operands"] else "NA"
        additional = instr["additional"]

        print(f"Destination: {destination}, Opcode: {opcode}, Operands: {operands}, Additional: {additional}")

def main(ir_file):
    """
    Main logic to extract instructions from basic blocks of functions in the given IR file.
    """
    # Extract functions from the IR file
    functions = extract_functions_from_ir(ir_file)

    # Process each function to extract basic blocks and instructions
    for function_idx, function in enumerate(functions):
        print(f"\nFunction {function_idx}:")
        basic_blocks = extract_basic_blocks_from_function(function)
        
        for block_idx, block in enumerate(basic_blocks):
            print(f"\nBasic Block {block_idx} ({block['label']}):")
            instructions = extract_instructions_from_block(block)
            print_instructions(instructions)

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Extract instructions from an LLVM IR file.")
    parser.add_argument("--ir_file", required=True, help="Path to the input LLVM IR file")
    
    # Parse arguments
    args = parser.parse_args()

    # Call the main function
    main(args.ir_file)

