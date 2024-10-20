def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    if not numbers:
        return 0
    numbers.sort()
    n = len(numbers)
    midpoint = n // 2
    if n % 2 == 1:
        return numbers[midpoint]
    else:
        return (numbers[midpoint] + numbers[midpoint - 1]) / 2

def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = max(frequency.values())
    for num, count in frequency.items():
        if count == max_count:
            return num

def main():
    fileName = input("Enter the file name: ")

    with open(fileName, 'r') as f:
        numbers = []
        for line in f:
            words = line.split()
            for word in words:
                try:
                    numbers.append(float(word))
                except ValueError:
                    print(f"Warning: '{word}' is not a valid number and was ignored.")

    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))

if __name__ == "__main__":
    main()
