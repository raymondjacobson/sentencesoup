# Generate random sentences given input

import sys, urllib3
import numpy as np

def getRandomText(text_lists):
  rn = np.random.random_integers(0, len(text_lists)-1)
  return text_lists[rn]

def getSentence(text):
  """Grabs a sentence (1) from a text"""
  t = []
  str_buff = ""
  for i in range(0, len(text)):
    if text[i] == '\n':
      str_buff += ' '
    elif text[i] not in ['\r', '"']:
      str_buff += text[i]
    if text[i] in [".", "!", "?"] and text[i+1] != '"':
      t.append(str_buff)
      str_buff = ""
  # Grab random line number
  rn = np.random.random_integers(0, len(t)-1)
  chosen = t[rn]
  chosen = chosen.strip()
  chosen = chosen.replace("  ", " ")
  return chosen

num_sentences = int(sys.argv[1])
print "Generating " + str(num_sentences) + " random sentences"

http = urllib3.PoolManager()
texts = [
  "http://ia700508.us.archive.org/1/items/washingtonsquare02870gut/wassq10.txt",
  "http://ia600305.us.archive.org/4/items/TaleOfTwoCities/Dickens-ATaleOfTwoCities_djvu.txt"
]
for i in range(0, num_sentences):
  r = http.request('GET', getRandomText(texts))
  print getSentence(r.data) + "\n\n"
