import pandas as pd
from collections import Counter
import re


csv_file = 'data4.csv'  
df = pd.read_csv(csv_file)

full_text = ' '.join(df.astype(str).apply(lambda x: ' '.join(x), axis=1))


# Unicode range for Bangla: \u0980-\u09FF
bangla_words = re.findall(r'[\u0980-\u09FF]+', full_text)

word_count = Counter(bangla_words)


word_count_df = pd.DataFrame(word_count.items(), columns=['Word', 'Count'])
output_file = 'unigram.csv'
word_count_df.to_csv(output_file, index=False)


