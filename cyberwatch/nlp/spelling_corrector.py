from symspellpy import Verbosity, SymSpell
import cyberwatch.dictionary_handler as dictionary_handler

# global sym_spell
# sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
# dictionary_path = "/Users/dini/Documents/Msc/Dissertation/Project/CyberWatch/dictionaries/main_dictionary.txt"
# term_index = 0
# count_index = 1
# if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
#     print("Dictionary file not found!")

def spellingChecker(words):
    # find spelling mistakes in each word
    for i in range(len(words)):
        suggestions = dictionary_handler.sym_spell.lookup(words[i], Verbosity.CLOSEST, max_edit_distance=2)
        if len(suggestions) > 0 and suggestions[0].term != words[i]:
            words[i] = suggestions[0].term
            #print(f"Spelling mistake found: {word} -> {suggestions[0].term}")
            #for sug in suggestions:
             #   print(sug)
    return words

#spellingChecker(['girls', 'who', 'bullied', 'me', 'in', 'high', 'school', 'are', 'emotions', 'now', 'and', 'im', 'universe'])