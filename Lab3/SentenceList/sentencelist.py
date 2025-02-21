import pandas as pd
data = pd.read_csv('body.csv')

sentences = []
for text in data['Body']: 
    if isinstance(text, str):  
        split_sentences = text.split('।')      
        for i, sentence in enumerate(split_sentences, 1):
            sentence = sentence.strip()  
            if sentence:  
                sentences.append(f"{i}. {sentence}।")  


sentence_df = pd.DataFrame(sentences, columns=['Sentences'])


sentence_df.to_csv('sentencelist.csv', index=False)

print("sentencelist.csv file is updated with numbered sentences.")
