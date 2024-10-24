# IR2Tab: LLVM IR to Spreadsheet Scripts

## Overview

This project contains a set of scripts that convert LLVM Intermediate Representation (IR) into a spreadsheet format where instruction dependencies are represented as cell-based formulas. The primary goal is to visualize data flow between instructions in a clear and structured way using real cell references in the spreadsheet.

## Scripts

### 1. `ir2tab_spreadsheet.py`
The main script that processes LLVM IR files, slices them into functions, basic blocks, and instructions, and generates a spreadsheet with cell-based formulas. These formulas show how the result of one instruction depends on the outputs of other instructions.

- **Key Functionality**:
  - Extracts functions and basic blocks from LLVM IR files.
  - Converts instructions into formulas using cell references (e.g., `C1 + C2` for an `add` operation).
  - Writes the resulting data into an Excel-compatible `.xlsx` file.

- **Usage**:
  Run this script to process your `.ll` files and generate the dependency spreadsheet.

### 2. `operator_formulas.py`
This script defines formulas for 60+ LLVM IR operators. Each operator (e.g., `add`, `sub`, `load`, `br`) is mapped to a corresponding formula that represents the data dependency in a spreadsheet-friendly format.

- **Key Functionality**:
  - Maps LLVM operators to appropriate formulas (e.g., `=A1 + A2` for `add`).
  - Covers arithmetic, logical, memory, control flow, and cast operations.

- **Usage**:
  This script is imported by `ir2tab_spreadsheet.py` and automatically applies the correct formula for each operator during the conversion process.

### 3. `ir2tab_instr.py`
A helper script that extracts instructions from basic blocks in the LLVM IR. This script parses the individual lines of LLVM IR instructions and structures them for further processing.

- **Key Functionality**:
  - Identifies the opcode, result variable, and operands for each instruction.
  - Prepares the instructions for conversion into spreadsheet formulas.

- **Usage**:
  This script is used internally by `ir2tab_spreadsheet.py` to handle instruction extraction.

### 4. `ir2tab_function.py`
This script handles slicing the LLVM IR into functions. It processes the input IR file and breaks it down into individual functions for further analysis.

- **Key Functionality**:
  - Identifies and extracts functions from LLVM IR files.
  - Prepares functions for basic block extraction.

- **Usage**:
  This script is called by `ir2tab_spreadsheet.py` to divide the IR code into manageable functions.

### 5. `ir2tab_block.py`
This script extracts basic blocks from each function in the LLVM IR. Basic blocks are groups of instructions that have a single entry and exit point.

- **Key Functionality**:
  - Identifies basic blocks within a function.
  - Groups instructions within each block for further processing.

- **Usage**:
  This script is used by `ir2tab_spreadsheet.py` to handle the basic block breakdown of functions.

## How It Works

1. **IR File Processing**: `ir2tab_spreadsheet.py` loads LLVM IR files and uses `ir2tab_function.py` and `ir2tab_block.py` to break the code into manageable chunks.
2. **Instruction Extraction**: `ir2tab_instr.py` is used to extract the opcode and operands from each instruction.
3. **Operator Formulas**: `operator_formulas.py` provides the appropriate formula for each LLVM operator, which is then written into the corresponding spreadsheet cell.
4. **Spreadsheet Generation**: The final output is an Excel `.xlsx` file with dependencies shown through cell-based formulas.

## Conclusion

Each script in this project plays a role in converting LLVM IR into a structured, formula-based spreadsheet format. The modular design makes it easy to extend or modify any part of the process to suit different IR analysis needs.
