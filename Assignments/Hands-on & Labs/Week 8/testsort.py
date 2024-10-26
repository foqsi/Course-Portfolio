def isSorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def main():
    test_cases = [
        [],                      # Empty list
        [1],                     # Single element list
        [1, 2, 3, 4, 5],         # Sorted list
        [5, 4, 3, 2, 1],         # Reverse sorted list
        [1, 2, 2, 3, 4],         # Sorted list with duplicates
        [1, 3, 2, 4, 5],         # Unsorted list
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"Test case {i + 1}: {test_case} -> {isSorted(test_case)}")

if __name__ == "__main__":
    main()
