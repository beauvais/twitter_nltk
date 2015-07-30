from nltk import *
import pandas as pd

text = "data/output.txt"
output_file = "data/tokens.txt"

f = open(text, 'rb')
raw = f.read()
tokens = word_tokenize(raw.decode('utf-8'))
print tokens[0:20]


f.close()
