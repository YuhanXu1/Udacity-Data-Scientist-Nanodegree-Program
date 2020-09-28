## Table of Contents
1. [Installation](#Installation)
2. [Project Motivation](#Project-Motivation)
3. [File Descriptions](#File-Descriptions)
4. [Results](#Results)
5. [Licensing, Authors, and Acknowledgements](#Licensing,-Authors,-and-Acknowledgements)

## Installation
Python libraries needed are: pandas, sqlalchemy, re, pickle, nltk, sklearn, plotly, flask, joblib. The code should run with no issues using Python versions 3.*.

## Project Motivation
This is the second project of Data Scientist Nanodegree on Udacity. This project will analyze disaster data from [Figure Eight](https://www.figure-eight.com/) to build a model for an API that classifies disaster messages.

## File Descriptions
Here is the file structure of this project:
- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 

- README.md

### Instructions:
1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/ or http://localhost:3001/

## Results
The results is showed in the web app when you can go to http://0.0.0.0:3001/ or http://localhost:3001/.

## Licensing, Authors, and Acknowledgements
Must give credit to Udacity and [Figure Eight](https://www.figure-eight.com/) for the data.
