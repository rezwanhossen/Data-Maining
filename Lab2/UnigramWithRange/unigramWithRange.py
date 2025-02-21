

import csv


def read_unigram_from_csv(file_path):
    unigram_data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            if len(row) == 2:  
                word = row[0]         
                frequency = int(row[1])  
                unigram_data.append((word, frequency))
    return unigram_data

def filter_unigrams_by_frequency(unigram_data, min_count, max_count):
    return [(word, freq) for word, freq in unigram_data if min_count <= freq <= max_count]


def save_filtered_unigrams_to_csv(filtered_unigrams, output_file_path):
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Word', 'Frequency'])  
        writer.writerows(filtered_unigrams)  


file_path = 'unigram.csv'  
output_file_path = 'unigramWithRange.csv'  


unigram_data = read_unigram_from_csv(file_path)


min_count = int(input("min range : "))
max_count = int(input("max range : "))


filtered_unigrams = filter_unigrams_by_frequency(unigram_data, min_count, max_count)


if filtered_unigrams:
    print("নির্ধারিত রেঞ্জের মধ্যে আসা ইউনিগ্রাম:")
    for word, freq in filtered_unigrams:
        print(f"{word} ,{freq}")

   
    save_filtered_unigrams_to_csv(filtered_unigrams, output_file_path)
    print(f"unifram filtering '{output_file_path}' save file")
else:
    print("There are no unigrams within the specified range.")
