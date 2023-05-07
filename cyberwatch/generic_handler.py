import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import sys
sys.path.append('nlp')

from cyberwatch.nlp.emoji_handler import removeEmojis, removeEmoticons
from cyberwatch.nlp.slangs_handler import mapSlangToTerm
from cyberwatch.nlp.spelling_corrector import spellingChecker
from cyberwatch.nlp.text_splitter import infer_spaces
nltk.download('words')

def normalize(str, spelling: dict=True, hashtag: dict=True, slang: dict=True):
    print(str)

    # ---- Case Conversion (Lowering) ----
    refactored_str = str.lower()
    
    # ---- Remove Emails----
    refactored_str = re.sub(r'[A-Za-z0-9]*@[A-Za-z]*\.?[A-Za-z0-9]*', "", refactored_str)
    refactored_str = " ".join(refactored_str.split())
    
    # ---- Remove URLs----
    refactored_str = re.sub(r'https\S+', '', refactored_str)
    refactored_str = re.sub(r'http\S+', '', refactored_str)
    refactored_str = re.sub(r'www\S+', '', refactored_str)
    
    # ---- Remove Emojis
    refactored_str = removeEmojis(refactored_str)
    
    # ---- Remove Emoticons
    refactored_str = removeEmoticons(refactored_str)
    
    # ---- Remove Numeric ----
    refactored_str = re.sub(r'\d+', '', refactored_str)
    
    # ---- Remove Punctuations except words and space----
    refactored_str = re.sub(r'[^\w\s]', '', refactored_str)

    # ---- Remove Whitespaces----
    pattern = re.compile(r'\s+')
    refactored_str = re.sub(pattern, ' ', refactored_str)
    refactored_str = refactored_str.strip()

    # ----- Tokenize -----
    words = word_tokenize(refactored_str.lower())

    # ---- Remove stopwords and non-alphabetic characters----
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # ---- Convert slang words to terms ----
    # print(words)
    if slang:
        print("slang")
        words = mapSlangToTerm(words)
        refactored_str = " ".join(words)
        words = word_tokenize(refactored_str)

    # ---- Remove stopwords and non-alphabetic characters----
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalpha() and word not in stop_words]

    # ---- Spelling Checker ----
    if spelling:
        print("spelling")
        words = spellingChecker(words)

    # ---- Split texts without spaces (Split HashTag Text)----
    if hashtag:
        print("hashtag")
        words = infer_spaces(words)

        # ---- Remove stopwords and non-alphabetic characters----
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word.isalpha() and word not in stop_words]

    # ---- Remove words with repeated letters ----
    pattern = re.compile(r'(\w)\1{2,}')
    words = [word for word in words if not pattern.search(word)]

    # ---- Lemmatizing ----
    lemmatizer = WordNetLemmatizer()
    for i in range(len(words)):
        lemmatized_word = lemmatizer.lemmatize(words[i])
        words[i] = lemmatized_word

     # ---- Remove stopwords and non-alphabetic characters----
    existing_stopwords = set(stopwords.words('english'))
    custom_stopwords = ['a', 'ing', 'u', 'th', 'nx', 'et', 'cetera']
    stop_words = existing_stopwords.union(custom_stopwords)
    words = [word for word in words if word.isalpha() and word not in stop_words]

    text = ' '.join(words)
    text = remove_one_letter_words(text)

    print(text)

    return text

def remove_one_letter_words(text):
    # Use regular expression to match and remove one-letter words
    processed_text = re.sub(r'\b\w\b', '', text)
    
    # Remove extra spaces
    processed_text = re.sub(r'\s+', ' ', processed_text)
    
    return processed_text.strip()