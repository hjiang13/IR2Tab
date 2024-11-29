import os
import csv
import argparse
from ir2tab_instr import extract_instructions_from_block
from ir2tab_function import extract_functions_from_ir
from ir2tab_block import extract_basic_blocks_from_function
from operator_formulas import build_dependency_formula
from classify_format import classify_format

def sanitize_for_csv(value):
    """
    Sanitizes the value to remove any commas.
    """
    return value.replace(",", "") if isinstance(value, str) else value

def convert_to_csv_with_dependency(functions, output_csv):
    """
    Converts functions with basic blocks and instructions into a CSV file.
    Each instruction's result is represented in a cell with a formula showing dependencies.
    """
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_csv)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open a CSV file for writing with a tab delimiter to avoid commas
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')  # Use tab as a delimiter

        # Write header row without any commas
        writer.writerow(["Instruction #", "Format", "Opcode", "Destination", "Operand1", "Operand2", "Formula"])

        instruction_counter = 1  # Track instruction numbers
        instruction_cells = {}  # Map result_var to its cell reference

        for function_idx, function in enumerate(functions):
            basic_blocks = extract_basic_blocks_from_function(function)
            
            for block_idx, block in enumerate(basic_blocks):
                instructions = extract_instructions_from_block(block)
                
                for instr in instructions:
                    opcode = instr['opcode']
                    result_var = instr['result_var'] if instr['result_var'] else "NA"
                    operand1 = instr['operand1'] if instr['operand1'] else "NA"
                    operand2 = instr['operand2'] if instr['operand2'] else "NA"

                    # Classify format
                    instr_format = classify_format(opcode)

                    # Map operand1 and operand2 to cell references if available
                    operand_cells = [
                        instruction_cells.get(operand1, operand1),
                        instruction_cells.get(operand2, operand2),
                    ]

                    # Ensure no commas in cell references
                    operand_cells = [sanitize_for_csv(cell) for cell in operand_cells]

                    # Build the dependency formula using the imported function
                    formula = build_dependency_formula(opcode, operand_cells)
                    formula = sanitize_for_csv(formula)

                    # Save the result_var cell reference for future dependencies
                    current_row = instruction_counter + 1  # Adjust to match row indexing in Excel
                    if result_var != "NA":
                        result_cell_ref = f"D{current_row}"
                        instruction_cells[result_var] = result_cell_ref  # Map result_var (e.g., %8) to its cell reference (e.g., D8)

                    # Write row data with formula if applicable
                    row = [instruction_counter, instr_format, opcode, result_var, operand1, operand2, formula]
                    sanitized_row = [sanitize_for_csv(str(item)) for item in row]
                    writer.writerow(sanitized_row)

                    instruction_counter += 1

    print(f"CSV with dependencies saved to {output_csv}")

if __name__ == "__main__":
    # Argument parsing
    parser = argparse.ArgumentParser(description="Convert IR to CSV with dependencies.")
    parser.add_argument("ir_file", type=str, help="Path to the IR file")
    args = parser.parse_args()
    
    # Input IR file
    ir_file = args.ir_file
    
    # Extract functions from the IR
    functions = extract_functions_from_ir(ir_file)

    # Dynamically name the output CSV based on the IR file name
    base_name = os.path.basename(ir_file).split('.')[0]  # Extract base name without extension
    output_csv = f"../data/processed/{base_name}_ir_instructions_with_cell_deps.csv"

    # Convert functions to a CSV with cell-based dependencies
    convert_to_csv_with_dependency(functions, output_csv)
