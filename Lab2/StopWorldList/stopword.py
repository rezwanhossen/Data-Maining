import pandas as pd


data = pd.read_csv('titledata.csv')


if 'Title' not in data.columns:
    raise ValueError("The 'Title' column does not exist in the titledata.csv file.")

titles = data['Title'].dropna().tolist()


stop_words = set([
    "আমি", "তুমি", "সে", "আমাদের", "আপনার", "তারা", "এটি", "ও", "এবং", "কিন্তু",
    "বা", "যদি", "যে", "যেমন", "এক", "দুই", "তিন", "চার", "পাঁচ", "এই", "সেখানে",
    "সাথে", "মধ্যে", "দ্বারা", "পর্যন্ত", "আবার", "তার", "তাদের", "করে", "করছি",
    "একজন", "অনেক", "কিছু", "কারা", "কোথায়", "কেন", "কখন", "কিভাবে", "কি", "সকল",
    "সব", "কেউ", "নই", "না", "অথবা", "তাহলে", "তবে", "যখন", "যদি", "যত", "উপরে",
    "নিচে", "পাশে", "আগে", "পরে", "এখনও", "ভালো", "যদিও", "আসলে", "বেশ", "মাত্র",
    "শুধুমাত্র"
])


filtered_titles = []
for title in titles:
    words = title.split()
    filtered_title = [word for word in words if word not in stop_words]
    filtered_titles.append(' '.join(filtered_title))

filtered_df = pd.DataFrame(filtered_titles, columns=['Filtered_Title'])
filtered_df.to_csv('stopWordList.csv', index=False)

print("Filtered titles have been saved to filtered_titles.csv successfully.")
