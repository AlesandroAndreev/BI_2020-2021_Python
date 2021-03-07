This branch contains 6 files:

1) Readme;
2) train.csv - data on the alignment of nucleotide sequences;
3) Script_for_train.py - script for processing train.csv data, contains 2 functions. 1 - Plots a graph of the distribution of nucleotide frequencies; 2 - Saves part of the analyzed data to a separate file train_part.csv;
4) train_part.csv - part of the data taken from train.csv;
5) Titanic.csv - a dataset of passengers on the Titanic ship.
6) Titanic_data_describe.py - a script that analyzes data about the Titanic. All graphs (13 pieces) are displayed in separate windows.

P.S. The final conclusion from Titanic.csv is as follows: The results of the analysis indicate that there are a large number of missing values ​​in the data, so before continuing with further work, it is necessary to exclude the Cabin variable from the data and implicate the data in the Age variable. A correlation was also found between the Fare_Category and Survived variables, which will need to be taken into account when deciding whether to perform regression analysis in the future.