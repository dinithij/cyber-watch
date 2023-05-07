import pandas as pd
import random

def append_bullying_words(input_file, output_file):
    # Read the data from the input CSV file
    data = pd.read_csv(input_file)
    data = data.dropna(subset=['tweet_text'])
    
    # Define the bullying words
    bullying_words = [
    "loser", "idiot", "stupid", "ugly", "fat", "weak", "dumb", "moron", "freak", "retard",
    "worthless", "pathetic", "jerk", "lame", "ignorant", "incompetent", "liar", "weirdo",
    "slacker", "failure", "coward", "nasty", "mean", "horrible", "arrogant", "rude",
    "disgusting", "trash", "vicious", "cruel", "hateful", "abusive", "spiteful", "malicious",
    "sneaky", "manipulative", "heartless", "vindictive", "scheming", "destructive",
    "intolerant", "obnoxious", "vulgar", "insensitive", "unkind", "pompous", "harsh", "sadistic",
    "narcissistic", "mean-spirited", "derogatory", "unpleasant", "menacing", "despicable", "loathsome", "contemptible",
    "deplorable", "ruthless", "brutal"]
    
    # Iterate over the rows and append bullying words randomly for cyberbullying records
    for index, row in data.iterrows():
        if row["cyberbullying_type"] == "cyberbullying" and random.random() <= 0.7:
            tweet_text = row["tweet_text"]
            tweet_words = tweet_text.split()
            bullying_word = random.choice(bullying_words)
            random_index = random.randint(0, len(tweet_words))
            tweet_words.insert(random_index, bullying_word)
            modified_text = " ".join(tweet_words)
            data.at[index, "tweet_text"] = modified_text
    
    # Write the modified data to the output CSV file
    data.to_csv(output_file, index=False)

append_bullying_words('./cyberbullying_tweets_normalized_10000_V1.csv','./cyberbullying_tweets_normalized_10000_V2.csv')
