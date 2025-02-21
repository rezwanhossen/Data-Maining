import pandas as pd
from collections import Counter


data = pd.read_csv('titledata.csv')


if 'Title' not in data.columns:
    raise ValueError("The 'Title' column does not exist in the titledata.csv file.")


titles = data['Title'].dropna().tolist()


all_words = []
for title in titles:
    all_words.extend(title.split())


word_counts = Counter(all_words)


hapax_legomena = {word: count for word, count in word_counts.items() if count == 1}


hapax_df = pd.DataFrame(hapax_legomena.items(), columns=['Word', 'Count'])


hapax_df.to_csv('hapaxlegomenon.csv', index=False)

print("Hapax legomena has been saved to hapax.csv successfully.")
