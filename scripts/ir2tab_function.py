import os

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

if __name__ == "__main__":
    # Input IR file
    ir_file = "../test/sample.ll"

    # Output directory where functions will be saved
    output_dir = "../test/"

    # Step 1: Extract functions
    functions = extract_functions_from_ir(ir_file)
    print(f"Extracted {len(functions)} functions from {ir_file}")

    # Step 2: Save functions to separate files
    save_functions(functions, output_dir)
