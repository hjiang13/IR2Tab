# scripts/ir2tab_program.py
#At the top level, we handle the program as a whole. 
#This involves loading the IR, identifying the functions, 
# and preparing the data at the program level (e.g., program metadata).
def process_program(ir_file):
    """
    Processes the entire program and splits it into functions.
    """
    functions = []
    with open(ir_file, 'r') as f_in:
        current_function = []
        for line in f_in:
            if line.startswith("define"):
                if current_function:
                    functions.append(current_function)
                    current_function = []
            current_function.append(line)
        if current_function:
            functions.append(current_function)
    
    return functions

if __name__ == "__main__":
    ir_file = "../data/processed/sample.ll"
    functions = process_program(ir_file)
    print(f"Extracted {len(functions)} functions from the program.")
