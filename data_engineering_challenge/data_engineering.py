# Import required packages
import requests
import json
from spatialite_database import SpatialiteDatabase
import sqlite3
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_report(data_url_path):
    """
    Reads the data from the url and converts to text.
    Additionally, it gives a report about data results.

    Args:
        data_url_path (str):
            Path to the data
    """

    print("Getting data results...")

    # Values used to determine the data included in the report instance – such as attribute values,
    # metric values and view filters. JSON format. Leave empty to import everything
    data_details = ""
    r = requests.get(data_url_path, data=data_details)
    if r.ok:
        print("Data results received...")
        print("HTTP %i - %s" % (r.status_code, r.reason))
        return r.text
    else:
        print("HTTP %i - %s" % (r.status_code, r.reason))


def export_to_json(data_url_path):
    """
    Reads the data from the url and exports it to a json file.

    Args:
        data_url_path (str):
            Path to the data
    """

    print("Exporting data results to JSON file...")
    r = get_report(data_url_path)
    text_file = open("results.json", "w", encoding="utf8")
    text_file.write(r)
    print("Exported data results to JSON file...")
    text_file.close()


def export_to_csv(data_url_path):
    """
    Reads the data from the url and exports it to a json file.

    Args:
        data_url_path (str):
            Path to the data
    """

    print("Exporting data results to CSV file...")

    csv_file = open('report_results.csv', "w", encoding="utf8")
    csv_file.write("gender; title; first; last; street_number; street_name; city; state; country; postcode; "
                   "latitude;longitude; timezone_offset; timezone_description;email; dob; age; id_name; "
                   "id_value; picture_large; picture_medium; picture_thumbnail; nationality "+"\n")
    csv_file.close()

    # Load the data as json
    r = get_report(data_url_path)
    contents = json.loads(r)

    # Write data results into a CSV
    print("Writing data results to CSV file...")
    for a1 in contents:
        if a1 == 'results':
            for a2 in contents[a1]:
                print(a2)
                val1 = a2['gender']
                print(val1)
                val2 = a2['name']['title']
                print(val2)
                val3 = a2['name']['first']
                print(val3)
                val4 = a2['name']['last']
                print(val4)
                val5 = str(a2['location']['street']['number'])
                print(val5)
                val6 = a2['location']['street']['name']
                print(val6)
                val7 = a2['location']['city']
                print(val7)
                val8 = a2['location']['state']
                print(val8)
                val9 = a2['location']['country']
                print(val9)
                val10 = str(a2['location']['postcode'])
                print(val10)
                val11 = str(a2['location']['coordinates']['latitude'])
                print(val11)
                val12 = str(a2['location']['coordinates']['longitude'])
                print(val12)
                val13 = str(a2['location']['timezone']['offset'])
                print(val13)
                val14 = a2['location']['timezone']['description']
                print(val14)
                val15 = a2['email']
                print(val15)
                val16 = str(a2['dob']['date'])
                print(val16)
                val17 = str(a2['dob']['age'])
                print(val17)
                val18 = a2['id']['name']
                print(val18)
                val19 = str(a2['id']['value'])
                print(val19)
                val20 = a2['picture']['large']
                print(val20)
                val21 = a2['picture']['medium']
                print(val21)
                val22 = a2['picture']['thumbnail']
                print(val22)
                val23 = a2['nat']
                print(val23)
                csv_file = open('report_results.csv', "a", encoding="utf8")
                print("csv file opened")
                csv_file.write(val1 + ";" + val2 + ";" + val3 + ";" + val4 + ";" + val5 + ";" + val6 + ";" + val7 + ";"
                               + val8 + ";" + val9 + ";" + val10 + ";" + val11 + ";" + val12 + ";" + val13 + ";" + val14
                               + ";" + val15 + ";" + val16 + ";" + val17 + ";" + val18 + ";" + val19 + ";" + val20 + ";"
                               + val21 + ";" + val22 + ";" + val23 + "\n")
                csv_file.close()
        else:
            continue

    print("Export finished")


