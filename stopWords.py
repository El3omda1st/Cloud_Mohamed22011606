import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def process(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  
    
    words = re.findall(r'\b\w+\b', text)
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    
    word_freq = Counter(filtered_words)
    
    return word_freq

def frequency_table(word_freq):
    print("Word\t\tFrequency")
    for word, freq in word_freq.items():
        print(f"{word.ljust(15)}\t{freq}")

file_path = './paragraphs.txt'

word_freq = process(file_path)

frequency_table(word_freq)
