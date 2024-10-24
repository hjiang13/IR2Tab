# scripts/ir2tab_function.py
#Let's start by slicing the LLVM IR files into individual functions. 
# We will write a script that processes the IR file, identifies where each function begins and ends, and then extracts the function body. 
# Each function will be saved separately or stored in a data structure that can be used later in the pipeline.

#Here’s the plan:

# 1. Identify function definitions (define keyword in LLVM IR).
# 2. Track the function body (from the define to the closing }).
# 3. Store each function separately for further processing.

import os

def extract_functions_from_ir(ir_file):
    """
    Extracts functions from the IR file and returns them as a list of functions.
    Each function is represented as a list of lines (instructions).
    """
    functions = []
    current_function = []
    inside_function = False

    with open(ir_file, 'r') as f_in:
        for line in f_in:
            line = line.strip()

            # Check for function start (LLVM IR function starts with "define")
            if line.startswith("define"):
                inside_function = True
                if current_function:
                    functions.append(current_function)
                    current_function = []
                current_function.append(line)
            elif line == "}":
                # End of function
                current_function.append(line)
                functions.append(current_function)
                inside_function = False
                current_function = []
            elif inside_function:
                # Collect lines inside the function
                current_function.append(line)

    return functions

def save_functions(functions, output_dir):
    """
    Saves each function to a separate file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for idx, function in enumerate(functions):
        output_file = os.path.join(output_dir, f"function_{idx}.ll")
        with open(output_file, 'w') as f_out:
            for line in function:
                f_out.write(line + "\n")
        print(f"Saved: {output_file}")

if __name__ == "__main__":
    # Input IR file
    ir_file = "../data/raw/sample.ll"

    # Output directory where functions will be saved
    output_dir = "../data/functions/"

    # Step 1: Extract functions
    functions = extract_functions_from_ir(ir_file)
    print(f"Extracted {len(functions)} functions from {ir_file}")

    # Step 2: Save functions to separate files
    save_functions(functions, output_dir)

