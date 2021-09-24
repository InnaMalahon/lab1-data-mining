import pandas as pd
import string
from matplotlib import pyplot as plt
import nltk.corpus
nltk.download('stopwords')
from nltk.corpus import stopwords
import numpy as np
from collections import Counter
import csv

df = pd.read_csv("sms-spam-corpus.csv")
"""
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
"""
ham = df[df.v1 == "ham"]
spam = df[df.v1 == "spam"]

# Створити словник слів для кожної з двох категорій
# Формат: Слово - скільки разів зустрічається в категорії. Зберегти в окремі файли

spam_words = spam['v2']
spam_words_list: list = spam['v2'].to_list()

spam_words_list = ' '.join(spam_words_list)
#print(spam_words_list)
"""
spam_counts = Counter(spam_words_list.split())


a_file = open("spam-words-dictionary.csv", "w")
writer = csv.writer(a_file)
writer.writerow(['word', 'frequency'])
for key, value in dict(spam_counts).items():
    writer.writerow([key, value])
a_file.close()
"""
ham_words = ham['v2']
ham_words_list: list = ham['v2'].to_list()
"""
ham_words_list = ' '.join(ham_words_list)
ham_counts = Counter(ham_words_list.split())

a_file = open("ham-words-dictionary.csv", "w")
writer = csv.writer(a_file)
writer.writerow(['word', 'frequency'])
for key, value in dict(ham_counts).items():
    writer.writerow([key, value])
a_file.close()
"""

# 1 - Вивести на графіках розподіл по довжині слів для кожної категорії і середню довжину слів
# 1) визначити довжину всіх слів
# 2) підрахувати к-ть знаків (list/dict)
# 3) знайти середню довжину

spam_df = pd.read_csv("output/spam-words-dictionary.csv")      #full file
spam_words_length_dict = {}
spam_df_list = spam_df['word'].to_list()     # 'word' column in list
spam_words_length = [0]  # empty list for length values

for i in range(0, len(spam_df_list)):
    spam_words_length.insert(i, len(spam_df_list[i]))

spam_words_length_counts = Counter(spam_words_length)
spam_words_length_frequency = [0]

for i in range(0, len(spam_words_length_counts)):
    spam_words_length_frequency.insert(i, spam_words_length_counts[i]/len(spam_words_length_counts))
#print(spam_words_length_frequency)
average_spam_length = sum(spam_words_length) / len(spam_words_length)
###
ham_df = pd.read_csv("output/ham-words-dictionary.csv")      #full file
ham_words_length_dict = {}
ham_df_list = ham_df['word'].to_list()     # 'word' column in list
ham_words_length = [0]  # empty list for length values

for i in range(0, len(ham_df_list)):
    ham_words_length.insert(i, len(str(ham_df_list[i])))

ham_words_length_counts = Counter(ham_words_length)
ham_words_length_frequency = ham_words_length_counts
average_ham_length = sum(ham_words_length) / len(ham_words_length)
##################################################################
plt.xlabel('Words length')
plt.ylabel('Frequency')
plt.title('Histogram of words length frequency')
plt.bar(range(len(dict(spam_words_length_counts))), list(dict(spam_words_length_counts).values()))
plt.xticks(range(len(dict(spam_words_length_counts))), list(dict(spam_words_length_counts).keys()))
#plt.show()

#print()

# 2 - Вивести на графіках розподіл по довжині повідомлень для кожної категорії і середню довжину повідомлення
### spam_words_list: list = spam['v2'].to_list()
spam_sms_length = [0]   # empty list for length values

for i in range(0, len(spam_words_list)):
    spam_sms_length.insert(i, len(str(spam_words_list[i])))
spam_sms_length_counts = Counter(spam_sms_length)
average_spam_sms_length = sum(spam_sms_length) / len(spam_sms_length)
#print(len(spam_words_list)) # 747 sms
#
ham_sms_length = [0]   # empty list for length values

for i in range(0, len(ham_words_list)):
    ham_sms_length.insert(i, len(str(ham_words_list[i])))
ham_sms_length_counts = Counter(ham_sms_length)
#print(ham_sms_length_counts)
average_ham_sms_length = sum(ham_sms_length) / len(ham_sms_length)
#print(average_ham_sms_length)

# 3 - Вивести на графіках 20 слів, які зустрічаються найчастіше для кожної категорії окремо
spam_frequent_words_list = spam_df.sort_values(by='frequency', ascending=False).head(20)
spam_frequent_words_list_freq = spam_frequent_words_list['frequency']/len(spam_words_list)
print(spam_frequent_words_list['frequency']/len(spam_words_list))

ham_frequent_words_list = ham_df.sort_values(by='frequency', ascending=False).head(20)
#print(ham_frequent_words_list)

plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Histogram of 20 most frequent words')
plt.bar((spam_frequent_words_list['frequency']), spam_frequent_words_list_freq)
plt.xticks((spam_frequent_words_list['frequency']), spam_frequent_words_list_freq)
#plt.show()

"""

"""

