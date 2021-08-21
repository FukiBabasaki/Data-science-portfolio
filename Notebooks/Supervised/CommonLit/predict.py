import pickle
import os
import pandas as pd


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

def stem_sentence(sentence):
    """ Given a sentence,
    modify each word in the sentence to stemmed word.
    """
    porter = PorterStemmer()
    words = word_tokenize(sentence)
    stemmed_words = []

    for word in words:
        stemmed_words.append(porter.stem(word))
        stemmed_words.append(" ")

    return "".join(stemmed_words)

def stem_paragraph(paragraph):
    """ Given a paragraph
    return a paragraph whose word is stemmed.
    """
    stemmed_sentence = []
    for sentence in paragraph.split("\n"):
        stemmed = stem_sentence(sentence)
        stemmed_sentence.append(stemmed)
        stemmed_sentence.append("\n")

    return "".join(stemmed_sentence)

def stem_dataset(dataset):
    # Stem all paragraphs in the dataset
    dataset_copy = dataset.copy()
    
    for index, row in dataset_copy.iterrows():
        dataset_copy.loc[index, 'clean_excerpt'] = stem_paragraph(row['excerpt'])

    return dataset_copy


from sklearn.feature_extraction.text import TfidfVectorizer

def get_X(clean_data):
    vectorizer = TfidfVectorizer(lowercase=True,token_pattern=r'(?u)\b[A-Za-z]+\b',stop_words='english',max_features=2000,strip_accents='unicode')
    vectorizer.fit(clean_data['clean_excerpt'].values)

    X = pd.DataFrame(columns= range(0, 2000))

    for index, row in clean_data.iterrows():
        numbers = vectorizer.transform(clean_data['clean_excerpt'][[index]])
        X = X.append(pd.DataFrame(numbers.toarray()))

    return X


with open("models/xgb_final.sav", "rb") as f:
    model = pickle.load(f)

df = pd.read_csv("dataset/web_scraped.csv")

X = get_X(stem_dataset(df))
y = model.predict(X)

results = pd.DataFrame(y, columns=['predicted'])
output = df.join(results)

output.to_csv("dataset/pred_web.csv", index=False)