#PROGRAMMING ASSIGNMENT 3
#SILVERIO, Jamille Anne | 2ECE-B

#PROBLEM 1: Save your file as Surname_Pandas-P1.py

#Using knowledge obtained from the experiment and demonstrations:
# a. Load the corresponding .csv file into a data frame named cars using pandas
# b. Display the first five and last five rows of the resulting cars.

#IMPORT PANDAS LIBRARY TO BE USED THROUGHOUT THE PROGRAM
import pandas as pd

#LOAD THE DATASET FROM cars.csv 
cars = pd.read_csv("cars.csv")

#DISPLAY TEXT
print("Here are the First & Last 5 items on the list: ")

#CONCATENATES THE FIRST AND LAST 5 ROWS OF ITEMS ON THE LIST
combined = pd.concat([cars.head(), cars.tail()])

# DISPLAYS CONCATENATED ITEMS
print(combined.to_string())