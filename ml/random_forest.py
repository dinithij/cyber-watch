from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import joblib

from cyberwatch.nlp.feature_extractor import featuresFromTfIdf


def trainRandomForestModel(x_train, x_test, y_train, y_test):
    # Vectorize the text data using TF-IDF
    #vectorizer = TfidfVectorizer(max_features=2000)
    vectorizer = CountVectorizer(max_features=500)
    X_train_rf = vectorizer.fit_transform(x_train)
    X_test_rf = vectorizer.transform(x_test)

    # Train the Random Forest model
    rf_classifier = RandomForestClassifier(n_estimators=200, class_weight="balanced")
    rf_classifier.fit(X_train_rf, y_train)
    
    # Test the model
    y_pred = rf_classifier.predict(X_test_rf)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, pos_label='cyberbullying')
    recall = recall_score(y_test, y_pred, pos_label='cyberbullying')
    f1 = f1_score(y_test, y_pred, pos_label='cyberbullying')
    conf_matrix = confusion_matrix(y_test, y_pred)

    ig, ax = plt.subplots(figsize=(5, 5))
    ax.matshow(conf_matrix, cmap=plt.cm.Oranges, alpha=0.3)
    for i in range(conf_matrix.shape[0]):
        for j in range(conf_matrix.shape[1]):
            ax.text(x=j, y=i, s=conf_matrix[i, j], va='center', ha='center', size='xx-large')
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title("Confusion Matrix for Random Forest Classifier")
    plt.show()

    print("----------------------------")
    print("       Random Forest")
    print("----------------------------")
    #Print classification report
    print("Accuracy:", accuracy)
    print("Precision:\n", precision)
    print("Recall:\n", recall)
    print("F1 Score:\n", f1)
    print("Confusion Matrix:\n", conf_matrix) 
    
    #Save model
    joblib.dump(rf_classifier, "./models/random_forest_model.pkl")
    joblib.dump(vectorizer, "./models/random_forest_vectorizer.pkl")
    