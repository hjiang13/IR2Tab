import os
import argparse
from ir2tab_function import extract_functions_from_ir  # Import the function extraction

def extract_basic_blocks_from_function(function_lines):
    """
    Extracts basic blocks from a function and returns them as a list of basic blocks.
    Each basic block is represented as a dictionary containing the label and instructions.
    """
    basic_blocks = []
    current_block = {
        "label": None,
        "instructions": []
    }
    inside_block = False

    for line in function_lines:
        line = line.strip()

        # Check for basic block label (ends with ":")
        if line.endswith(":"):
            # Save the current block before starting a new one
            if inside_block:
                basic_blocks.append(current_block)
                current_block = {
                    "label": None,
                    "instructions": []
                }
            inside_block = True
            current_block["label"] = line.strip(":")  # Set the block label
        else:
            # Collect instructions inside the current basic block
            current_block["instructions"].append(line)
            # Check if this is a terminator instruction (ends the block)
            if any(term in line for term in ["br", "ret", "switch", "unreachable"]):
                basic_blocks.append(current_block)
                current_block = {
                    "label": None,
                    "instructions": []
                }
                inside_block = False

    # Handle any remaining block
    if current_block["instructions"]:
        basic_blocks.append(current_block)

    return basic_blocks

def save_basic_blocks(basic_blocks, function_idx, output_dir):
    """
    Saves each basic block to a file named based on its label and function index.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for block_idx, block in enumerate(basic_blocks):
        label = block["label"] if block["label"] else f"block_{block_idx}"
        output_file = os.path.join(output_dir, f"function_{function_idx}_{label}.ll")
        with open(output_file, 'w') as f_out:
            f_out.write(f"{block['label']}:\n")
            for instruction in block['instructions']:
                f_out.write(instruction + "\n")
        print(f"Saved: {output_file}")

def main(ir_file, output_dir):
    """
    Main logic to extract basic blocks from functions in the given IR file and save them.
    """
    # Step 1: Extract functions from the IR file
    functions = extract_functions_from_ir(ir_file)
    print(f"Extracted {len(functions)} functions from {ir_file}")

    # Step 2: Process each function to extract basic blocks and save them
    for function_idx, function in enumerate(functions):
        basic_blocks = extract_basic_blocks_from_function(function)
        print(f"Extracted {len(basic_blocks)} basic blocks from function {function_idx}")
        
        # Debugging: Print block information
        for block_idx, block in enumerate(basic_blocks):
            print(f"Basic Block {block_idx}: Label = {block['label']}, Instructions = {len(block['instructions'])}")
        
        # Save the basic blocks to files
        save_basic_blocks(basic_blocks, function_idx, output_dir)

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Extract basic blocks from an LLVM IR file.")
    parser.add_argument("--ir_file", required=True, help="Path to the input LLVM IR file")
    parser.add_argument("--output_dir", default="../test/basic_blocks/", help="Directory where basic blocks will be saved")
    
    # Parse arguments
    args = parser.parse_args()

    # Call the main function
    main(args.ir_file, args.output_dir)
