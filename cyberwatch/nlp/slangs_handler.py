from symspellpy import Verbosity
from nltk.corpus import words as engWords
import cyberwatch.dictionary_handler as dictionary_handler

def mapSlangToTerm(words):
        result = 0
        mapped_text = []
        for word in words:
            # Check for an exiting word in the english dictionary
            if word not in engWords.words():
                if word in dictionary_handler.slang_dict:
                        mapped_text.append(dictionary_handler.slang_dict[word])
                        result = 1
                else:
                    mapped_text.append(word)
            else:
                mapped_text.append(word)
        return mapped_text
