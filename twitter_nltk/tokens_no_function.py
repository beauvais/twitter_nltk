from nltk import *
import pandas as pd

start_file = "data/output.txt"
token_file = "data/tokens.txt"
word_file = "data/words.txt"
text_file = "data/text.txt"

f = open(start_file, 'rb')
raw = f.read()
tokens = wordpunct_tokenize(raw.decode('utf-8'))
print tokens[0:20]

words = [w.lower() for w in tokens]
text = Text(tokens)

token_out = open(token_file.decode('utf-8'), 'w')
for item in tokens:
	print>>token_out, tokens

words_out = open(word_file.decode('utf-8'),'w')
for item in words:
	print>>words_out, words

text_out = open(text_file.decode('utf-8'),'w')
for item in text:
	print>>text_out, text

f.close()
token_out.close()
words_out.close()
text_out.close()