class Database(SpatialiteDatabase):
    """
    The Database class represents a Spatialite database for creating a database with data results.

    Args:
        spatialite_filepath (str):
            File path of the Spatialite extension
    """

    def __init__(self, database_filepath, spatialite_filepath="mod_spatialite"):
        SpatialiteDatabase.__init__(self, database_filepath, spatialite_filepath)

    def create_tables(self):
        """
        Creates all necessary tables in the database. These are:
            FlightData : Stores the Flight Data coming from the API.
        """

        # Create table FlightData
        sql_statement = "CREATE TABLE FlightData ("
        sql_statement += "id                        INTEGER PRIMARY KEY, "
        sql_statement += "gender                    TEXT, "
        sql_statement += "title                     TEXT, "
        sql_statement += "first                     TEXT,"
        sql_statement += "last                      TEXT, "
        sql_statement += "street_number             INTEGER, "
        sql_statement += "street_name               TEXT, "
        sql_statement += "city                      TEXT, "
        sql_statement += "state                     TEXT, "
        sql_statement += "country                   TEXT, "
        sql_statement += "postcode                  INTEGER, "
        sql_statement += "latitude                  FLOAT, "
        sql_statement += "longitude                 FLOAT, "
        sql_statement += "timezone_offset           FLOAT, "
        sql_statement += "timezone_description      TEXT, "
        sql_statement += "email                     TEXT, "
        sql_statement += "dob                       FLOAT, "
        sql_statement += "age                       FLOAT, "
        sql_statement += "id_name                   TEXT, "
        sql_statement += "id_value                  TEXT, "
        sql_statement += "picture_large             TEXT, "
        sql_statement += "picture_medium            TEXT, "
        sql_statement += "picture_thumbnail         TEXT, "
        sql_statement += "nationality               TEXT)"
        self.connection.execute(sql_statement)
        print("Table District created")

    def import_data(self, data_filepath):
        """
        Imports flight data from the given filepath.
            data_filepath : File path to the Flight data.
        """

        # Read columns district, total population, male population, female population and number
        # of households from input CSV file
        print("Starting import")
        file = open(data_filepath)
        rows = csv.reader(file, delimiter=";")
        next(rows, None) # Skip headers

        # Insert the data to the PopulationDistribution table
        sql_statement = "INSERT INTO FlightData (gender, title, first, last, street_number, street_name, " \
                            "city,state, country,postcode, latitude,longitude, timezone_offset, " \
                            "timezone_description,email, dob, age, id_name, id_value, picture_large, " \
                            "picture_medium, picture_thumbnail, nationality) "
        sql_statement += "VALUES (?, ?, ?, ?, ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        for row in rows:
            self.cursor.execute(sql_statement, row)

        self.connection.commit()
        print("Flight data added")


def export_chart_country(data_file_path):
    """
    Exports a pie chart with percentage of data for each country.

    Args:
    data_file_path (str):
        File path of the exported CSV file
    """

    # Read csv as pandas dataframe
    fight_data = pd.read_csv(data_file_path, sep=';')
    fight_data_df = pd.DataFrame(fight_data)

    # Group data for unique values of the country
    fight_data_df_group = fight_data_df.groupby([' country'])[' country'].count()

    # Plot and save a pie distribution
    labels = fight_data_df_group.index

    # Define Seaborn color palette to use
    colors = sns.color_palette('pastel')[0:5]

    # Create pie chart
    plt.pie(fight_data_df_group, labels=labels, colors=colors, autopct='%.0f%%')
    plt.savefig('saved_figure_country.png', dpi=300, bbox_inches = "tight")
    plt.close()


