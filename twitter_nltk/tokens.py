from nltk import *

text = "data/output.txt"
		
def token(text):
	with open(text, 'rb') as f:
		raw = f.read()
		tokens = word_tokenize(raw.decode('utf-8'))
		print tokens[0:20]
		return tokens

token(text)
# print tokens[0:20]