import re
from ir2tab_block import extract_basic_blocks_from_function  # Import the basic block extraction
from ir2tab_function import extract_functions_from_ir  # Import the function extraction

def extract_instructions_from_block(block):
    """
    Extracts instructions from a basic block. Each instruction is represented as a
    dictionary containing the result variable, opcode, and operands.
    """
    instructions = []

    for line in block["instructions"]:
        # Ignore labels and comments
        if line.endswith(":") or line.startswith(";") or not line:
            continue

        # Split the line based on assignment and instruction part
        if "=" in line:
            # Pattern: result = opcode type operand1, type operand2
            match = re.match(r'(%\S+)\s*=\s*(\S+)\s+(.+)', line)
            if match:
                result_var = match.group(1)  # e.g., %9
                opcode = match.group(2)      # e.g., mul
                operand_section = match.group(3)
            else:
                continue
        else:
            # For instructions without result assignment (like `br label %bb1`)
            result_var = None
            parts = line.split(maxsplit=1)
            opcode = parts[0]
            operand_section = parts[1] if len(parts) > 1 else ""

        # Extract operands, filtering out type information
        operands = re.findall(r'%\S+', operand_section)

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
    # Input IR file
    ir_file = "../test/sample.ll"  # Adjust this path as needed

    # Extract functions from the IR file
    functions = extract_functions_from_ir(ir_file)

    # Process each function to extract basic blocks and then instructions
    for function_idx, function in enumerate(functions):
        print(f"\nFunction {function_idx}:")
        basic_blocks = extract_basic_blocks_from_function(function)
        
        for block_idx, block in enumerate(basic_blocks):
            print(f"\nBasic Block {block_idx} ({block['label']}):")
            instructions = extract_instructions_from_block(block)
            print_instructions(instructions)
