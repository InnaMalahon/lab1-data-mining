import pandas as pd
import string
from matplotlib import pyplot as plt
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
import numpy as np

df = pd.read_csv("sms-spam-corpus.csv")

# видалити цифри і спеціальні символи, привести до єдиного регістру
df['v2'] = df['v2'].str.lower().str.replace(r'[^A-Za-z\']+', ' ')
df['v2'] = df['v2'].str.replace(r'[\']+', '')

# deleting empty columns
df.dropna(axis=1, how='any', inplace=True)

# прибрати стоп.слова
stop_words = stopwords.words('english') + ['u']
#print(stopwords.words('english'))
df['v2'] = df['v2'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))

df.to_csv('sms-spam-corpus.csv', encoding='utf-8')

ham = df[df.v1 == "ham"]
spam = df[df.v1 == "spam"]

# Створити словник слів для кожної з двох категорій
# Формат: Слово - скільки разів зустрічається в категорії. Зберегти в окремі файли

ham_words = ham['v2']
spam_words = spam['v2']

spam_words_number = spam_words.str.split().map(len).sum()
#print(spam_words_number)    # 11506
ham_words_number = ham_words.str.split().map(len).sum()
#print(ham_words_number)    # 38570
#print(spam_words)  # 747

spam_words = spam_words.split(" ")
#spam_words.sort()
print(spam_words)

def get_spam_words_dict(spam_words):
    spam_words_dict = dict()
    for word in spam_words:
        if word in spam_words_dict:
            spam_words_dict[word] = spam_words_dict[word] + 1
        else:
            spam_words_dict[word] = 1
    return spam_words_dict

#print(get_spam_words_dict(spam_words))