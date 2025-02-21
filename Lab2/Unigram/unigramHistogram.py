import pandas as pd
import sys
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')


plt.rcParams['font.family'] = 'kalpurush'


def read_unigram_csv(file_name):
    df = pd.read_csv(file_name)  
    unigram_dict = dict(zip(df['Word'], df['Count']))  
    return unigram_dict


def plot_histogram(unigram_dict, top_n=15):
    sorted_unigrams = sorted(unigram_dict.items(), key=lambda item: item[1], reverse=True)[:top_n]
    words, counts = zip(*sorted_unigrams)  
    plt.figure(figsize=(8, 6)) 
    plt.bar(words, counts, color='skyblue')  
    plt.title(f"Top {top_n} Unigrams by Frequency", fontsize=14)
    plt.xlabel("Words", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45, ha='right')  #
    plt.tight_layout()  
    plt.show()  

def main():
    file_name = 'unigram.csv'  
    unigram_dict = read_unigram_csv(file_name)  
    plot_histogram(unigram_dict, top_n=15)  

if __name__ == "__main__":
    main()
