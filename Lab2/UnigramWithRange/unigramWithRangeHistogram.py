import pandas as pd
import sys
import matplotlib.pyplot as plt

sys.stdout.reconfigure(encoding='utf-8')


plt.rcParams['font.family'] = 'kalpurush'


def read_unigram_csv(file_name):
    df = pd.read_csv(file_name) 
    unigram_dict = dict(zip(df['Word'], df['Frequency']))  
    return unigram_dict


def plot_histogram(unigram_dict):
    words = list(unigram_dict.keys())
    counts = list(unigram_dict.values())
    plt.figure(figsize=(12, 8))  
    plt.bar(words, counts, color='skyblue')  
    plt.title("Unigrams by Frequency", fontsize=16)
    plt.xlabel("Words", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.xticks(rotation=45, ha='right')  
    plt.tight_layout() 
    plt.show()  


def main():
    file_name = 'unigramWithRange.csv'  
    unigram_dict = read_unigram_csv(file_name)  
    plot_histogram(unigram_dict)  


if __name__ == "__main__":
    main()
# import pandas as pd
# import sys
# import matplotlib.pyplot as plt


# sys.stdout.reconfigure(encoding='utf-8')


# plt.rcParams['font.family'] = 'kalpurush'


# def read_unigram_csv(file_name):
#     df = pd.read_csv(file_name) 
#     unigram_dict = dict(zip(df['Word'], df['Frequency']))  
#     return unigram_dict


# def plot_histogram(unigram_dict, top_n=100):
#     sorted_unigrams = sorted(unigram_dict.items(), key=lambda item: item[1], reverse=True)[:top_n]
#     words, counts = zip(*sorted_unigrams) 
#     plt.figure(figsize=(6, 5)) 
#     plt.bar(words, counts, color='skyblue') 
#     plt.title(f"Top {top_n} Unigrams by Frequency", fontsize=14)
#     plt.xlabel("Words", fontsize=12)
#     plt.ylabel("Frequency", fontsize=12)
#     plt.xticks(rotation=45, ha='right')  
#     plt.tight_layout()  
#     plt.show()  


# def main():
#     file_name = 'range.csv' 
#     unigram_dict = read_unigram_csv(file_name)  
#     plot_histogram(unigram_dict, top_n=100)  

# # Entry point of the script
# if __name__ == "__main__":
#     main()
