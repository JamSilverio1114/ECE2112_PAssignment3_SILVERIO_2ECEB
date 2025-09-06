# PROGRAMMING ASSIGNMENT 3
# SILVERIO, Jamille Anne | 2ECE-B

# PROBLEM 2: Save your file as Surname_Pandas-P2.py

#Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.
# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.
# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

# IMPORT PANDAS LIBRARY TO BE USED THROUGHOUT THE PROGRAM
import pandas as pd

# LOAD DATASET
cars = pd.read_csv("cars.csv")

#FIRST 5 ROWS AND ODD-NUMBERED COLUMNS
a = cars.iloc[[0, 1, 2, 3, 4], [1, 3, 5, 7, 9, 11]]

#SELECTS ROWS STARTING FROM INDEX 0 TO 1 (EXCLUSIVE OF 1), WHICH IS THE ROW OF MAZDA RX4
b = cars[0:1]

#ROW OF CAMARO Z28 AND THE COLUMN OF ITS MODEL AND CYL
c = cars.loc[[23], ["Model", "cyl"]]

#ROWS OF MAZDA RX4 WAG, FORD PANTERA L, AND HONDA CIVIC, AND COLUMNS OF ITS MODEL, CYL, AND GEAR
d = cars.loc[[1, 28, 18], ["Model", "cyl", "gear"]]

#DISPLAY EVERYTHING
print(a.to_string(), "\n")
print(b.to_string(), "\n")
print(c.to_string(), "\n")
print(d.to_string(), "\n")