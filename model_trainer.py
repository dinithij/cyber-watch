import pandas as pd

from ml.naive_bayes import trainNaiveBayesModel
from ml.random_forest import trainRandomForestModel
from ml.svm import trainSvmModel
from sklearn.model_selection import train_test_split

from cyberwatch.dictionary_handler import loadDictionaries
from cyberwatch.generic_handler import normalize
from nltk.tokenize import word_tokenize

print("---- Load Dictionaries")
loadDictionaries()

print("---- loading data")
dtypes = {'tweet_text': str, 'cyberbullying_type': str}

data = pd.read_csv('./dataset/cyberbullying_tweets_normalized_10000_V2.csv', encoding='utf8', dtype=dtypes)

# Normalize the text and save
# print("---- normalizing")
# data['tweet_text'] = data['tweet_text'].apply(normalize)
# data.to_csv('./cyberbullying_tweets_normalized_10000_v2.csv', index=False, encoding='utf8')

# Remove empty 
data = data.dropna(subset=['tweet_text'])
data = data[data['tweet_text'].apply(lambda x: len(word_tokenize(x))) >=3]

print("---- splitting train and test data")
# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data['tweet_text'], data['cyberbullying_type'], test_size=0.2, random_state=42)

# Train Naive Bayes Model
trainNaiveBayesModel(x_train, x_test, y_train, y_test)

# Train SVM Model
trainSvmModel(x_train, x_test, y_train, y_test)

# Train Random Forest Model
trainRandomForestModel(x_train, x_test, y_train, y_test)
