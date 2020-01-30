from collections import Counter
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download(['punkt', 'stopwords', 'wordnet'])

def compute_word_counts(messages, load=True, filepath='counts.npz'):
    '''
    INPUT:
        messages - (list) List of messages to compute top words from
        load - (bool) By default true. If false will generate word counts
        filepath - (string) File path to save or load data

    OUTPUT:
        top_words - (list) Top words
        top_counts - (list) Top word counts

    '''
    if load:
        # load arrays
        data = np.load(filepath)
        return list(data['top_words']), list(data['top_counts'])
    else:
        # get top words
        counter = Counter()
        for message in messages:
            tokens = tokenize(message)
            for token in tokens:
                counter[token] += 1
        # top 20 words
        top = counter.most_common(20)
        top_words = [word[0] for word in top]
        top_counts = [count[1] for count in top]
        # save arrays
        np.savez(filepath, top_words=top_words, top_counts=top_counts)
        return list(top_words), list(top_counts)

def tokenize(text):
    '''
    INPUT:
    text - (str) Takes text and standardizes it

    OUTPUT:
    tokens - (list) Tokenized text
    '''
    lower_text = text.lower()
    tokens = word_tokenize(lower_text)
    lemmatizer = WordNetLemmatizer()
    tokens = [words for words in tokens if words not in stopwords.words("english")]
    for element in tokens:
        lemmatizer.lemmatize(element)
    return tokens

if __name__ == '__main__':
    pass
