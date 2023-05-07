from matplotlib import pyplot as plt
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib

def trainSvmModel(x_train, x_test, y_train, y_test):
    # Vectorize the text data using TF-IDF
    # vectorizer = TfidfVectorizer()
    vectorizer = CountVectorizer(max_features=500)
    #vectorizer = TfidfVectorizer(max_features=2000)

    X_train_tfidf = vectorizer.fit_transform(x_train)
    X_test_tfidf = vectorizer.transform(x_test)

    # Train the SVM model
    svm_classifier = SVC(kernel='linear')
    svm_classifier.fit(X_train_tfidf, y_train)

    # Test the model
    y_pred = svm_classifier.predict(X_test_tfidf)
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
    plt.title("Confusion Matrix for SVM Classifier")
    plt.show()

    print("----------------------------")
    print("        SVM")
    print("----------------------------")
    print("Accuracy:", accuracy)
    print("Precision:\n", precision)
    print("Recall:\n", recall)
    print("F1 Score:\n", f1)
    print("Confusion Matrix:\n", conf_matrix)
    
    #Save model
    joblib.dump(svm_classifier, "./models/svm_model.pkl")