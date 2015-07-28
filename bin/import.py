#! /usr/bin/python

from sys import argv
import pandas as pd

script, filename, output_file = argv

pd.set_option('display.max_colwidth', -1)
df = pd.read_csv(filename, header=0)
df['text'].to_csv(output_file, index=False, header=False)


