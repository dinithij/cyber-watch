import re

def handleNegation(text):
    negation_terms = ['not', 'no', 'n\'t']
    negation_window = 5  # Number of words to include in the negation window
    
    # Tokenize the text into individual words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Initialize a list to store the modified words
    modified_words = []
    
    # Iterate through the words
    i = 0
    while i < len(words):
        word = words[i]
        modified_word = word
        
        # Check if the current word is a negation term
        if word in negation_terms:
            # Check the window of words following the negation term
            for j in range(i+1, min(i+1+negation_window, len(words))):
                # Add the "NOT_" prefix to the following words
                modified_word = 'NOT_' + words[j]
                modified_words.append(modified_word)
                
            # Skip the words that have been modified within the window
            i += negation_window
        
        # If the word is not a negation term, add it as it is
        modified_words.append(modified_word)
        i += 1
    
    # Reconstruct the modified text by joining the modified words
    modified_text = ' '.join(modified_words)
    
    return modified_text
