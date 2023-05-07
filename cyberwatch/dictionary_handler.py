import os
import json
from math import log
from symspellpy import SymSpell

def loadDictionaries():
    global dictionary_words
    global word_cost
    global max_word
    # Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
    current_dir = os.path.dirname(os.path.abspath(__file__))

    dictionary_words = open(os.path.join(current_dir, "dictionaries/frequency_dictionary.txt")).read().split()
    word_cost = dict((k, log((i + 1) * log(len(dictionary_words)))) for i, k in enumerate(dictionary_words))
    max_word = max(len(x) for x in dictionary_words)

    # load spelling check dictionary
    global sym_spell
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    dictionary_path = os.path.join(current_dir, "dictionaries/main_dictionary.txt")
    term_index = 0
    count_index = 1
    if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
        print("Dictionary file not found!")

    # load slang dictionary
    global slang_dict
    file = open(os.path.join(current_dir, 'dictionaries/slang_disctionary.json'))
    slang_dict = json.load(file)