from setuptools import setup, find_packages

setup(
    name='cyberwatch',
    version='0.0.1',
    description='Cyber Watch is a cyber bullying detection library',
    author='Dinithi Jayasinghe',
    author_email='dinithijaya.93@gmail.com',
    packages=find_packages(
        exclude=['dataset','ml','models','internal','venv']),
    package_data={'cyberwatch': ['dictionaries/*.txt','dictionaries/*.json','random_forest_model.pkl','random_forest_vectorizer.pkl']},
    setup_requires=['pytest-runner'],
    install_requires=[
        'pandas',
        'scikit-learn',
        'joblib',
        'symspellpy',
        'nltk'
    ],
)
