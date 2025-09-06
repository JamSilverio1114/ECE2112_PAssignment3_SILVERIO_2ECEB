# PROGRAMING ASSIGNMENT 3
PYTHON DATA ANALYSIS (PANDAS)

---

**NAME:** SILVERIO, Jamille Anne &emsp;&emsp;&emsp;&emsp; **DATE SUBMITTED:** Sept. 6, 2025  
**SECTION:** 2ECEB  

---

## I. Intended Learning Outcomes:
1. To identify the codes and functions incorporated in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

---

## II. Instructions:
Write a Python script/code in the Jupyter Notebook to do the given problems. You may submit your Jupyter
notebook in the dedicated submission bin.

---

### PROBLEM 1: 
Save your file as Surname_Pandas-P1.py

Using knowledge obtained from the experiment and demonstrations:

a. Load the corresponding .csv file into a data frame named cars using pandas

b. Display the first five and last five rows of the resulting cars.

**Implementation (My Work):**
```python
#IMPORT PANDAS LIBRARY TO BE USED THROUGHOUT THE PROGRAM
import pandas as pd

# a. Load the corresponding .csv file into a data frame named cars using pandas

#LOAD THE DATASET FROM cars.csv 
cars = pd.read_csv("cars.csv")
#DISPLAY DATAFRAME
cars

# b. Display the first five and last five rows of the resulting cars.

#DISPLAY TEXT
print("Here are the First & Last 5 items on the list: ")
#CONCATENATES THE FIRST AND LAST 5 ROWS OF ITEMS ON THE LIST
combined = pd.concat([cars.head(), cars.tail()])
#DISPLAYS CONCATENATED ITEMS
combined
```
**Code Walkthrough:**

***PART A***
```python
import pandas as pd
```
* I imported the Pandas Library, which I refer to as ```pd``` throughout the code. It is the main tool I will use to work with tabular data.
```python
cars = pd.read_csv("cars.csv")
cars
```
* I used the ```pd.read_csv()``` function to read the ```cars.csv``` file, then stored it into a variable named ```cars```.
* I then displayed the DataFrame by printing ```cars```.

***PART B***
```python
print("Here are the First & Last 5 items on the list: ")
```
* To make the output clear, I first printed a simple text line as a heading.
```python
combined = pd.concat([cars.head(), cars.tail()])
combined
```
* I used two built-in functions: ```cars.head()``` for the first 5 rows, and ```cars.tail()``` for the last 5 rows.
* I placed them inside the ```pd.concat()``` function to merge the two sets of rows into a single DataFrame named ```combined```.
* I then displayed the concatenated DataFrame by printing ```combined```.
  
**Conclusion:**  
The program **successfully** displayed the first and last 5 rows of the DataFrame.

---

### PROBLEM 2:
Save your file as Surname_Pandas-P2.py

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

**Implementation (My Work):**
```python
#IMPORT PANDAS LIBRARY TO BE USED THROUGHOUT THE PROGRAM
import pandas as pd

# a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.

#DISPLAYS THE FIRST 5 ROWS AND ODD-NUMBERED COLUMNS
cars.iloc[[0, 1, 2, 3, 4], [1, 3, 5, 7, 9, 11]]

# b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

#SELECTS ROWS STARTING FROM INDEX 0 TO 1 (EXCLUSIVE OF 1), WHICH IS THE ROW OF MAZDA RX4
cars[0:1]

# c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

#DISPLAYS THE ROW OF CAMARO AND THE COLUMN OF ITS MODEL AND CYL
cars.loc[[23], ["Model", "cyl"]]

# d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

#DISPLAYS THE ROWS OF MAZDA RX4 WAG, FORD PANTERA L, AND HONDA CIVIC
#DISPLAYS THE COLUMNS OF ITS MODEL, CYL, AND GEAR
cars.loc[[1, 28, 18], ["Model", "cyl", "gear"]]
```
**Code Walkthrough:**
```python
import pandas as pd
```
* I imported the Pandas Library, which I refer to as ```pd``` throughout the code. It is the main tool I will use to work with tabular data.
```python
cars.iloc[[0, 1, 2, 3, 4], [1, 3, 5, 7, 9, 11]]
```
* I used the ```iloc[]``` indexer, which allows me to select specific rows & columns based on their integer positions.
* For the first 5 rows, I used the indices ```[0, 1, 2, 3, 4]```, and ```[1, 3, 5, 7, 9, 11]``` for the odd-numbered columns.
```python
cars[0:1]
```
* Since the ‘Mazda RX4’ is located in the very first row of the dataset ```(index 0)```, I used slicing notation ```cars[0:1]``` to extract it.
* It starts from index ```0``` up to, but not including index ```1```.
```python
cars.loc[[23], ["Model", "cyl"]]
```
* I used the ```.loc[]``` indexer, and specified the row index ```[23]``` and selected only the ```"Model"``` and ```"cyl"``` columns to display the model name and cylinder count.
```python
cars.loc[[1, 28, 18], ["Model", "cyl", "gear"]]
```
* I used the ```.loc[]``` indexer again, and specified the row indices for the three models: Mazzda RX4 Wag ```[1]```, Ford Pantera L ```28```, and Honda Civic ```18```.
* I then selected the specified columns: ```"Model"```, ```"cyl"```, and ```"gear"``` to display the model name, cylinder count, and gear.

**Conclusion:**  
The program **successfully** extracted specific data from the ```cars.csv``` dataset using different indexing techniques.

---

**Click here to see my Jupyter Notebook:**  [SILVERIO_2ECEB_PA3.ipynb](https://github.com/JamSilverio1114/ECE2112_PAssignment3_SILVERIO_2ECEB/blob/main/SILVERIO_2ECEB_PA3.ipynb)  
**DATE DUE:** Sept. 10, 2025  

---
