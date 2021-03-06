"""#Building an Automated News Summarizer
website: https://www.vox.com/

Text summarization has two parts extraction and abstraction.

gensim lib. - Its implementation is based on "TextRank algorithm" ,its a graph based ranking modl for text processing.
"""

pip install gensim

from bs4 import BeautifulSoup
from requests import get

#CLI
import sys #for argument parsing

# Exception Handling

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the  URL")

def get_only_text(url):
 """ 
  return the title and the text of the article
  at the specified url
 """
 page = get(url)
 soup = BeautifulSoup(page.content, "lxml")
 text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
 #text = soup.text
 title = ' '.join(soup.title.stripped_strings)
 return title , text

#Calling the function with the desired News URL
#url = "https://en.wikinews.org/wiki/Global_markets_plunge"
#text = get_only_text(url)

text = get_only_text("https://en.wikinews.org/wiki/Global_markets_plunge")

len(text)

text

#Number of Words - Original Text
text[0]
len(str.split(text[1]))

#Summarization
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

"""Printing the Summarized Text"""

#Method #1 - Word Count

print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), word_count=100))

len(str.split((summarize(repr(text[1]), word_count=100))))

#Number of Words - Summarized Text

print ("Title : " + text[0])
print ("Summary : ")
print (summarize(repr(text[1]), ratio=0.1))

summarized_text = summarize(repr(text[1]), ratio=0.1)

#Number of Words - Summarized Text
len(str.split(summarized_text))

#Method #2 - Keywords
print ('\nKeywords:')
print (keywords(text[1], ratio=0.1, lemmatize=True))