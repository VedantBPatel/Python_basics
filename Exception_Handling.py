#Python Exception
"""
When a program meets an error, it stops the execution of the rest of the program.
An error in python might be either an error in the syntax of an expression or a python exception.
->An exception in python is an event that disrupts the normal flow of the program execution.
->An object that describes an error is called exception.
->It allows to respond to the error instead of crashing the running program.
"""
#It consists of some blocks to handle:
#1. try block
"""
try block in python is used to write code that might raise an exception during execution.
The main purpose of try block is to test and monitor code for potential errors.
If an exception occurs within the try block, Python will skip the remaining code and executes the corresponding except block.
"""

#2.except block
"""
except block allows us to handle the error or exception occured in try block.
If an error occured in try block, Python jumps to except block and executes it.
"""

#3.else block
"""
else block is optional and if included, it must follow all exception blocks,
means it must come after all exception blocks.
It runs only when try block succeeds, means there is no error occured in try block.
"""

#4.finally block
"""
finally block will execute no matter what is the result.
"""

try:
    n=0
    res=100/n

except ZeroDivisionError:
    print("You can't divide by zero")

else:
    print("The result is:",res)

finally:
    print("Execution complete.")

#5.raise
"""
Raising an exception in Python is the act of triggering an error intentionally during the execution of a program.
This is useful when you want your program to stop and notify the user or developer of an issue, especially when if certain conditions are not met.
"""
def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Can't divide by zero")
    return a/b

try:
    print(divide(10,0))
except ZeroDivisionError as e:
    print(f"Error: {e}")

"""
#Types of Exception:
SyntaxError: This exception is raised when the interpreter encounters a syntax error in
the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.

> TypeError: This exception is raised when an operation or function is applied to an object
of the wrong type, such as adding a string to an integer.

> NameError: This exception is raised when a variable or function name is not found in
the current scope.

> IndexError: This exception is raised when an index is out of range for a list, tuple, or
other sequence types.

> KeyError: This exception is raised when a key is not found in a dictionary.

> ValueError: This exception is raised when a function or method is called with an invalid
argument or input, such as trying to convert a string to an integer when the string does
not represent a valid integer.

> AttributeError: This exception is raised when an attribute or method is not found on an
object, such as trying to access a non-existent attribute of a class instance.

> IOError: This exception is raised when an I/O operation, such as reading or writing a
file, fails due to an input/output error.

> ZeroDivisionError: This exception is raised when an attempt is made to divide a number
by zero.

> ImportError: This exception is raised when an import statement fails to find or load a
module.
"""