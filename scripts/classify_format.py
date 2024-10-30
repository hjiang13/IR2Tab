def classify_format(opcode):
    """
    Classifies the instruction format based on the opcode.
    """
    r_format_ops = [
        "add", "sub", "mul", "udiv", "sdiv", "urem", "srem", 
        "and", "or", "xor", "shl", "lshr", "ashr", "icmp", "fcmp",
        "fadd", "fsub", "fmul", "fdiv", "frem", "trunc", "zext", 
        "sext", "bitcast"
    ]
    
    i_format_ops = [
        "load", "store", "alloca", "getelementptr", "trunc", "zext", "sext",
        "fptrunc", "fpext", "uitofp", "sitofp", "fptoui", "fptosi", 
        "inttoptr", "ptrtoint", "phi", "select", "call", "va_arg", 
        "extractelement", "insertelement", "shufflevector", "atomicrmw", 
        "cmpxchg"
    ]
    
    j_format_ops = [
        "br", "switch", "ret", "unreachable", "indirectbr", 
        "invoke", "resume", "catchswitch", "catchpad", "cleanuppad"
    ]
    
    if opcode in r_format_ops:
        return "R"
    elif opcode in i_format_ops:
        return "I"
    elif opcode in j_format_ops:
        return "J"
    else:
        return "I"  # Default to I-format if unknown
