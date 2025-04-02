# Ask user for file names
input_file = input("Enter the file to read: ")
output_file = input("Enter the file to create: ")

try:
    # Open and read the input file
    with open(input_file, 'r') as f:
        text = f.read()
    
    # Make text uppercase (simple modification)
    new_text = text.upper()
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.write(new_text)
    
    print("File copied and modified successfully!")

except FileNotFoundError:
    print(f"Error: Could not find '{input_file}'")
except:
    print("An error occurred")