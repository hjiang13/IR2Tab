import os
import argparse

def extract_functions_from_ir(ir_file):
    """
    Extracts functions from the IR file and returns them as a list of functions.
    Each function is represented as a list of lines (instructions).
    """
    functions = []
    current_function = []
    brace_count = 0
    inside_function = False

    with open(ir_file, 'r') as f_in:
        for line in f_in:
            line = line.strip()

            # Start of a function
            if line.startswith("define") and not inside_function:
                inside_function = True
                brace_count = line.count('{') - line.count('}')
                current_function = [line]  # Start collecting the function lines
            elif inside_function:
                # Update the brace count
                brace_count += line.count('{') - line.count('}')
                current_function.append(line)

                # If brace count reaches zero, function definition is complete
                if brace_count == 0:
                    functions.append(current_function)
                    inside_function = False
                    current_function = []
    
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

def main(ir_file, output_dir):
    """
    Main logic to process the input IR file.
    """
    # Use ir_file
    print(f"Processing file: {ir_file}")

    # Step 1: Extract functions
    functions = extract_functions_from_ir(ir_file)
    print(f"Extracted {len(functions)} functions from {ir_file}")

    # Step 2: Save functions to separate files
    save_functions(functions, output_dir)

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Extract functions from an LLVM IR file.")
    parser.add_argument("--ir_file", required=True, help="Path to the input LLVM IR file")
    parser.add_argument("--output_dir", default="../test/", help="Directory where functions will be saved")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the main function
    main(args.ir_file, args.output_dir)
