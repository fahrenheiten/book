words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_couts = Counter(words)
top_three  = word_couts.most_common(6)
print(top_three)

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_couts[word] +=1
print(word_couts['eyes'])
print(word_couts.update(morewords))


