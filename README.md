# FlightRightCodeTest
This repository contains the answers for my FlightRight coding test. Additionally explanations to those answers.

## 1. Data Engineering Exercise

The python program to run the below queries can be found in the folder: data_engineering_challenge/.
Clone the entire repository and run data_engineering.py in your terminal. The program is designed in a such a fashion that it assigns each below query to a certain option to be chosen by the user.

The program requires you to manually type in the following:

1. Rest API URL.
2. The path to the csv file exported while running the program.
3. The path to store all the outputs of the program (if not specified, the program stores all outputs in the working directory).
4. The path to set up the Spatialite database.

### a. Python program that pulls data from the rest api

The rest api is read and exported to a json file. 

### b. CSV with all the data

The rest api is read again and written to a CSV file. 

### c. Database with all the data

The program creates a connection to the spatialite database with spatialite.py. 
And reads the data from the exported CSV in query b. The database contains a single table called FlightData as I thought the data values were belonging to a single category 
and it was best to keep them in one table. Although I do think I could have created tables for nationality and gender and assigned the ids back to the FlightRight table (Couldn't do it with lack of time :( )

### d. Generating readable statistics

- Entries for each country:  
    Exports a pie chart with the percentage entries for each country.
    The pie chart helps visualise the proportion of data captured by each country.


- Average age for each country:  
    Exports a line chart with the average age for each country. This also helps clearly show the difference between the average ages for each country.


- Age distribution for each country:  
    Exports a box plot with age distribution for each country which I assumed would be an interesting data distribution to look at and analyse.


- Count genders for each country:  
    Exports a bar chart with gender distribution for each country.

Possible prospects: The statistics for gender vs age for each country would also be something interesting to look at. 

## Dependencies
The program requires importing spatialitedatabase.py. 

## Requirements

- Python 3.x 
- Pandas (0.2.2.0 or later)
- sqlite3
- seaborn
- matplotlib
- json
- csv

## 2. Predict Cancellations

PySpark is new to me, it was a challenge. I understood the working of Logistic Regression having worked with it before but with PySpark it was slightly a challenge. 
But quite a fantastic learning experience. 

You will find a Jupyter notebook with the workings in the predict_cancellations folder.


## Requirements

- Python 3.x
- IPython notebooks
- Pandas (0.2.2.0 or later)
- PySpark
- matplotlib