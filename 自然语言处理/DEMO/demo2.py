from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(sent_tokenize(mytext))#句子拆分
print(word_tokenize(mytext))#单词拆分
