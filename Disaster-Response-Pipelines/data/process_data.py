import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    '''Load in two dataset and merge into one dataset
    
    INPUT:
    messages_filepath: str. The file path of the messages dataset
    categories_filepath: str. The file path of the categories dataset
    
    OUTPUT:
    df: the merged dataset
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = messages.merge(categories, how="inner", on="id")
    return df

def clean_data(df):
    '''clean the dataset by splitting the column categories and dropping duplicates
    
    INPUT:
    df: the dataset that needs to be cleaned
    
    OUTPUT:
    df: the cleaned dataset
    '''
    categories = df["categories"].str.split(";", expand=True)
    row = categories.iloc[0]
    categories.columns = row.apply(lambda x: x[:-2])
    
    for column in categories:
        categories[column] = categories[column].apply(lambda x: x[-1])
        categories[column] = categories[column].astype(int)
    
    df.drop(["categories"], axis=1, inplace=True)
    df = pd.concat([df, categories], axis=1)
    
    df.drop_duplicates(keep="first", inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def save_data(df, database_filename):
    '''
    save the dataset into an sqlite database
    
    INPUT:
    df: the dataset needed to be saved
    database_filename: str. The file path to save the file
    '''
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql("disasters", engine, index=False)
 
def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()