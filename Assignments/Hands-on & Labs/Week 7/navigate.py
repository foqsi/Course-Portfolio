def navigate_file():
    fileName = input("Enter the file name: ")

    try:
        with open(fileName, 'r') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        
        while True:
            print(f"\nThe file contains {total_lines} lines.")
            
            try:
                line_number = int(input(f"Enter a line number (1 to {total_lines}, or 0 to quit): "))
                
                if line_number == 0:
                    print("Quitting the program.")
                    break
                
                if 1 <= line_number <= total_lines:
                    print(f"Line {line_number}: {lines[line_number - 1].strip()}")
                else:
                    print(f"Invalid line number. Please enter a number between 1 and {total_lines}.")
            
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    except FileNotFoundError:
        print(f"Error: The file '{fileName}' was not found.")

if __name__ == "__main__":
    navigate_file()
