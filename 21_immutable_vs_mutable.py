
# ---------------------------------------------------
# 🔹 Immutable vs Mutable in Python
# ---------------------------------------------------
# 🧩 Immutable Objects:
#   - Cannot be changed after creation.
#   - Examples: int, float, str, tuple, frozenset, bool
#   - Any modification creates a new object in memory.
#
# 🧩 Mutable Objects:
#   - Can be changed after creation.
#   - Examples: list, dict, set, bytearray
#   - Modifications happen in-place, and the memory address stays the same.
# ---------------------------------------------------

# ASCII Diagram of Memory Working
#
# Immutable (int, str, tuple, etc.)
# 
#     +-----------+        x = 10
#     |   10      |  <---+
#     +-----------+      |
#                         |
#                    +----v----+
#                    |   x     |
#                    +---------+
#
# Change x = 20
#     +-----------+        x = 20 (New object)
#     |   20      |  <---+
#     +-----------+      |
#                         |
#                    +----v----+
#                    |   x     |
#                    +---------+
#
# Mutable (list, dict, set, etc.)
#
#     +---------------------------+
#     | [10, 20, 30]              |  <---+
#     +---------------------------+      |
#                                        |
#                                  +-----v-----+
#                                  |    mylist  |
#                                  +-----------+
#
# Modify mylist[0] = 100 → Same memory updated
#
#     +---------------------------+
#     | [100, 20, 30]             |
#     +---------------------------+
#

# ---------------------------------------------------
# 🔹 Code Examples
# ---------------------------------------------------

# Example of Immutable
x = 10
print(f"Original x: {x}, Memory ID: {id(x)}")
x = 20
print(f"New x: {x}, Memory ID: {id(x)}")  # Different memory ID

# Example of Mutable
my_list = [10, 20, 30]
print(f"\nOriginal List: {my_list}, Memory ID: {id(my_list)}")
my_list[0] = 100
print(f"Modified List: {my_list}, Memory ID: {id(my_list)}")  # Same memory ID
