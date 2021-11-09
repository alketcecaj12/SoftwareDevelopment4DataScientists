# Import local package
import text_analyzer
from collections import Counter

list1 = ['hello','hello','hi','hi','hey','hey','yes','no']
list2 = ['hallo','hallo','hey','hi','hey','hey','yes','no']


word_counts = [Counter(list1), Counter(list2)]
#print(word_counts)

# Sum word_counts using sum_counters from text_analyzer
word_count_totals = text_analyzer.sum_counters(word_counts)

print(word_count_totals)