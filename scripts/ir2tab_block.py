# scripts/ir2tab_block.py
#basic block extraction from the individual functions. 
# In LLVM IR, basic blocks are typically identified by labels (e.g., entry:, bb1:) followed by a sequence of instructions, 
# and they end with a terminator instruction (like br, ret, or switch).

#Plan for Basic Block Extraction:
# Identify basic blocks: Each basic block starts with a label (ending with a colon :) and continues until a terminator instruction.
# Group instructions: All instructions between the label and the terminator are part of the basic block.
# Store basic blocks: We'll collect basic blocks from each function and save them for further analysis or processing.


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
            if inside_block:
                basic_blocks.append(current_block)
                current_block = {
                    "label": None,
                    "instructions": []
                }
            inside_block = True
            current_block["label"] = line.strip(":")
        else:
            # Collect instructions inside the current basic block
            current_block["instructions"].append(line)
            # Check if this is a terminator instruction (which ends the basic block)
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
    Saves each basic block to a file named function_<idx>_block_<block_idx>.ll
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for block_idx, block in enumerate(basic_blocks):
        output_file = os.path.join(output_dir, f"function_{function_idx}_block_{block_idx}.ll")
        with open(output_file, 'w') as f_out:
            f_out.write(f"{block['label']}:\n")
            for instruction in block['instructions']:
                f_out.write(instruction + "\n")
        print(f"Saved: {output_file}")

if __name__ == "__main__":
    # Example function as a list of lines
    sample_function = [
        "define i32 @main() {",
        "entry:",
        "%0 = alloca i32, align 4",
        "store i32 0, i32* %0, align 4",
        "br label %bb1",
        "bb1:",
        "%1 = load i32, i32* %0, align 4",
        "ret i32 %1",
        "}"
    ]

    # Extract basic blocks
    basic_blocks = extract_basic_blocks_from_function(sample_function)
    print(f"Extracted {len(basic_blocks)} basic blocks.")

    # Save basic blocks (replace with actual function index and output directory)
    save_basic_blocks(basic_blocks, function_idx=0, output_dir="../data/basic_blocks/")

