import cyberwatch.dictionary_handler as dictionary_handler

def infer_spaces(words):
    words = list(words)
    result = []

    for index in range(len(words)):
        """Uses dynamic programming to infer the location of spaces in a string
        without spaces."""
        # Find the best match for the i first characters, assuming cost has
        # been built for the i-1 first characters.
        # Returns a pair (match_cost, match_length).
        def best_match(i):
            candidates = enumerate(reversed(cost[max(0, i - dictionary_handler.max_word):i]))
            return min((c + dictionary_handler.word_cost.get(words[index][i - k - 1:i], 9e999), k + 1) for k, c in candidates)

        # Build the cost array.
        cost = [0]
        for i in range(1, len(words[index]) + 1):
            c, k = best_match(i)
            cost.append(c)

        # Backtrack to recover the minimal-cost string.
        out = []
        i = len(words[index])
        while i > 0:
            c, k = best_match(i)
            assert c == cost[i]
            out.append(words[index][i - k:i])
            i -= k

        if len(out) > 1:
            out = reversed(out)
            for word in out:
                 result.append(word)
        elif len(out) == 1:
            result.append(out[0])

    return result
