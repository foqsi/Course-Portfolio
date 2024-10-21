import string

def remove_punctuation_and_digits(text):
    """
    Removes punctuation and digits from the input text.
    """
    for char in string.punctuation + string.digits:
        text = text.replace(char, '')
    return text

def get_word_pairs(words):
    """
    Creates a dictionary of word pairs and how often they appear.
    """
    pairs = {}
    for i in range(len(words) - 1):
        pair = (words[i], words[i + 1])
        if pair in pairs:
            pairs[pair] += 1
        else:
            pairs[pair] = 1
    return pairs

def main():
    input_file_name = input("Enter the name of the file: ")

    try:
        # Open the file and read lines
        input_file = open(input_file_name, 'r', encoding='utf-8') 
        lines = input_file.readlines()
        input_file.close()

        # Create the output file
        output_file_name = "Analysis-" + input_file_name
        output_file = open(output_file_name, 'w')

        # Initialize counts
        total_lines = 0
        total_words = 0
        total_characters = 0
        all_words = []

        # Go through each line in the file
        for line in lines:
            total_lines += 1
            total_characters += len(line)
            clean_line = remove_punctuation_and_digits(line).lower()
            words = clean_line.split()

            total_words += len(words)
            all_words.extend(words)

        # Count word frequencies
        word_frequencies = {}
        for word in all_words:
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1

        # Get two-word pairs
        word_pairs = get_word_pairs(all_words)
        repeated_pairs = {}
        for pair, count in word_pairs.items():
            if count > 1:
                repeated_pairs[pair] = count

        # Calculate average word lengths
        total_unique_words = len(word_frequencies)
        total_word_pairs = len(repeated_pairs)

        if total_words > 0:
            average_word_length = sum(len(word) for word in all_words) / total_words
        else:
            average_word_length = 0

        if total_unique_words > 0:
            average_unique_word_length = sum(len(word) for word in word_frequencies) / total_unique_words
        else:
            average_unique_word_length = 0

        # Write basic statistics to the output file
        output_file.write(f"Number of lines: {total_lines}\n")
        output_file.write(f"Number of words: {total_words}\n")
        output_file.write(f"Number of characters: {total_characters}\n\n")

        # Write unique word frequencies
        output_file.write("Unique words (frequency count):\n")
        for word, count in sorted(word_frequencies.items()):
            output_file.write(f"{word}: {count}\n")

        # Write repeated word pairs
        output_file.write("\nRepeated word pairs (frequency count):\n")
        for pair, count in repeated_pairs.items():
            output_file.write(f"{pair[0]} {pair[1]}: {count}\n")

        # Write final summary statistics
        output_file.write("\nSummary statistics:\n")
        output_file.write(f"Total number of words: {total_words}\n")
        output_file.write(f"Average length of a word: {average_word_length:.2f}\n")
        output_file.write(f"Number of unique words: {total_unique_words}\n")
        output_file.write(f"Average number of letters in unique words: {average_unique_word_length:.2f}\n")
        output_file.write(f"Number of word pairs with frequencies of 2 or more: {total_word_pairs}\n")

        output_file.close()

        # Display basic stats and summary statistics on the screen
        print(f"Number of lines: {total_lines}")
        print(f"Number of words: {total_words}")
        print(f"Number of characters: {total_characters}\n")
        print("\nRepeated word pairs (frequency count):")
        for pair, count in repeated_pairs.items():
            print(f"{pair[0]} {pair[1]}: {count}")

        print("\nSummary statistics:")
        print(f"Total number of words: {total_words}")
        print(f"Average length of a word: {average_word_length:.2f}")
        print(f"Number of unique words: {total_unique_words}")
        print(f"Average number of letters in unique words: {average_unique_word_length:.2f}")
        print(f"Number of word pairs with frequencies of 2 or more: {total_word_pairs}")

    except FileNotFoundError:
        print(f"Sorry, the file '{input_file_name}' was not found.")

if __name__ == "__main__":
    main()
