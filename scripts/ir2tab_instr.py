from ir2tab_block import extract_basic_blocks_from_function  # Import the basic block extraction
from ir2tab_function import extract_functions_from_ir  # Import the function extraction

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
