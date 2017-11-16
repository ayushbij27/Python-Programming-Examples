#  Train a word2vec model by getting the contents from wikipedia on the basis of search performed.

import wikipedia
import os
import sys
from gensim.models import Word2Vec
from wikipedia import search, page
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

page = wikipedia.page('machine learning')

print page.content		
sentences = [word_tokenize(sent) for sent in sent_tokenize(page.content)]
stop_words = set(stopwords.words('english'))
filtered_sentence_words=[]
flat_list=[item for sublist in sentences for item in sublist]
flat_list= [token.lower() for token in flat_list]
filtered_sentence_words = [w for w in flat_list if not w in stop_words]	
print filtered_sentence_words
#print sentences[0]

model = Word2Vec(sentences, min_count=2, size=50, window=10)
vocab = list(model.wv.vocab.keys())[:10]
print vocab
print('***************************************************************************************')
print vocab[:10]
print('***************************************************************************************')
print model['results']
print('***************************************************************************************')
print model.most_similar('results')
print('***************************************************************************************')
