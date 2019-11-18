from nltk.book import *
#搜索文本中出现的词的上下文
text1.concordance("monstrous")
#搜索文本中相似的词的上下文
text1.similar("monstrous")
#搜索文本中一同出现两个词的上下文
text1.common_contexts(["monstrous","very"])
#词汇分布图
#text4.dispersion_plot(["citizens","democracy","freedom","duties","America"])
#随机输出
text3.generate()
#统计字符
print(len(text3))