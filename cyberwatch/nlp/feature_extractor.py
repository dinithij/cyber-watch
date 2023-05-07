from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


def featuresFromTfIdf(x_train, x_test):
    vectorizer = TfidfVectorizer(max_features=2000)
    vectorizer = CountVectorizer()
    X_train_tfidf = vectorizer.fit_transform(x_train)
    X_test_tfidf = vectorizer.transform(x_test)
    return X_train_tfidf, X_test_tfidf

def featuresFromBow(str):
    # Bag of Words
    count_vect = CountVectorizer()
    bow = count_vect.fit_transform(str)
    return bow

