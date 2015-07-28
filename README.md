# twitter_nltk

This is a project where I'll be putting in my scripts and ideas for using [nltk][1] to analyse data.

To start with, I'll be using my twitter archive as a corpus. [You can read how request and download your own twitter archive here.][2]


## Import

Twitter archives look like this:

* /css
* /data
* /img
* index.html
* /js
* /lib
* README.txt
* tweets.csv

They present you with a self-contained website, which you can browse simply by opening index.html in your browser.

The archive of tweets themselves live in *tweets.csv*.

In this project, /twitter_nltk contains *import.py*. It's a simple script, which uses pandas to grab the actual text of your tweets, and output into a txt file.



[1]: http://www.nltk.org/
[2]: https://support.twitter.com/articles/20170160#