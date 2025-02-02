# main.py
from pass1 import pass1  # Corrected import statement
from pass2 import pass2  # Corrected import statement
from test_assembler import assembly_code  # Removed unnecessary import

def create_txt(assembly_code, symbol_table, object_code):
    # Open or create a text file in write mode
    with open("assembler_output.txt", "a") as file:
        # Write sample assembly code
        file.write("Random Assembly Code: \n")
        for i, line in enumerate(assembly_code, 1):
            file.write(f"{i}. {line}\n")
        
        # Write symbol table
        file.write("\nSymbol Table: \n")
        for label, location in symbol_table.items():  # Corrected variable name
            file.write(f"- {label}: {location}\n")
        
        # Write object code
        file.write("\nObject Code:\n")
        for i, code in enumerate(object_code, 1):
            file.write(f"{i}. {code}\n")
        
        file.write("Nowe -----------------------------------------\n")  # Corrected typo

# Run Pass 1 to build the symbol table
symbol_table = pass1(assembly_code)
# Run Pass 2 to generate object code
object_code = pass2(assembly_code, symbol_table)
# Create text file with assembly code, symbol table, and object code
create_txt(assembly_code, symbol_table, object_code)

# Display the symbol table
print("\nSymbol Table:")
for label, location in symbol_table.items():  # Corrected variable name
    print(f"- {label}: {location}")
