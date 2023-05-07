from matplotlib import pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib

def trainNaiveBayesModel(x_train, x_test, y_train, y_test):
    # Vectorize the text data
    vectorizer = TfidfVectorizer(max_features=2000)
    #vectorizer = CountVectorizer(max_features=500)
    X_train_counts = vectorizer.fit_transform(x_train)
    X_test_counts = vectorizer.transform(x_test)

    # Train the Naive Bayes model
    nb_classifier = MultinomialNB(alpha=1.0)
    nb_classifier.fit(X_train_counts, y_train)

    # Test the model accuracy
    y_pred = nb_classifier.predict(X_test_counts)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label='cyberbullying')
    recall = recall_score(y_test, y_pred, pos_label='cyberbullying')
    f1 = f1_score(y_test, y_pred, pos_label='cyberbullying')
    conf_matrix = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.matshow(conf_matrix, cmap=plt.cm.Oranges, alpha=0.3)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title("Confusion Matrix for Naive Bayes Classifier")
    plt.show()

    print("----------------------------")
    print("        Naive Bayes")
    print("----------------------------")
    print("Accuracy:", accuracy)
    print("Precision:\n", precision)
    print("Recall:\n", recall)
    print("F1 Score:\n", f1)
    print("Confusion Matrix:\n", conf_matrix)
    
    #Save model
    joblib.dump(nb_classifier, "./models/naive_bayes_model.pkl")



#def predict():
    # print("---- Start test model")
    # Test the model
    # test_text = "You are soooo ugly!!!! 😱😱😱😱😱😱 Nobody likes you!!!! 🤮🤮🤮🤮🤮🤮 Your face looks like it was hit by a truck!!!! 😂😂😂😂😂😂 #ugly #loser #nofriends #fail #sorrynotsorry 🤷‍♀️🤷‍♂️🙅‍♀️🙅‍♂️👎 www.youareugly.com"
    # test_text = normalize(test_text)
    # test_text_vector = vectorizer.fit_transform([test_text])
    # prediction = nb_classifier.predict(test_text_vector)
    # print("---- End test model")

    # if prediction[0] == 'cyberbullying':
    #     print("The text is bullying.")
    # else:
    #     print("The text is not bullying." + prediction[0])