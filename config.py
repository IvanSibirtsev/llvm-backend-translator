binary_operations = {
            "add", "fadd", "sub", "fsub", "mul", "fmul", "udiv", "sdiv", "urem", "srem", "frem"
        }

unary_operations = {"fneg"}

logic_operations = {"shl", "lshr", "ashr", "and", "or", "xor"}

other = {"icmp", "fcmp"}

LLVM_OPERATIONS = binary_operations\
    .union(unary_operations)\
    .union(logic_operations)\
    .union(other)

LLVM_TYPES = {"i1", "i32", "ptr"}

MEMORY_ACCESS = {"store", "load", "alloca"}

LLVM_TRANSFER = {"ret", "label", "call"}