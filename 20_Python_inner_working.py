# ---------------------------------------------------
# Python Code Execution Flow
# ---------------------------------------------------
# 1) Python code is written by the programmer.
# 2) Python code is compiled into Bytecode (.pyc files).
# 3) The Bytecode is executed by the Python Virtual Machine (PVM).
# 4) The PVM executes the instructions and returns the result.
# 5) compile to byte code ==> low level and python Independent
# 6) Python Virtual Machine (PVM) ==> execute the byte code
# 7) byte code run faster than python code
# 8) pyc file is stored in __pycache__ folder ====> Frozen Binaries
# 8) byte code is not machine code
# 
# Note:
# - Python uses an interpreter to execute code line by line.
# - The interpreter reads the code, compiles it to bytecode, and executes it.
# - Bytecode is a low-level, platform-independent representation of your code.
# ---------------------------------------------------

# ASCII Diagram of Python Execution Flow:
# 
#    +---------------------+         +------------------+         +------------------------+         +-----------------+
#    |  Python Source Code |  --->   |  Python Compiler |  --->   |    Bytecode (.pyc)     |  --->   | Python VM (PVM) |
#    +---------------------+         +------------------+         +------------------------+         +-----------------+
#                                                                                                          |
#                                                                                                          v
#                                                                                                    +-----------+
#                                                                                                    |  Result   |
#                                                                                                    +-----------+

# Example Code to See Execution
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Running the function
if __name__ == "__main__":
    result = add_numbers(10, 5)
    print(f"Result: {result}")
