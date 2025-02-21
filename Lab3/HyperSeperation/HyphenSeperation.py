import pandas as pd
import re
from collections import Counter


def generate_hyphenated_variations(word):
    variations = []
    for i in range(1, len(word)):
        variations.append(word[:i] + '-' + word[i:])
    return variations


def categorize_words(input_word, valid_words_set):
    correct_unigrams = []
    outlier_unigrams = []

    #  original word
    if input_word in valid_words_set:
        correct_unigrams.append(input_word)

    # Generate hyphenated
    hyphenated_variations = generate_hyphenated_variations(input_word)
    
    for variation in hyphenated_variations:
        if '-' in variation:  
            left, right = variation.split('-')

            # Check left part
            if left in valid_words_set:
                correct_unigrams.append(left)
            else:
                outlier_unigrams.append(left)

            # Check right part
            if right in valid_words_set:
                correct_unigrams.append(right)
            else:
                outlier_unigrams.append(right)

    return list(set(correct_unigrams)), list(set(outlier_unigrams))

# Load valid words from a text file
def load_valid_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return set(word.strip() for word in f.readlines() if word.strip())

# Process the CSV file
def process_csv(file_path, valid_words_set):
    df = pd.read_csv(file_path, encoding='utf-8')
    correct_unigrams = []
    outlier_unigrams = []

    # Iterate through each cell in the DataFrame
    for column in df.columns:
        for value in df[column].astype(str):
            # Extract Bengali words only
            words = re.findall(r'[\u0980-\u09FF]+', value)  # Find Bengali words
            for word in words:
                cleaned_word = word.strip()
                if cleaned_word:  # Avoid empty tokens
                    c_unigrams, o_unigrams = categorize_words(cleaned_word, valid_words_set)
                    correct_unigrams.extend(c_unigrams)
                    outlier_unigrams.extend(o_unigrams)

    return correct_unigrams, outlier_unigrams

# Example usage
valid_words_file = 'D:/DataMaining/lab3/HyphenSeperation/words.txt'  # Path to your valid words file
csv_file = 'D:/DataMaining/lab3/HyphenSeperation/sort_file.csv'  # Path to your CSV file
valid_words_set = load_valid_words(valid_words_file)

correct_unigrams, outlier_unigrams = process_csv(csv_file, valid_words_set)

# Count occurrences
correct_counts = Counter(correct_unigrams)
outlier_counts = Counter(outlier_unigrams)

# Save the correct unigrams to a text file
with open('correct_unigrams.txt', 'w', encoding='utf-8') as f:
    for unigram, count in correct_counts.items():
        f.write(f"{unigram} - Frequency: {count}\n")

# Save the outlier unigrams to another text file
with open('outlier_unigrams.txt', 'w', encoding='utf-8') as f:
    for unigram, count in outlier_counts.items():
        f.write(f"{unigram} - Frequency: {count}\n")

print("FILE SAVED COMPLETLY")
