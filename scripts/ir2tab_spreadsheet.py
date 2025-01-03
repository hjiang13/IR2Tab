import os
import csv
import argparse
from ir2tab_instr import extract_instructions_from_block
from ir2tab_function import extract_functions_from_ir
from ir2tab_block import extract_basic_blocks_from_function

def sanitize_for_csv(value):
    """
    Sanitizes the value to remove any commas.
    """
    return value.replace(",", "") if isinstance(value, str) else value

def convert_to_spreadsheet(functions, output_csv):
    """
    Converts functions with basic blocks and instructions into a structured spreadsheet.
    """
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_csv)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open a CSV file for writing
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header row
        writer.writerow([
            "Instruction ID", "Basic Block ID", "Operator", 
            "Destination", "Operand 1", "Operand 2", 
            "Additional Fields", "Dependencies"
        ])

        instruction_counter = 1  # Unique identifier for instructions
        instruction_map = {}  # Map destination to its ID for dependency tracking

        for function_idx, function in enumerate(functions):
            basic_blocks = extract_basic_blocks_from_function(function)
            
            for block_idx, block in enumerate(basic_blocks):
                block_label = block.get("label", f"BB-{block_idx}")
                instructions = extract_instructions_from_block(block)
                
                for instr in instructions:
                    # Extract relevant fields
                    opcode = instr.get('opcode', "unknown")
                    destination = instr.get('destination', "NA")
                    operands = instr.get('operands', [])
                    additional = instr.get('additional', "NA")

                    # Map operands to their corresponding instruction IDs
                    dependency_list = [
                        instruction_map.get(operand, operand) for operand in operands
                    ]

                    # Split operands into separate columns
                    operand1 = operands[0] if len(operands) > 0 else "NA"
                    operand2 = operands[1] if len(operands) > 1 else "NA"

                    # Store the current instruction's ID
                    if destination != "NA":
                        instruction_map[destination] = f"I{instruction_counter}"

                    # Write row data
                    row = [
                        f"I{instruction_counter}",  # Instruction ID
                        block_label,               # Basic Block ID
                        opcode,                    # Operator
                        destination,               # Destination
                        operand1,                  # Operand 1
                        operand2,                  # Operand 2
                        additional,                # Additional Fields
                        ", ".join(dependency_list)  # Dependencies
                    ]
                    sanitized_row = [sanitize_for_csv(str(item)) for item in row]
                    writer.writerow(sanitized_row)

                    instruction_counter += 1

    print(f"Spreadsheet saved to {output_csv}")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert IR to a structured spreadsheet.")
    parser.add_argument("--ir_file", type=str, required=True, help="Path to the IR file")
    parser.add_argument("--output_dir", type=str, default="../data/processed/", help="Directory to save the output CSV file")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Validate the input file path
    if not os.path.isfile(args.ir_file):
        print(f"Error: Input file '{args.ir_file}' does not exist.")
        exit(1)
    
    # Extract functions from the IR
    functions = extract_functions_from_ir(args.ir_file)

    # Dynamically name the output CSV based on the IR file name
    base_name = os.path.basename(args.ir_file).split('.')[0]  # Extract base name without extension
    output_csv = os.path.join(args.output_dir, f"{base_name}_ir_instructions.csv")

    # Convert instructions to a spreadsheet
    convert_to_spreadsheet(functions, output_csv)
