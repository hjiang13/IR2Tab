# scripts/ir2tab_spreadsheet.py

import openpyxl
from openpyxl.utils import get_column_letter
from ir2tab_instr import extract_instructions_from_block
from ir2tab_function import extract_functions_from_ir
from ir2tab_block import extract_basic_blocks_from_function
from operator_formulas import build_dependency_formula  # Import the formula function

def convert_to_spreadsheet_with_dependency(functions, output_xlsx):
    """
    Converts functions with basic blocks and instructions into a spreadsheet.
    Each instruction's result is represented in a cell with a formula showing dependencies
    using cell numbers.
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "IR Dependencies"

    # Header row
    ws.append(["Function", "BasicBlock", "Result", "Opcode", "Formula"])

    row_counter = 2  # Start from the second row, since row 1 is the header

    for function_idx, function in enumerate(functions):
        basic_blocks = extract_basic_blocks_from_function(function)
        
        for block_idx, block in enumerate(basic_blocks):
            block_label = block['label']
            instructions = extract_instructions_from_block(block)
            
            for instr_idx, instr in enumerate(instructions):
                result_var = instr['result_var'] if instr['result_var'] else ""
                opcode = instr['opcode']
                operands = instr['operands']
                
                # Map operands to cell numbers
                operand_cells = []
                for operand_idx, operand in enumerate(operands):
                    # Operand cells are in column 'C', starting from the current row and index
                    operand_cell = f'C{row_counter - len(instructions) + operand_idx}'  # Adjust to point to earlier rows
                    operand_cells.append(operand_cell)

                # Build the dependency formula with cell numbers
                formula = build_dependency_formula(opcode, operand_cells)

                # Write the result and formula directly into the spreadsheet
                ws[f'C{row_counter}'] = result_var
                ws[f'D{row_counter}'] = opcode
                ws[f'E{row_counter}'] = formula

                # Add function and basic block labels
                ws[f'A{row_counter}'] = f'function_{function_idx}'
                ws[f'B{row_counter}'] = block_label

                row_counter += 1

    # Save the workbook
    wb.save(output_xlsx)
    print(f"Spreadsheet with dependencies saved to {output_xlsx}")

if __name__ == "__main__":
    # Input IR file
    ir_file = "../data/raw/sample.ll"
    
    # Extract functions from the IR
    functions = extract_functions_from_ir(ir_file)

    # Output Excel file
    output_xlsx = "../data/processed/ir_instructions_with_cell_deps.xlsx"

    # Convert functions to a spreadsheet with cell-based dependencies
    convert_to_spreadsheet_with_dependency(functions, output_xlsx)
