# scripts/operator_formulas.py

def build_dependency_formula(opcode, operand_cells):
    """
    Constructs a formula for the spreadsheet based on the opcode and operand cells.
    Enumerates all possible operators and gives reasonable formula definitions.
    """
    # Ensure we have enough operand cells for each formula
    operand_cells = operand_cells + [""] * (3 - len(operand_cells))  # Extend to at least 3 items for safety

    operator_formulas = {
        # Arithmetic operators
        "add": f"={operand_cells[0]} + {operand_cells[1]}",
        "sub": f"={operand_cells[0]} - {operand_cells[1]}",
        "mul": f"={operand_cells[0]} * {operand_cells[1]}",
        "div": f"={operand_cells[0]} / {operand_cells[1]}",
        "fadd": f"={operand_cells[0]} + {operand_cells[1]}",
        "fsub": f"={operand_cells[0]} - {operand_cells[1]}",
        "fmul": f"={operand_cells[0]} * {operand_cells[1]}",
        "fdiv": f"={operand_cells[0]} / {operand_cells[1]}",

        # Logical operators
        "and": f"={operand_cells[0]} AND {operand_cells[1]}",
        "or": f"={operand_cells[0]} OR {operand_cells[1]}",
        "xor": f"={operand_cells[0]} XOR {operand_cells[1]}",

        # Shift operators
        "shl": f"={operand_cells[0]} << {operand_cells[1]}",
        "lshr": f"={operand_cells[0]} >> {operand_cells[1]}",
        "ashr": f"={operand_cells[0]} >>> {operand_cells[1]}",

        # Comparison operators
        "icmp": f"=IF({operand_cells[0]} = {operand_cells[1]}, TRUE, FALSE)",
        "fcmp": f"=IF({operand_cells[0]} = {operand_cells[1]}, TRUE, FALSE)",

        # Memory operations
        "load": f"=LOAD({operand_cells[0]})",
        "store": f"=STORE({operand_cells[0]}, {operand_cells[1]})",
        "alloca": f"=ALLOCATE({operand_cells[0]})",

        # Cast and conversion operators
        "zext": f"=ZERO_EXTEND({operand_cells[0]})",
        "sext": f"=SIGN_EXTEND({operand_cells[0]})",
        "trunc": f"=TRUNCATE({operand_cells[0]})",
        "bitcast": f"=BITCAST({operand_cells[0]})",
        "fptrunc": f"=FLOAT_TRUNCATE({operand_cells[0]})",
        "fpext": f"=FLOAT_EXTEND({operand_cells[0]})",

        # Control flow operators
        "br": f"=BRANCH({operand_cells[0]})",
        "ret": f"=RET({operand_cells[0]})",
        "switch": f"=SWITCH({operand_cells[0]})",

        # Other operators
        "phi": f"=PHI({operand_cells[0]}, {operand_cells[1]}, {operand_cells[2]})",
        "call": f"=CALL({operand_cells[0]}, {', '.join(operand_cells[1:])})",
        "select": f"=SELECT({operand_cells[0]}, {operand_cells[1]}, {operand_cells[2]})",
        "va_arg": f"=VAR_ARG({operand_cells[0]})",
        "unreachable": f"=UNREACHABLE()"
    }

    # Return the formula for the given opcode, if defined
    return operator_formulas.get(opcode, f"={opcode}({', '.join(operand_cells)})")
