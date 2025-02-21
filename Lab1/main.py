import pandas as pd
data_1 = pd.read_csv('Dataset1.csv',encoding="utf-8-SIG")
data_2 = pd.read_csv('Dataset2.csv',encoding='utf-8-SIG')
data3 = pd.merge(data_1, data_2, how='outer')
desired_columns = ['Title', 'Body', 'Source', 'Category', 'Time', 'ReportedBy']
data3_reordered = data3[desired_columns]
data3_sorted = data3_reordered.sort_values(by='Category')
data3_sorted.to_csv('integrated_dataset.csv', index=False,encoding="utf-8-SIG")

