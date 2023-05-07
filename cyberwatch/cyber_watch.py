import os
import joblib
from .generic_handler import normalize
from .dictionary_handler import loadDictionaries

class CyberWatch:
    def __init__(self):
        loadDictionaries()
    
        current_dir = os.path.dirname(os.path.abspath(__file__))

        model_path = os.path.join(current_dir, "random_forest_model.pkl")
        vectorizer_path = os.path.join(current_dir, "random_forest_vectorizer.pkl")

        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)

    def predict(self, text, spelling: dict=True, hashtag: dict=True, slang: dict=True):
        new_data = [normalize(text, spelling, hashtag, slang)]
        X_new = self.vectorizer.transform(new_data)
        predictions = self.model.predict(X_new)
        return predictions[0]
