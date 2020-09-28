import sys
import pandas as pd
from sqlalchemy import create_engine
import re
import pickle

from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report

def load_data(database_filepath):
    '''
    load the dataset from sqlite database and split the text data and target labels
    
    INPUT:
    database_filepath: str. The file path of the database
    
    OUTPUT:
    X: the text data used to classify the target
    y: the target labels
    category_names: list. The list of the names of the categories
    '''
    # read in file
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table("disasters", engine)
    
    # define features and label arrays
    X = df.message
    y = df.drop(["id", "message", "original", "genre"], axis=1)
    category_names = list(y.columns)
        
    return X, y, category_names


def tokenize(text):
    '''
    process the text data
    
    INPUT:
    text: str. the text data needed to be processed
    
    OUTPUT:
    clean_tokens: the processed text data
    '''
    text = re.sub(r"[^a-zA-Z0-9]", "", text)
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok.lower().strip(" "))
        clean_tokens.append(clean_tok)
    
    return clean_tokens


def build_model():
    '''
    build a pipeline
    
    OUTPUT:
    model_pipeline: the final model pipeline
    '''
    # text processing and model pipeline
    pipeline = Pipeline([("vect", CountVectorizer(tokenizer = tokenize)),
                         ("tfidf", TfidfTransformer()),
                         ("clf", MultiOutputClassifier(RandomForestClassifier()))])

    # define parameters for GridSearchCV
    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2)],
        'vect__stop_words': (None, 'english'),
        'vect__max_df': (0.5, 0.75, 1.0),
        'tfidf__use_idf': (True, False),
        'clf__estimator__min_samples_split': (2, 3, 5),
        'clf__estimator__n_estimators': [10, 20, 50]}

    # create gridsearch object and return as final model pipeline
    model_pipeline = GridSearchCV(pipeline, param_grid = parameters)

    return model_pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    '''
    evaluate the performance of the model
    
    INPUT:
    model: the model we want to evaluate
    X_test: the test part of the text data used to classify the target
    Y_test: the test part of the target labels
    category_names: list. The list of the names of the categories
    '''    
    Y_pred_arr = model.predict(X_test)
    Y_pred = pd.DataFrame(Y_pred_arr, columns = Y_test.columns)
    overall_accuracy = (Y_pred == Y_test.reset_index(drop=True)).mean().mean()
    print("The overall_accuracy is %0.2f." % overall_accuracy*100)
    for i in category_names:
        print("Class: ", i, "\n", classification_report(Y_test[i], Y_pred[i]))
        
        
def save_model(model, model_filepath):
    '''save model as a pickle file
    
    INPUT:
    model: the model object
    model_filepath: str. the filepath to save the model
    '''
    pickle.dump(model, open(model_filepath, "wb"))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()