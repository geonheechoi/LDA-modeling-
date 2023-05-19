import pandas as pd
from konlpy.tag import Okt
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
import re

# Load the CSV file into a Pandas dataframe
df = pd.read_csv('all_titles.csv',error_bad_lines=False, encoding='utf-8')
#print(df.head())

# Prepare the data for LDA modeling
text_data = df['title'].reset_index(drop=True)

#plt.bar(range(len(text_data)),text_data)
#print(text_data)
text_data = [str(doc) for doc in text_data]
# Define regex pattern to match non-alphanumeric characters
pattern = r'[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]'

# Remove special characters from each document in the text data
text_data = [re.sub(pattern, '', doc)  for doc in text_data]

# Tokenize the text da
okt = Okt()
word_lists = [okt.morphs(doc) for doc in text_data]
#print(word_lists)
# Create a dictionary of the words
dictionary = Dictionary(word_lists)

# Convert the word lists into a bag-of-words representation
corpus = [dictionary.doc2bow(word_list) for word_list in word_lists]
# plt.bar(range(len(text_data)),text_data)
# plt.topic('topic label')
# plt.title('Topic modeling bar chart')
# plt.show()
# plt.xlabel('X-axis label')
# plt.ylabel('Y-axis label')
# plt.title('Example bar chart')
# plt.show()
# Train the LDA model
num_topics = 20
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics)

# Show the topics generated by the model
for idx, topic in lda_model.print_topics(-1):
    print("Topic: {} \nWords: {}".format(idx, topic))
    #plt.show()