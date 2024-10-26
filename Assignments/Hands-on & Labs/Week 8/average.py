def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [float(line.strip()) for line in file]

def calculate_average(numbers):
    if not numbers:
        return 0
    sum_of_numbers = sum(numbers)
    count_of_numbers = len(numbers)
    return sum_of_numbers / count_of_numbers

def main():
    filename = input("Enter filename to find average of numbers: ")
    try:
        numbers = read_numbers_from_file(filename)
        average = calculate_average(numbers)
        print(f"The average of the numbers in the file '{filename}' is {average}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

if __name__ == "__main__":
    main()
