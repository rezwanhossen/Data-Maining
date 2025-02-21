
import pandas as pd


data = pd.read_csv('title.csv')


bengali_chars = ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ', 
                 'ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ', 'জ', 'ঝ', 'ঞ', 
                 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 
                 'প', 'ফ', 'ব', 'ভ', 'ম', 'য', '়', '০', '১', '২', 
                 '৩', '৪', '৫', '৬', '৭', '৮', '৯']


alphabet_list = []


for title in data['title']:  
    if isinstance(title, str):  
        for word in title.split():  
            for char in word:  
                if char in bengali_chars:  
                    alphabet_list.append(char)

char_count = pd.Series(alphabet_list).value_counts()


alphabet_df = pd.DataFrame({'Character': char_count.index, 'Count': char_count.values})


alphabet_df.to_csv('alphabetlista.csv', index=False)

print(alphabet_df)
