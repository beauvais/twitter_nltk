#! /usr/bin/python

from sys import argv
import pandas as pd

# We use pandas for reading and writing your csv file to a text file.

script, filename, output_file = argv

# Input your csv file (which, when using the twitter archive is 'tweets.csv') 
# when calling the script. Choose your output file name at the same time.

def import_text(filename):
	pd.set_option('display.max_colwidth', -1)
	df = pd.read_csv(filename, header=0)
	df['text'].to_csv(output_file, index=False, header=False)

import_text(filename)

# We set turn off pandas' column width, because it will truncate rows if not.
# This simply uses pandas' 'to_csv', opting not to include the index or 
# header.