def export_chart_avg_age_by_country(data_file_path):
    """
    Exports a line chart with average age observed for each country.

    Args:
    data_file_path (str):
        File path of the exported CSV file
    """

    # Read csv as pandas dataframe
    fight_data = pd.read_csv(data_file_path, sep=';')
    fight_data_df = pd.DataFrame(fight_data)

    # Group data for average age of each country and plot a line chart
    fight_data_df.groupby([' country'])[' age'].mean().plot(linewidth=10)

    plt.xlabel("Country")
    plt.ylabel("Average Age observed for each country")
    plt.title("Distribution of average age observed for each country")
    plt.savefig('saved_figure_avg_age.png', dpi=300, bbox_inches = "tight")
    plt.close()


def export_chart_age_dist_by_country(data_file_path):
    """
    Exports a box plot age distribution observed for each country.

    Args:
    data_file_path (str):
        File path of the exported CSV file
    """

    # Read csv as pandas dataframe
    fight_data = pd.read_csv(data_file_path, sep=';')
    fight_data_df = pd.DataFrame(fight_data)

    sns.set_theme(style="ticks", palette="pastel")

    # Define figure size
    sns.set(font_scale=1.2)

    # Create a boxplot
    sns.boxplot(x=" country", y=" age",palette=["m", "g"], data=fight_data_df).set(xlabel='Country', ylabel='Age Distribution', title='Age distribution observed for each country')

    plt.savefig('age_distribution.png', dpi=300, bbox_inches = "tight")
    plt.close()


def export_chart_gender_dist_by_country(data_file_path):
    """
    Exports a cat plot with distribution of gender observed for each country.

    Args:
    data_file_path (str):
        File path of the exported CSV file
    """

    # Read csv as pandas dataframe
    fight_data = pd.read_csv(data_file_path, sep=';')
    fight_data_df = pd.DataFrame(fight_data)

    # Define font size
    sns.set(font_scale=1.05)

    # Plot a catplot for distribution of gender in each country
    plot_gender = sns.catplot(data=fight_data_df, kind='count', x=' country', hue='gender').set(title='Gender distribution in country')

    plot_gender.set_xlabels('Country', fontsize=15)
    plot_gender.set_ylabels("Count for each gender", size=14)
    plt.savefig('saved_figure_gender.png', dpi=300, bbox_inches = "tight")
    plt.close()


def main():
    # Path to data url
    data_url_path = "https://randomuser.me/api/?results=300&nat=de,dk,fr,gb&inc=id,gender,name,location,email,dob,picture,nat&seed=flightright"

    # Path to CSV file
    data_file_path = "/home/shinde/Documents/Personal/Applications/Flightright/FlightRightCodeTest/report_results.csv"

    # Setup path to the database
    db = Database("/home/shinde/Documents/Personal/Applications/Flightright/test.sqlite",
                  '/usr/lib/x86_64-linux-gnu/mod_spatialite.so.7.1.0')

    option = None
    while option != "0":
        print(
            """
        ---MENU---

        0 - Exit
        1 - Export data results to JSON file
        2 - Export data results to CSV file
        3 - Export report results to a db
        4 - Export statistics chart for each country
        5 - Export statistics chart for average age of each country
        6 - Export statistics chart for distribution of age for each country
        7 - Export statistics chart for count genders in each country
        """
        )

        option = input("Your option: ")  # What To Do ???
        print()

        if option == "0":
            print("Good bye!")
        elif option == "1":
            export_to_json(data_url_path)
        elif option == "2":
            export_to_csv(data_url_path)
        elif option == "3":
            # Example logging output
            print("Flight Database started")

            try:
                db.connect()
            except sqlite3.OperationalError:
                print("Spatialite extension cannot be loaded. Exiting ...")
                exit()
            db.create_tables()
            db.import_data(data_file_path)
        elif option == "4":
            export_chart_country(data_file_path)
        elif option == "5":
            export_chart_avg_age_by_country(data_file_path)
        elif option == "6":
            export_chart_age_dist_by_country(data_file_path)
        elif option == "7":
            export_chart_gender_dist_by_country(data_file_path)
        else:
            print(" ### Wrong option ### ")


# Main program
main()
