## Table of Contents
1. [Installation](#Installation)
2. [Project Overview](#Project-Overview)
3. [File Descriptions](#File-Descriptions)
4. [Results](#Results)
5. [Licensing, Authors, and Acknowledgements](#Licensing,-Authors,-and-Acknowledgements)

## Installation
Python libraries needed to run the code beyond the Anaconda distribution of Python are: pandas, sklearn, and xgboost. The code should run with no issues using Python versions 3.*.

## Project Overview
This is the capstone project of Data Scientist Nanodegree on Udacity.   

In this project, I analyzed demographics data for customers of a mail-order sales company in Germany, comparing it against demographics information for the general population. I used unsupervised learning techniques to perform customer segmentation, identifying the parts of the population that best describe the company's core customer base. 

Then, I applied what I've learned on a third dataset with demographics information for targets of a marketing campaign for the company. I built a machine learning model to predict which individuals are most likely to respond to the campaign and become customers for the company.

AUC (Area under the ROC Curve) is used to evaluate the performance of the model. The metric of the result is a Kaggle competition.

## File Descriptions
There are 6 files associated with this project: 4 .csv data files and 2 .xlsx files including the descriptions about the features.
- Udacity_AZDIAS_052018.csv: Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns).
- Udacity_CUSTOMERS_052018.csv: Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns).
- Udacity_MAILOUT_052018_TRAIN.csv: Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns).
- Udacity_MAILOUT_052018_TEST.csv: Demographics data for individuals who were targets of a marketing campaign; 42 833 persons (rows) x 366 (columns).
- DIAS Information Levels - Attributes 2017.xlsx: A brief classification and description of all the features.
- DIAS Attributes - Values 2017.xlsx: A more detailed description of all the features including the description of specific values.

Consider the Non-Disclosure Agreement, the data is not included in this folder. The data can be found at Udacity.  

All the code with descriptions is in Arvato Project Workbook.ipynb.

## Results
The main findings of the code can be found at the post available [here](https://yuhanxu.medium.com/customer-segmentation-report-for-arvato-financial-services-4ea4eae1f2c8).

## Licensing, Authors, and Acknowledgements
Must give credit to Arvato Financial Solutions and Udacity for the data.
