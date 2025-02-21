import pandas as pd
from nltk import ngrams
from collections import Counter

data = pd.read_csv('titledata.csv')


if 'Title' not in data.columns:
    raise ValueError("The 'Title' column does not exist in the titledata.csv file.")


titles = data['Title'].dropna().tolist()  


def generate_bigrams(titles):
    bigrams = []
    for title in titles:
        words = title.split()  
        bigrams.extend(list(ngrams(words, 2)))  
    return bigrams


bigrams = generate_bigrams(titles)


bigram_counts = Counter(bigrams)


bigram_df = pd.DataFrame(bigram_counts.items(), columns=['Bigram', 'Count'])


bigram_df.to_csv('bigram.csv', index=False)

print("Bigram data has been saved to bigram.csv successfully.")
